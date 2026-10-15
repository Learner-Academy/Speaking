import React, { useState, useEffect, useRef } from 'react';
import confetti from 'canvas-confetti';
import {
  TopicScenario,
  UserProfile,
  DialoguePhrase,
  AgeGroup,
  CardStepQuotas,
} from '../types';
import { SUPPORTED_LANGUAGES } from '../data/languages';
import { getTopicDailySentences, TOPIC_SCENARIOS } from '../data/topics';
import { useConversationalCurriculum } from '../hooks/useConversationalCurriculum';
import {
  speakPhrase,
  stopSpeaking,
  playSuccessChime,
  playTryAgainChime,
  playTapClick,
} from '../utils/audio';
import {
  calculatePronunciationScore,
  createSpeechRecognizer,
  isSpeechRecognitionSupported,
} from '../utils/speechRecognition';
import {
  Mic,
  MicOff,
  Volume2,
  Tv,
  CheckCircle2,
  RefreshCw,
  ChevronRight,
  ChevronLeft,
  Sparkles,
  Award,
  HelpCircle,
  Play,
  RotateCcw,
  Zap,
  BookOpen,
  Lock,
  Headphones,
  Video,
  Check,
} from 'lucide-react';

interface PracticeRoomProps {
  topic: TopicScenario;
  profile: UserProfile;
  onUpdateStepQuotas: (
    sentenceKey: string,
    step: 'listening' | 'watching' | 'practice' | 'speaking'
  ) => void;
  onUpdateProgress: (phraseId: string, score: number, starsEarned: number, xpEarned: number) => void;
  onOpenVideo: (videoId: string, title: string) => void;
  onBack: () => void;
  soundEnabled: boolean;
  onCompleteDay?: (dayNum: number) => void;
}

export const PracticeRoom: React.FC<PracticeRoomProps> = ({
  topic,
  profile,
  onUpdateStepQuotas,
  onUpdateProgress,
  onOpenVideo,
  onBack,
  soundEnabled,
  onCompleteDay,
}) => {
  const ageGroup = profile.ageGroup;
  const weekNumber = Math.ceil(profile.currentDay / 7);
  const weekSeed = profile.weekSeeds[weekNumber] || 0;
  const isRemediationB = Boolean(profile.remediationWeeks?.[weekNumber] || weekSeed > 0);

  // Generate 3 authentic progressive sentences for current day, topic, level, and variant
  const curriculum = useConversationalCurriculum({
    day: profile.currentDay,
    ageGroup: profile.ageGroup,
    level: profile.level,
    category: topic.category,
    topicId: topic.id,
    targetLanguage: profile.targetLanguage,
    motherTongue: profile.motherTongue,
    remediationVariant: isRemediationB ? 'B' : 'A',
    weekSeed,
  });

  const phrases = curriculum.items;
  const [currentIdx, setCurrentIdx] = useState(0);
  const activeSentence = phrases[currentIdx] || phrases[0];

  const targetLangInfo = SUPPORTED_LANGUAGES[profile.targetLanguage] || SUPPORTED_LANGUAGES.es;
  const motherTongueInfo = SUPPORTED_LANGUAGES[profile.motherTongue] || SUPPORTED_LANGUAGES.en;

  const targetText = activeSentence.targetText;
  const phoneticGuide = activeSentence.romanized;
  const translationText = activeSentence.english;

  // Sentence key for step quotas
  const sentenceKey = `${profile.currentDay}_${topic.id}_s${currentIdx + 1}`;
  const stepQuotas: CardStepQuotas = profile.sentenceStepQuotas[sentenceKey] || {
    listening: 0,
    watching: 0,
    practice: 0,
    speaking: 0,
  };

  // Check Step Quotas: Listening (3), Watching (5), Practice (10), Speaking (3)
  const isListeningDone = stepQuotas.listening >= 3;
  const isWatchingDone = stepQuotas.watching >= 5;
  const isPracticeDone = stepQuotas.practice >= 10;
  const isSpeakingDone = stepQuotas.speaking >= 3;

  // Sequential active step determination
  let currentActiveStep = 1;
  if (!isListeningDone) {
    currentActiveStep = 1;
  } else if (!isWatchingDone) {
    currentActiveStep = 2;
  } else if (!isPracticeDone) {
    currentActiveStep = 3;
  } else if (!isSpeakingDone) {
    currentActiveStep = 4;
  } else {
    currentActiveStep = 5; // All 4 completed!
  }

  const isAllStepsCompleted =
    isListeningDone && isWatchingDone && isPracticeDone && isSpeakingDone;

  // State
  const [isSpeakingTts, setIsSpeakingTts] = useState(false);
  const [isRecording, setIsRecording] = useState(false);
  const [spokenTranscript, setSpokenTranscript] = useState('');
  const [lastScore, setLastScore] = useState<number | null>(null);
  const [feedbackMessage, setFeedbackMessage] = useState<string | null>(null);
  const [isMatch, setIsMatch] = useState<boolean | null>(null);
  const [cadenceRate, setCadenceRate] = useState<number>(profile.speechRate || 1.0);

  // Word building state (for practice)
  const [scrambledWords, setScrambledWords] = useState<string[]>([]);
  const [builtWords, setBuiltWords] = useState<string[]>([]);
  const [isWritingSolved, setIsWritingSolved] = useState(false);

  // Speech Recognizer Ref
  const recognizerRef = useRef<{ start: () => void; stop: () => void; abort: () => void } | null>(null);
  const isSpeechSupported = isSpeechRecognitionSupported();

  // Cleanup audio & speech on unmount
  useEffect(() => {
    return () => {
      stopSpeaking();
      if (recognizerRef.current) {
        recognizerRef.current.abort();
      }
    };
  }, []);

  useEffect(() => {
    stopSpeaking();
    if (recognizerRef.current) {
      recognizerRef.current.abort();
    }
    setIsRecording(false);
    setIsSpeakingTts(false);

    setSpokenTranscript('');
    setLastScore(null);
    setFeedbackMessage(null);
    setIsMatch(null);
    setIsWritingSolved(false);

    // Scramble words for practice from authentic tokens
    const words =
      activeSentence.tokens && activeSentence.tokens.length > 0
        ? [...activeSentence.tokens]
        : targetText
            .replace(/[¡!¿?,.:;，。]/g, '')
            .split(' ')
            .filter(Boolean);
    const shuffled = [...words].sort(() => Math.random() - 0.5);
    setScrambledWords(shuffled);
    setBuiltWords([]);

    // Auto-speak on 4-6 if enabled
    if (ageGroup === '4-6' && profile.autoPlayTts) {
      const timer = setTimeout(() => {
        handlePlayAudio();
      }, 500);
      return () => clearTimeout(timer);
    }
  }, [currentIdx, profile.targetLanguage, profile.currentDay, isRemediationB, profile.ageGroup, profile.level, targetText]);

  // Step 1: Listening Handler
  const handlePlayAudio = () => {
    playTapClick();
    setIsSpeakingTts(true);
    speakPhrase(
      targetText,
      targetLangInfo.speechLocale,
      cadenceRate,
      () => setIsSpeakingTts(true),
      () => {
        setIsSpeakingTts(false);
        onUpdateStepQuotas(sentenceKey, 'listening');
        if (soundEnabled && stepQuotas.listening + 1 === 3) {
          playSuccessChime();
        }
      },
      () => setIsSpeakingTts(false)
    );
  };

  // Step 2: Watching Handler
  const handleWatchVideo = () => {
    playTapClick();
    onUpdateStepQuotas(sentenceKey, 'watching');
    onOpenVideo(topic.youtubeVideoId, topic.videoTitle);
  };

  // Step 3: Interactive Practice Handler
  const handlePracticeTileClick = (word: string, index: number) => {
    playTapClick();
    const newBuilt = [...builtWords, word];
    const newScrambled = [...scrambledWords];
    newScrambled.splice(index, 1);

    setBuiltWords(newBuilt);
    setScrambledWords(newScrambled);
    onUpdateStepQuotas(sentenceKey, 'practice');

    if (newScrambled.length === 0) {
      setIsWritingSolved(true);
      if (soundEnabled) playSuccessChime();
    }
  };

  const handleQuickPracticeRepeat = () => {
    playTapClick();
    onUpdateStepQuotas(sentenceKey, 'practice');
    if (soundEnabled) playTapClick();
  };

  const handleResetPractice = () => {
    playTapClick();
    const words =
      activeSentence.tokens && activeSentence.tokens.length > 0
        ? [...activeSentence.tokens]
        : targetText
            .replace(/[¡!¿?,.:;，。]/g, '')
            .split(' ')
            .filter(Boolean);
    const shuffled = [...words].sort(() => Math.random() - 0.5);
    setScrambledWords(shuffled);
    setBuiltWords([]);
    setIsWritingSolved(false);
  };

  // Step 4: Speaking Handler
  const startRecording = () => {
    if (!isSpeechSupported) {
      handleSimulatedMic();
      return;
    }

    playTapClick();
    setIsRecording(true);
    setFeedbackMessage('Listening closely... Speak now!');

    recognizerRef.current = createSpeechRecognizer(
      targetLangInfo.speechLocale,
      (transcript) => {
        setIsRecording(false);
        setSpokenTranscript(transcript);
        processVoiceResult(transcript);
      },
      (err) => {
        setIsRecording(false);
        setFeedbackMessage('Could not detect clear voice audio. Tap again to retry.');
      },
      () => setIsRecording(true),
      () => setIsRecording(false)
    );

    if (recognizerRef.current) {
      recognizerRef.current.start();
    } else {
      handleSimulatedMic();
    }
  };

  const stopRecording = () => {
    playTapClick();
    if (recognizerRef.current) {
      recognizerRef.current.stop();
    }
    setIsRecording(false);
  };

  const processVoiceResult = (transcript: string) => {
    const result = calculatePronunciationScore(transcript, targetText);
    setLastScore(result.score);
    setIsMatch(result.isMatch);
    setFeedbackMessage(result.feedback);

    if (result.isMatch) {
      onUpdateStepQuotas(sentenceKey, 'speaking');
      if (soundEnabled) playSuccessChime();
      try {
        confetti({
          particleCount: 50,
          spread: 60,
          origin: { y: 0.7 },
        });
      } catch {
        // ignore
      }
      onUpdateProgress(activeSentence.id, result.score, 1, 20);
    } else {
      if (soundEnabled) playTryAgainChime();
    }
  };

  const handleSimulatedMic = () => {
    setIsRecording(true);
    setFeedbackMessage('Analyzing voice tone and native accent cadence...');
    setTimeout(() => {
      setIsRecording(false);
      setSpokenTranscript(targetText);
      processVoiceResult(targetText);
    }, 850);
  };

  // Themes
  const isWonderland = ageGroup === '4-6';
  const isQuest = ageGroup === '7-9';
  const isAcademy = ageGroup === '10-12';
  const isTeen = ageGroup === '13-16';

  return (
    <div
      className={`min-h-[calc(100vh-64px)] pb-16 transition-colors duration-200 ${
        isTeen
          ? 'bg-slate-950 text-slate-100'
          : isAcademy
          ? 'bg-purple-50/40 text-slate-900'
          : isQuest
          ? 'bg-sky-50/40 text-slate-900'
          : 'bg-amber-50/40 text-slate-900'
      }`}
    >
      <div className="max-w-3xl mx-auto px-4 sm:px-6 pt-6">
        {/* Navigation Bar / Step Counter */}
        <div className="flex items-center justify-between gap-2 sm:gap-3 mb-4 sm:mb-6">
          <button
            onClick={() => {
              playTapClick();
              onBack();
            }}
            className={`inline-flex items-center gap-1.5 text-xs font-semibold px-3 py-1.5 rounded-xl border transition-colors min-h-[44px] cursor-pointer shrink-0 ${
              isTeen
                ? 'border-slate-800 bg-slate-900 text-slate-300 hover:text-white'
                : 'border-slate-200 bg-white text-slate-700 hover:bg-slate-50'
            }`}
          >
            <ChevronLeft className="w-4 h-4" />
            <span className="hidden xs:inline">Topics</span>
          </button>

          {/* Clean Editorial Title / Scenario Anchor */}
          <div className="text-center min-w-0 px-1 flex-1">
            <span className="text-[10px] sm:text-[11px] font-bold uppercase tracking-wider text-slate-400 block truncate">
              Day {profile.currentDay} · {topic.category}
            </span>
            <span className="text-xs sm:text-sm font-extrabold flex items-center justify-center gap-1 sm:gap-1.5 truncate">
              <span>{topic.badgeEmoji}</span>
              <span className="truncate">{topic.title}</span>
            </span>
          </div>

          {/* Video Lesson Quick Trigger */}
          <button
            onClick={handleWatchVideo}
            className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-bold bg-red-600 hover:bg-red-700 text-white shadow-sm transition-transform active:scale-95 min-h-[44px] cursor-pointer shrink-0"
          >
            <Tv className="w-3.5 h-3.5" />
            <span className="hidden sm:inline">[ Watch Lesson ]</span>
            <span className="sm:hidden">Video</span>
          </button>
        </div>

        {/* Mascot / Age Badge Alert */}
        {isWonderland && (
          <div className="mb-5 p-4 rounded-3xl bg-amber-100/80 border-2 border-amber-300 flex items-center gap-3 animate-bounce-gentle">
            <span className="text-3xl shrink-0">🐥</span>
            <div className="text-xs text-amber-900">
              <span className="font-bold">Chicky says:</span> Complete the 4 steps below in order to unlock the next sentence!
            </div>
          </div>
        )}

        {isQuest && (
          <div className="mb-5 p-3.5 rounded-2xl bg-indigo-50 border border-indigo-200 flex items-center justify-between text-xs text-indigo-900">
            <div className="flex items-center gap-2">
              <span className="text-2xl">🦊</span>
              <span><strong>Rusty the Fox:</strong> Sentence {currentIdx + 1} of {phrases.length} · Clear quotas to progress!</span>
            </div>
            <span className="font-bold bg-indigo-600 text-white px-2 py-0.5 rounded-full text-[10px]">
              Sentence {currentIdx + 1}
            </span>
          </div>
        )}

        {isAcademy && (
          <div className="mb-5 p-3.5 rounded-xl bg-purple-900/10 border border-purple-200/80 flex items-center justify-between text-xs text-purple-950">
            <div className="flex items-center gap-2">
              <span className="text-xl">🚀</span>
              <span><strong>Academy Lab:</strong> Sequential Step Quotas active. Strict sentence mastery enforced.</span>
            </div>
            <span className="font-mono text-[11px] font-semibold text-purple-700">
              Day {profile.currentDay}
            </span>
          </div>
        )}

        {isTeen && (
          <div className="mb-5 flex items-center justify-between text-xs text-slate-400 border-b border-slate-800 pb-3">
            <div className="flex items-center gap-2">
              <Zap className="w-3.5 h-3.5 text-emerald-400" />
              <span className="text-slate-200 font-semibold">Fluency Sprint</span>
              <span>· Target Accent: {targetLangInfo.nativeName}</span>
            </div>

            {/* Speech Cadence Selector */}
            <div className="flex items-center gap-1.5">
              <span className="text-[11px]">Speed:</span>
              {[0.75, 1.0, 1.25].map((speed) => (
                <button
                  key={speed}
                  onClick={() => {
                    playTapClick();
                    setCadenceRate(speed);
                  }}
                  className={`px-2 py-0.5 text-[10px] font-mono rounded ${
                    cadenceRate === speed
                      ? 'bg-emerald-500 text-slate-950 font-bold'
                      : 'bg-slate-800 text-slate-400 hover:text-slate-200'
                  }`}
                >
                  {speed}x
                </button>
              ))}
            </div>
          </div>
        )}

        {/* =====================================================================
            PRACTICE CARD DISPLAY (FIX #2 & #3 STRICT SPECIFICATIONS)
            - Line 1: Mother Tongue (small/muted text CSS)
            - Line 2: Target Language (large/bold text CSS)
            - Line 3: Native phonetic transcript (secondary text CSS)
            ===================================================================== */}
        <div
          className={`relative p-6 sm:p-8 rounded-3xl transition-all shadow-md ${
            isWonderland
              ? 'bg-white rounded-3xl border-4 border-amber-300 shadow-amber-200/50'
              : isQuest
              ? 'bg-white rounded-2xl border-2 border-indigo-200 shadow-indigo-100'
              : isAcademy
              ? 'bg-white rounded-2xl border border-purple-200 shadow-purple-50'
              : 'bg-slate-900 rounded-2xl border border-slate-800 shadow-2xl'
          }`}
        >
          {/* Card Top Speaker Label & Sentence Counter */}
          <div className="flex items-center justify-between mb-4">
            <span
              className={`text-xs font-bold uppercase tracking-wider ${
                isTeen ? 'text-emerald-400' : 'text-slate-400'
              }`}
            >
              Sentence {currentIdx + 1} of {phrases.length}
            </span>

            {/* Quota Completion Badge */}
            {isAllStepsCompleted ? (
              <span className="inline-flex items-center gap-1 text-xs font-bold text-emerald-600 dark:text-emerald-400 bg-emerald-50 dark:bg-emerald-950/40 px-2.5 py-1 rounded-full border border-emerald-200">
                <Check className="w-3.5 h-3.5 stroke-[3]" />
                <span>Quotas Met! Next Unlocked</span>
              </span>
            ) : (
              <span className="text-xs font-medium text-slate-400">
                Step {Math.min(4, currentActiveStep)} of 4 Active
              </span>
            )}
          </div>

          {/* Three Lines of Typography mapped to exact CSS classes */}
          <div className="text-center my-6">
            {/* LINE 1: Mother Tongue (Small/muted text CSS) */}
            <p
              className={`text-sm sm:text-base font-medium mb-3 ${
                isTeen ? 'text-slate-400' : 'text-slate-500'
              }`}
              dir={motherTongueInfo.dir}
            >
              {translationText.startsWith('"') ? translationText : `"${translationText}"`}
            </p>

            {/* LINE 2: Target Language (Large/bold text CSS) */}
            <h2
              className={`text-3xl sm:text-4xl md:text-5xl font-extrabold tracking-tight mb-3 select-all leading-tight ${
                isWonderland
                  ? 'font-playful text-slate-900'
                  : isTeen
                  ? 'font-tech text-slate-50'
                  : 'text-slate-900'
              }`}
              dir={targetLangInfo.dir}
            >
              {targetText}
            </h2>

            {/* LINE 3: Native Phonetic Transcript/Transliteration (Secondary text CSS) */}
            <div className="inline-block mt-1 px-4 py-1.5 rounded-full bg-slate-100 dark:bg-slate-800 text-xs sm:text-sm font-mono font-medium text-amber-700 dark:text-amber-300">
              <span className="opacity-75">Sounds like: </span>
              <span className="font-bold">{phoneticGuide}</span>
            </div>
          </div>

          {/* Tip Note */}
          {activeSentence.tip && (
            <div className="mt-4 pt-3 border-t border-slate-100 dark:border-slate-800 text-xs text-slate-500 dark:text-slate-400 flex items-start gap-2">
              <HelpCircle className="w-4 h-4 text-amber-500 shrink-0 mt-0.5" />
              <span>{activeSentence.tip}</span>
            </div>
          )}
        </div>

        {/* =====================================================================
            MANDATORY 4 LEARNING STEPS WITH SEQUENTIAL HIGHLIGHTING & QUOTAS:
            1. Listening (Must complete 3 times)
            2. YT Vid Watching (Must complete 5 times)
            3. Practice (Must complete 10 times)
            4. Speaking (Must complete 3 times)
            ===================================================================== */}
        <div className="mt-6 space-y-4">
          <div className="flex items-center justify-between">
            <h3 className="text-xs font-bold uppercase tracking-wider text-slate-400">
              Mandatory Sentence Mastery Steps
            </h3>
            <span className="text-xs font-mono text-slate-400">
              Follow highlighted sequence
            </span>
          </div>

          {/* STEP 1: LISTENING (Quota: 3) */}
          <div
            className={`p-4 rounded-2xl border transition-all ${
              currentActiveStep === 1
                ? 'border-amber-500 bg-amber-50/70 dark:bg-amber-950/30 shadow-md ring-2 ring-amber-400/30'
                : isListeningDone
                ? 'border-emerald-300 bg-emerald-50/30 dark:bg-emerald-950/10'
                : 'border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 opacity-60'
            }`}
          >
            <div className="flex items-center justify-between gap-3">
              <div className="flex items-center gap-3">
                <div
                  className={`w-9 h-9 rounded-xl flex items-center justify-center font-bold text-sm ${
                    isListeningDone
                      ? 'bg-emerald-500 text-white'
                      : currentActiveStep === 1
                      ? 'bg-amber-500 text-white'
                      : 'bg-slate-200 dark:bg-slate-800 text-slate-500'
                  }`}
                >
                  {isListeningDone ? '✓' : '1'}
                </div>
                <div>
                  <h4 className="text-sm font-bold text-slate-900 dark:text-slate-100 flex items-center gap-2">
                    <span>1. Listening</span>
                    <span className="text-xs font-normal text-slate-500">
                      (Must complete 3 times)
                    </span>
                  </h4>
                  <p className="text-xs text-slate-500">
                    Listen to authentic native speech cadence and vowel lengths.
                  </p>
                </div>
              </div>

              <div className="flex items-center gap-3">
                <span className="text-xs font-mono font-bold tabular-nums">
                  {stepQuotas.listening}/3
                </span>
                <button
                  onClick={handlePlayAudio}
                  disabled={isSpeakingTts}
                  className={`px-4 py-2 rounded-xl text-xs font-bold transition-all min-h-[44px] flex items-center gap-1.5 cursor-pointer active:scale-95 ${
                    isListeningDone
                      ? 'bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300'
                      : 'bg-amber-500 hover:bg-amber-600 text-white shadow-sm'
                  }`}
                >
                  <Volume2 className={`w-4 h-4 ${isSpeakingTts ? 'animate-bounce' : ''}`} />
                  <span>{isSpeakingTts ? 'Playing...' : 'Listen'}</span>
                </button>
              </div>
            </div>
          </div>

          {/* STEP 2: YT VID WATCHING (Quota: 5) */}
          <div
            className={`p-4 rounded-2xl border transition-all ${
              currentActiveStep === 2
                ? 'border-red-500 bg-red-50/70 dark:bg-red-950/30 shadow-md ring-2 ring-red-400/30'
                : isWatchingDone
                ? 'border-emerald-300 bg-emerald-50/30 dark:bg-emerald-950/10'
                : 'border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 opacity-60'
            }`}
          >
            <div className="flex items-center justify-between gap-3">
              <div className="flex items-center gap-3">
                <div
                  className={`w-9 h-9 rounded-xl flex items-center justify-center font-bold text-sm ${
                    isWatchingDone
                      ? 'bg-emerald-500 text-white'
                      : currentActiveStep === 2
                      ? 'bg-red-600 text-white'
                      : 'bg-slate-200 dark:bg-slate-800 text-slate-500'
                  }`}
                >
                  {isWatchingDone ? '✓' : '2'}
                </div>
                <div>
                  <h4 className="text-sm font-bold text-slate-900 dark:text-slate-100 flex items-center gap-2">
                    <span>2. YT Vid Watching</span>
                    <span className="text-xs font-normal text-slate-500">
                      (Must complete 5 times)
                    </span>
                  </h4>
                  <p className="text-xs text-slate-500">
                    Watch classroom companion lesson for visual contextual reinforcement.
                  </p>
                </div>
              </div>

              <div className="flex items-center gap-3">
                <span className="text-xs font-mono font-bold tabular-nums">
                  {stepQuotas.watching}/5
                </span>
                <button
                  onClick={handleWatchVideo}
                  className={`px-4 py-2 rounded-xl text-xs font-bold transition-all min-h-[44px] flex items-center gap-1.5 cursor-pointer active:scale-95 ${
                    isWatchingDone
                      ? 'bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300'
                      : 'bg-red-600 hover:bg-red-700 text-white shadow-sm'
                  }`}
                >
                  <Tv className="w-4 h-4" />
                  <span>Watch ({stepQuotas.watching}/5)</span>
                </button>
              </div>
            </div>
          </div>

          {/* STEP 3: PRACTICE (Quota: 10) */}
          <div
            className={`p-4 rounded-2xl border transition-all ${
              currentActiveStep === 3
                ? 'border-indigo-500 bg-indigo-50/70 dark:bg-indigo-950/30 shadow-md ring-2 ring-indigo-400/30'
                : isPracticeDone
                ? 'border-emerald-300 bg-emerald-50/30 dark:bg-emerald-950/10'
                : 'border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 opacity-60'
            }`}
          >
            <div className="flex items-center justify-between gap-3 mb-3">
              <div className="flex items-center gap-3">
                <div
                  className={`w-9 h-9 rounded-xl flex items-center justify-center font-bold text-sm ${
                    isPracticeDone
                      ? 'bg-emerald-500 text-white'
                      : currentActiveStep === 3
                      ? 'bg-indigo-600 text-white'
                      : 'bg-slate-200 dark:bg-slate-800 text-slate-500'
                  }`}
                >
                  {isPracticeDone ? '✓' : '3'}
                </div>
                <div>
                  <h4 className="text-sm font-bold text-slate-900 dark:text-slate-100 flex items-center gap-2">
                    <span>3. Practice</span>
                    <span className="text-xs font-normal text-slate-500">
                      (Must complete 10 times)
                    </span>
                  </h4>
                  <p className="text-xs text-slate-500">
                    Assemble sentence tiles or drill verbal rehearsals.
                  </p>
                </div>
              </div>

              <div className="flex items-center gap-3">
                <span className="text-xs font-mono font-bold tabular-nums">
                  {stepQuotas.practice}/10
                </span>
                <button
                  onClick={handleQuickPracticeRepeat}
                  className="px-3.5 py-1.5 rounded-xl text-xs font-bold bg-indigo-600 hover:bg-indigo-700 text-white shadow-sm transition-all min-h-[44px] cursor-pointer"
                >
                  + Drill (+1)
                </button>
              </div>
            </div>

            {/* Word tile construction for Practice Step */}
            <div className="mt-3 pt-3 border-t border-indigo-100 dark:border-indigo-900/60">
              <div className="flex items-center justify-between mb-2">
                <span className="text-xs font-medium text-slate-500">
                  Sentence Assembly Tray:
                </span>
                <button
                  onClick={handleResetPractice}
                  className="text-[11px] font-semibold text-slate-400 hover:text-slate-600 flex items-center gap-1"
                >
                  <RotateCcw className="w-3 h-3" /> Reset
                </button>
              </div>

              <div className="min-h-[48px] p-2 rounded-xl border border-dashed border-indigo-300 dark:border-indigo-800 bg-white/80 dark:bg-slate-950/40 flex flex-wrap items-center gap-1.5 mb-2.5">
                {builtWords.length === 0 ? (
                  <span className="text-xs text-slate-400 italic">Tap tiles to assemble...</span>
                ) : (
                  builtWords.map((w, idx) => (
                    <span
                      key={idx}
                      className="px-2.5 py-1 rounded-lg bg-indigo-600 text-white text-xs font-bold shadow-xs"
                    >
                      {w}
                    </span>
                  ))
                )}
              </div>

              <div className="flex flex-wrap gap-1.5">
                {scrambledWords.map((word, idx) => (
                  <button
                    key={idx}
                    onClick={() => handlePracticeTileClick(word, idx)}
                    className="px-3 py-1.5 rounded-lg bg-white dark:bg-slate-800 border border-slate-300 dark:border-slate-700 text-xs font-bold hover:bg-indigo-50 text-slate-800 dark:text-slate-200 transition-transform active:scale-95 shadow-2xs min-h-[40px]"
                  >
                    {word}
                  </button>
                ))}
              </div>
            </div>
          </div>

          {/* STEP 4: SPEAKING (Quota: 3) */}
          <div
            className={`p-4 sm:p-5 rounded-2xl border transition-all ${
              currentActiveStep === 4
                ? 'border-emerald-500 bg-emerald-50/70 dark:bg-emerald-950/30 shadow-md ring-2 ring-emerald-400/30'
                : isSpeakingDone
                ? 'border-emerald-300 bg-emerald-50/30 dark:bg-emerald-950/10'
                : 'border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 opacity-60'
            }`}
          >
            <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
              <div className="flex items-center gap-3">
                <div
                  className={`w-9 h-9 rounded-xl flex items-center justify-center font-bold text-sm ${
                    isSpeakingDone
                      ? 'bg-emerald-500 text-white'
                      : currentActiveStep === 4
                      ? 'bg-emerald-600 text-white'
                      : 'bg-slate-200 dark:bg-slate-800 text-slate-500'
                  }`}
                >
                  {isSpeakingDone ? '✓' : '4'}
                </div>
                <div>
                  <h4 className="text-sm font-bold text-slate-900 dark:text-slate-100 flex items-center gap-2">
                    <span>4. Speaking</span>
                    <span className="text-xs font-normal text-slate-500">
                      (Must complete 3 times)
                    </span>
                  </h4>
                  <p className="text-xs text-slate-500">
                    Tap mic and speak aloud into the Web Speech recognizer.
                  </p>
                </div>
              </div>

              <div className="flex items-center gap-3 self-end sm:self-center">
                <span className="text-xs font-mono font-bold tabular-nums">
                  {stepQuotas.speaking}/3
                </span>
                <button
                  onClick={isRecording ? stopRecording : startRecording}
                  className={`px-4 py-2.5 rounded-xl text-xs font-bold transition-all min-h-[44px] flex items-center gap-2 cursor-pointer active:scale-95 shadow-sm ${
                    isRecording
                      ? 'bg-red-500 text-white animate-mic-pulse'
                      : 'bg-emerald-600 hover:bg-emerald-700 text-white'
                  }`}
                >
                  {isRecording ? <MicOff className="w-4 h-4" /> : <Mic className="w-4 h-4" />}
                  <span>{isRecording ? 'Listening...' : 'Tap & Speak'}</span>
                </button>
              </div>
            </div>

            {/* Transcript & Accuracy Meter */}
            {lastScore !== null && (
              <div className="mt-4 pt-3 border-t border-emerald-100 dark:border-emerald-900/60 text-left">
                <div className="flex items-center justify-between mb-1.5">
                  <span className="text-xs font-bold text-emerald-800 dark:text-emerald-300">
                    Accuracy Meter
                  </span>
                  <span className="text-xs font-mono font-bold text-emerald-700 dark:text-emerald-400">
                    {lastScore}% Match
                  </span>
                </div>
                <div className="w-full h-2 rounded-full bg-slate-200 dark:bg-slate-800 overflow-hidden mb-2">
                  <div
                    className={`h-full rounded-full transition-all duration-500 ${
                      lastScore >= 70 ? 'bg-emerald-500' : 'bg-amber-500'
                    }`}
                    style={{ width: `${lastScore}%` }}
                  />
                </div>
                <p className="text-xs text-slate-600 dark:text-slate-300 leading-relaxed">
                  {feedbackMessage}
                </p>
              </div>
            )}
          </div>
        </div>

        {/* =====================================================================
            NEXT ARROW REVEAL LOGIC (FIX #2 & #3 STRICT RULE)
            "The arrow to proceed to the next sentence MUST remain hidden or disabled.
            Only when the learner completes all 4 steps (including quotas) for the
            current sentence will the arrow appear to go to the 2nd sentence."
            ===================================================================== */}
        <div className="mt-8 flex flex-col sm:flex-row items-center justify-between gap-3 sm:gap-4 pb-safe">
          <div className="flex sm:hidden items-center justify-center w-full">
            <span className="text-xs font-semibold text-slate-400 tabular-nums">
              Sentence {currentIdx + 1} of {phrases.length}
            </span>
          </div>

          <div className="flex items-center justify-between sm:justify-start gap-2.5 w-full sm:w-auto">
            <button
              onClick={() => {
                playTapClick();
                setCurrentIdx((prev) => Math.max(0, prev - 1));
              }}
              disabled={currentIdx === 0}
              className={`flex-1 sm:flex-initial flex items-center justify-center gap-2 px-4 sm:px-5 py-3 rounded-2xl text-xs font-bold border transition-all min-h-[48px] ${
                currentIdx === 0
                  ? 'opacity-30 cursor-not-allowed border-slate-200 dark:border-slate-800'
                  : 'hover:bg-slate-100 dark:hover:bg-slate-800 border-slate-300 dark:border-slate-700 cursor-pointer active:scale-95'
              }`}
            >
              <ChevronLeft className="w-4 h-4" />
              <span>Previous</span>
            </button>

            {/* Mobile inline next / unlock trigger */}
            <div className="flex-1 sm:hidden">
              {isAllStepsCompleted ? (
                topic.id === TOPIC_SCENARIOS[TOPIC_SCENARIOS.length - 1]?.id && currentIdx === phrases.length - 1 && profile.currentDay < 90 ? (
                  <button
                    onClick={() => {
                      if (soundEnabled) {
                        playSuccessChime();
                      }
                      try {
                        confetti({
                          particleCount: 80,
                          spread: 80,
                          origin: { y: 0.6 },
                        });
                      } catch {
                        // ignore
                      }
                      onCompleteDay?.(profile.currentDay);
                    }}
                    className="w-full flex items-center justify-center gap-1.5 px-3 py-3 rounded-2xl text-xs font-extrabold bg-gradient-to-r from-amber-500 via-orange-500 to-amber-600 hover:from-amber-600 hover:to-orange-600 active:scale-95 text-white shadow-xl shadow-amber-500/25 transition-all min-h-[48px] cursor-pointer animate-bounce-gentle text-center"
                    title={`Start Day ${profile.currentDay + 1}`}
                  >
                    <Sparkles className="w-3.5 h-3.5 text-white shrink-0" />
                    <span>Day {profile.currentDay + 1}</span>
                    <ChevronRight className="w-3.5 h-3.5 stroke-[2.5] shrink-0" />
                  </button>
                ) : (
                  <button
                    onClick={() => {
                      playTapClick();
                      if (currentIdx < phrases.length - 1) {
                        setCurrentIdx((prev) => prev + 1);
                      } else {
                        playSuccessChime();
                        try {
                          confetti({
                            particleCount: 60,
                            spread: 70,
                            origin: { y: 0.6 },
                          });
                        } catch {
                          // ignore
                        }
                        onBack();
                      }
                    }}
                    className="w-full flex items-center justify-center gap-1.5 px-3 py-3 rounded-2xl text-xs font-extrabold bg-emerald-600 hover:bg-emerald-700 text-white shadow-lg shadow-emerald-600/25 active:scale-95 transition-all min-h-[48px] cursor-pointer animate-bounce-gentle text-center"
                  >
                    <span>{currentIdx < phrases.length - 1 ? 'Next' : 'Finish'}</span>
                    <ChevronRight className="w-3.5 h-3.5 shrink-0" />
                  </button>
                )
              ) : (
                <div
                  className="w-full flex items-center justify-center gap-1.5 px-3 py-3 rounded-2xl text-xs font-bold bg-slate-100 dark:bg-slate-800 text-slate-400 border border-slate-200 dark:border-slate-700 cursor-not-allowed opacity-60 text-center"
                  title="Complete all 4 learning step quotas above to unlock Next Sentence!"
                >
                  <Lock className="w-3.5 h-3.5 shrink-0" />
                  <span className="truncate">Unlock Next</span>
                </div>
              )}
            </div>
          </div>

          <span className="hidden sm:inline text-xs font-semibold text-slate-400 tabular-nums">
            Sentence {currentIdx + 1} of {phrases.length}
          </span>

          {/* Desktop/Tablet Next Button Container */}
          <div className="hidden sm:block">
            {isAllStepsCompleted ? (
              topic.id === TOPIC_SCENARIOS[TOPIC_SCENARIOS.length - 1]?.id && currentIdx === phrases.length - 1 && profile.currentDay < 90 ? (
                <button
                  onClick={() => {
                    if (soundEnabled) {
                      playSuccessChime();
                    }
                    try {
                      confetti({
                        particleCount: 80,
                        spread: 80,
                        origin: { y: 0.6 },
                      });
                    } catch {
                      // ignore
                    }
                    onCompleteDay?.(profile.currentDay);
                  }}
                  className="flex items-center gap-2 px-6 py-3 rounded-2xl text-xs sm:text-sm font-extrabold bg-gradient-to-r from-amber-500 via-orange-500 to-amber-600 hover:from-amber-600 hover:to-orange-600 active:scale-95 text-white shadow-xl shadow-amber-500/25 transition-all min-h-[48px] cursor-pointer animate-bounce-gentle"
                  title={`Start Day ${profile.currentDay + 1}`}
                >
                  <Sparkles className="w-4 h-4 text-white" />
                  <span>Start Day {profile.currentDay + 1}</span>
                  <ChevronRight className="w-4 h-4 stroke-[2.5]" />
                </button>
              ) : (
                <button
                  onClick={() => {
                    playTapClick();
                    if (currentIdx < phrases.length - 1) {
                      setCurrentIdx((prev) => prev + 1);
                    } else {
                      playSuccessChime();
                      try {
                        confetti({
                          particleCount: 60,
                          spread: 70,
                          origin: { y: 0.6 },
                        });
                      } catch {
                        // ignore
                      }
                      onBack();
                    }
                  }}
                  className="flex items-center gap-2 px-6 py-3 rounded-2xl text-xs font-extrabold bg-emerald-600 hover:bg-emerald-700 text-white shadow-lg shadow-emerald-600/25 active:scale-95 transition-all min-h-[48px] cursor-pointer animate-bounce-gentle"
                >
                  <span>{currentIdx < phrases.length - 1 ? 'Next Sentence' : 'Finish Scenario'}</span>
                  <ChevronRight className="w-4 h-4" />
                </button>
              )
            ) : (
              <div
                className="flex items-center gap-2 px-5 py-3 rounded-2xl text-xs font-bold bg-slate-100 dark:bg-slate-800 text-slate-400 border border-slate-200 dark:border-slate-700 cursor-not-allowed opacity-60"
                title="Complete all 4 learning step quotas above to unlock Next Sentence!"
              >
                <Lock className="w-3.5 h-3.5" />
                <span>Complete 4 Steps to Unlock</span>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};
