import React, { useState } from 'react';
import {
  TopicScenario,
  UserProfile,
  TopicCategory,
} from '../types';
import { TOPIC_SCENARIOS } from '../data/topics';
import { getPracticeContent } from '../data/practiceEngine';
import { getConversationalCurriculum } from '../data/conversationalCurriculum';
import { SUPPORTED_LANGUAGES } from '../data/languages';
import {
  Sparkles,
  Star,
  CheckCircle2,
  Tv,
  ChevronRight,
  Flame,
  Trophy,
  Filter,
  Volume2,
  Compass,
  ArrowUpRight,
  Calendar,
  Lock,
  Award,
  AlertCircle,
  RotateCcw,
} from 'lucide-react';
import { playTapClick, playSuccessChime, speakPhrase } from '../utils/audio';
import confetti from 'canvas-confetti';

interface LearningHubProps {
  profile: UserProfile;
  onSelectTopic: (topicId: string) => void;
  onOpenVideo: (videoId: string, title: string) => void;
  onOpenPreferences: () => void;
  onCompleteDay: (dayNumber: number) => void;
  onOpenRewards: () => void;
  onOpenExam: () => void;
  onFailRestart?: () => void;
  soundEnabled?: boolean;
}

export const LearningHub: React.FC<LearningHubProps> = ({
  profile,
  onSelectTopic,
  onOpenVideo,
  onOpenPreferences,
  onCompleteDay,
  onOpenRewards,
  onOpenExam,
  onFailRestart,
  soundEnabled = true,
}) => {
  const [selectedCategory, setSelectedCategory] = useState<string>('All');

  const ageGroup = profile.ageGroup;
  const isWonderland = ageGroup === '4-6';
  const isQuest = ageGroup === '7-9';
  const isAcademy = ageGroup === '10-12';
  const isTeen = ageGroup === '13-16';

  const targetLang = SUPPORTED_LANGUAGES[profile.targetLanguage] || SUPPORTED_LANGUAGES.es;
  const sourceLang = SUPPORTED_LANGUAGES[profile.motherTongue] || SUPPORTED_LANGUAGES.en;

  // 15 Comprehensive Conversation Categories
  const categories: string[] = [
    'All',
    'Home & Daily Life',
    'Family & Relatives',
    'Travel & Transport',
    'Shopping & Food',
    'Health & Doctor',
    'School & Study',
    'Friends & Play',
    'Nature & Outdoors',
    'Manners & Help',
    'Fun & Tech',
    'Time & Weather',
    'Holidays & Events',
    'Sports & Games',
    'Clothes & Style',
    'Chores & Helping',
  ];

  const filteredTopics = TOPIC_SCENARIOS.filter((topic) => {
    if (selectedCategory === 'All') return true;
    return topic.category === selectedCategory;
  });

  const completedCount = TOPIC_SCENARIOS.filter((t) =>
    profile.completedTopics.includes(t.id)
  ).length;

  const totalProgress = Math.round((completedCount / TOPIC_SCENARIOS.length) * 100);

  // 90-Day Progression Variables
  const currentDay = profile.currentDay;
  const currentMonth = currentDay <= 30 ? 1 : currentDay <= 60 ? 2 : 3;
  const isCurrentDayDone = profile.completedDays.includes(currentDay);

  // Check if today is a test day (weekly test or monthly test)
  const isTestDay =
    currentDay % 7 === 0 || currentDay === 30 || currentDay === 60 || currentDay === 90;
  const hasPassedExamToday = Boolean(profile.examScores[currentDay] && profile.examScores[currentDay] >= 80);

  // Month completion milestone banner
  const isMonth1Completed = profile.completedDays.includes(30);
  const isMonth2Completed = profile.completedDays.includes(60);

  // Mascot speak for 4-6
  const speakChickyInstruction = () => {
    if (soundEnabled) {
      playTapClick();
      speakPhrase(
        `Welcome to LinguaJunior Day ${currentDay}! Tap any picture card to start speaking ${targetLang.label}!`,
        'en-US',
        0.9
      );
    }
  };

  const handleUnlockNextDay = () => {
    if (soundEnabled) {
      playSuccessChime();
    }
    try {
      confetti({
        particleCount: 70,
        spread: 70,
        origin: { y: 0.6 },
      });
    } catch {
      // ignore
    }
    onCompleteDay(currentDay);
  };

  return (
    <div
      className={`min-h-[calc(100vh-64px)] pb-20 transition-colors duration-200 ${
        isTeen
          ? 'bg-slate-950 text-slate-100'
          : isAcademy
          ? 'bg-slate-50 text-slate-900'
          : isQuest
          ? 'bg-indigo-50/30 text-slate-900'
          : 'bg-amber-50/30 text-slate-900'
      }`}
    >
      <div className="max-w-6xl mx-auto px-4 sm:px-6 pt-6 sm:pt-8">
        {/* =========================================================================
            3-MONTH (90-DAY) PROGRESSION ENGINE HEADER BAR
            ========================================================================= */}
        <div
          className={`relative overflow-hidden mb-6 p-5 sm:p-6 rounded-3xl border transition-all ${
            isTeen
              ? 'bg-slate-900/95 border-slate-800 text-slate-100 shadow-xl shadow-black/20'
              : 'bg-gradient-to-br from-white via-white to-amber-50/50 border-slate-200/90 shadow-md shadow-amber-500/5'
          }`}
        >
          {/* Subtle ambient lighting accent */}
          <div
            className="absolute -top-16 -right-16 w-56 h-56 bg-amber-400/10 rounded-full blur-3xl pointer-events-none"
            aria-hidden="true"
          />

          {/* Top Bar Row: Left Month/Day Info & Right Upper Side Beginner Level Badge */}
          <div className="relative flex items-center justify-between gap-3 mb-3.5">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-2xl bg-gradient-to-br from-amber-500 to-orange-500 text-white flex items-center justify-center font-bold text-sm shrink-0 shadow-md shadow-amber-500/20">
                <Calendar className="w-5 h-5" />
              </div>
              <div className="flex flex-col sm:flex-row sm:items-center gap-0.5 sm:gap-2">
                <span className="whitespace-nowrap uppercase tracking-wider text-xs font-bold text-amber-600 dark:text-amber-400">
                  MONTH {currentMonth} OF 3
                </span>
                <span className="whitespace-nowrap text-xs font-bold text-amber-600 dark:text-amber-400">
                  (Day {currentDay}/90)
                </span>
              </div>
            </div>

            {/* Right Upper Side: Learner Level Badge */}
            <div className="shrink-0">
              <span className="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs font-extrabold bg-amber-500/10 dark:bg-amber-400/10 text-amber-700 dark:text-amber-300 border border-amber-300/70 dark:border-amber-600/40 shadow-xs backdrop-blur-xs">
                <Sparkles className="w-3.5 h-3.5 text-amber-500 shrink-0" />
                <span>{profile.level} Level</span>
              </span>
            </div>
          </div>

          {/* Content & Action Row */}
          <div className="relative flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
            <div>
              <h3 className="text-base sm:text-lg font-black tracking-tight text-slate-950 dark:text-white">
                {currentDay <= 30
                  ? 'Foundational Vocabulary & Daily Rituals'
                  : currentDay <= 60
                  ? 'Situational Problem-Solving & Social Quests'
                  : 'Advanced Native Nuance & Full Fluency'}
              </h3>
              <p className={`text-xs sm:text-sm font-semibold mt-1 leading-relaxed ${
                isTeen ? 'text-slate-200' : 'text-slate-700'
              }`}>
                {currentDay <= 30 ? (
                  <>
                    Build your{' '}
                    <span className={`font-bold underline decoration-amber-500 decoration-2 underline-offset-2 ${
                      isTeen ? 'text-amber-400' : 'text-amber-700'
                    }`}>
                      foundational
                    </span>{' '}
                    vocabulary and daily conversational speaking habits.
                  </>
                ) : currentDay <= 60 ? (
                  'Expand into situational problem-solving and dynamic social quests.'
                ) : (
                  'Achieve advanced native nuance, colloquial cadence, and full course fluency.'
                )}
              </p>
            </div>

            {/* Daily Unlock Gate & Rewards Vault Trigger */}
            <div className="flex items-center gap-2.5 w-full sm:w-auto justify-end shrink-0">
              <button
                onClick={() => {
                  playTapClick();
                  onOpenRewards();
                }}
                className={`px-4 py-2.5 rounded-xl text-xs font-bold border transition-all flex items-center gap-1.5 min-h-[44px] cursor-pointer shadow-xs ${
                  isTeen
                    ? 'border-slate-700 bg-slate-800 text-slate-200 hover:bg-slate-700 hover:border-slate-600'
                    : 'border-slate-200/90 bg-white text-slate-700 hover:bg-slate-50 hover:border-slate-300'
                }`}
                title="Open Multi-Tier Rewards Vault"
              >
                <Trophy className="w-4 h-4 text-amber-500" />
                <span>Rewards</span>
              </button>

              {/* Day Badge / Button - Display Only */}
              {currentDay < 90 && (
                <div
                  className="px-4 py-2.5 rounded-xl text-xs font-extrabold bg-gradient-to-r from-amber-500 via-orange-500 to-amber-600 text-white shadow-md shadow-amber-500/20 min-h-[44px] flex items-center justify-center select-none cursor-default"
                >
                  <span>Complete Day {currentDay} & Unlock {currentDay + 1}</span>
                </div>
              )}
            </div>
          </div>

          {/* 90-Day Progress Bar */}
          <div className="relative mt-4 pt-3.5 border-t border-slate-100 dark:border-slate-800">
            <div className="flex items-center justify-between text-xs text-slate-500 dark:text-slate-400 mb-1.5">
              <span className="font-medium">90-Day Curriculum Track</span>
              <span className="font-mono font-bold text-amber-600 dark:text-amber-400">
                {Math.round((currentDay / 90) * 100)}% Complete
              </span>
            </div>
            <div className="w-full h-2 rounded-full bg-slate-100 dark:bg-slate-800 overflow-hidden shadow-inner">
              <div
                className="h-full bg-gradient-to-r from-amber-500 via-orange-500 to-amber-500 rounded-full transition-all duration-500"
                style={{ width: `${(currentDay / 90) * 100}%` }}
              />
            </div>
          </div>
        </div>

        {/* =========================================================================
            MONTH TRANSITION BANNER (COMPLETING 30 DAYS OR 60 DAYS)
            ========================================================================= */}
        {currentDay === 30 && (
          <div className="mb-6 p-4 sm:p-5 rounded-2xl bg-gradient-to-r from-emerald-600 to-teal-700 text-white shadow-lg flex items-center justify-between gap-4">
            <div className="flex items-center gap-3">
              <span className="text-3xl">🎉</span>
              <div>
                <h4 className="text-sm sm:text-base font-extrabold text-white">
                  Month 1 Completed! Entering Month 2: Fluency Expansion
                </h4>
                <p className="text-xs sm:text-sm text-emerald-50 font-medium mt-0.5">
                  You conquered the 30-day foundational sprint. Complex situational missions now active!
                </p>
              </div>
            </div>
          </div>
        )}

        {currentDay === 60 && (
          <div className="mb-6 p-4 sm:p-5 rounded-2xl bg-gradient-to-r from-purple-700 to-indigo-800 text-white shadow-lg flex items-center justify-between gap-4">
            <div className="flex items-center gap-3">
              <span className="text-3xl">🚀</span>
              <div>
                <h4 className="text-sm sm:text-base font-extrabold text-white">
                  Month 2 Completed! Entering Month 3: Mastery & Certification
                </h4>
                <p className="text-xs sm:text-sm text-purple-50 font-medium mt-0.5">
                  Advanced colloquial expressions, idioms, and fast-paced conversational dialogues unlocked!
                </p>
              </div>
            </div>
          </div>
        )}

        {/* =========================================================================
            MANDATORY EXAM NOTIFICATION BANNER (DAYS 7, 14, 21, 28, 30, ETC.)
            ========================================================================= */}
        {isTestDay && (
          <div className="mb-6 p-4 sm:p-5 rounded-2xl bg-amber-500/10 border-2 border-amber-500/40 text-slate-900 dark:text-slate-100 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-xl bg-amber-500 text-white flex items-center justify-center text-xl shrink-0">
                📝
              </div>
              <div>
                <span className="text-[11px] font-bold uppercase tracking-wider text-amber-600 dark:text-amber-400 block">
                  Mandatory Verification Checkpoint
                </span>
                <h4 className="text-sm sm:text-base font-bold">
                  Day {currentDay} Mastery Exam (80% Passing Score Required)
                </h4>
                <p className="text-xs text-slate-500 dark:text-slate-400">
                  {hasPassedExamToday
                    ? '✓ Passed! Your score is recorded.'
                    : 'Verify your conversational mastery to unlock the next week.'}
                </p>
              </div>
            </div>

            <button
              onClick={() => {
                playTapClick();
                onOpenExam();
              }}
              className="px-5 py-2.5 rounded-xl text-xs font-extrabold bg-amber-500 hover:bg-amber-600 text-white shadow-md active:scale-95 transition-all min-h-[44px] cursor-pointer"
            >
              <span>{hasPassedExamToday ? 'Retake Exam' : 'Start Mastery Test'}</span>
            </button>
          </div>
        )}

        {/* =========================================================================
            DYNAMIC AGE-ADAPTIVE HERO BANNER & MASCOT HEADER
            ========================================================================= */}
        {isWonderland && (
          <div className="relative mb-8 p-6 sm:p-8 rounded-3xl bg-gradient-to-r from-amber-300 via-yellow-200 to-orange-200 border-4 border-amber-400 shadow-xl shadow-amber-300/30 text-slate-900">
            <div className="flex flex-col sm:flex-row items-center justify-between gap-6">
              <div className="flex items-center gap-5 text-center sm:text-left">
                {/* 3D Mascot Avatar 🐥 Chicky */}
                <div
                  onClick={speakChickyInstruction}
                  className="w-20 h-20 sm:w-24 sm:h-24 rounded-3xl bg-white shadow-lg flex items-center justify-center text-5xl sm:text-6xl shrink-0 cursor-pointer hover:scale-105 active:scale-95 transition-transform border-4 border-amber-300"
                  title="Tap Chicky to hear instructions!"
                  role="button"
                  tabIndex={0}
                >
                  🐥
                </div>

                <div>
                  <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-white/80 font-bold text-xs text-amber-900 mb-1.5">
                    <span>Playful Wonderland Track · Day {currentDay}</span>
                    <button
                      onClick={speakChickyInstruction}
                      className="p-1 text-amber-700 hover:text-amber-900 cursor-pointer"
                      aria-label="Speak instruction"
                    >
                      <Volume2 className="w-3.5 h-3.5" />
                    </button>
                  </div>
                  <h1 className="text-3xl sm:text-4xl font-extrabold font-playful tracking-tight">
                    Let's Talk in {targetLang.label}! {targetLang.flag}
                  </h1>
                  <p className="text-sm font-semibold text-amber-950 mt-1 max-w-lg">
                    Tap any picture card below. Speak big words, collect stars, and celebrate with Chicky!
                  </p>
                </div>
              </div>

              {/* Big tactile stars badge */}
              <div className="bg-white/90 rounded-2xl px-5 py-3 border-2 border-amber-300 flex items-center gap-3 shrink-0 shadow-sm">
                <span className="text-3xl text-amber-500">★</span>
                <div>
                  <div className="text-2xl font-black font-playful tabular-nums leading-none">
                    {profile.totalStars} Stars
                  </div>
                  <div className="text-[11px] font-bold text-slate-500 mt-0.5">
                    {completedCount} of {TOPIC_SCENARIOS.length} Topics Finished
                  </div>
                </div>
              </div>
            </div>
          </div>
        )}

        {isQuest && (
          <div className="relative mb-8 p-6 sm:p-7 rounded-2xl bg-gradient-to-r from-indigo-700 via-indigo-600 to-sky-600 text-white shadow-xl shadow-indigo-600/20">
            <div className="flex flex-col sm:flex-row items-center justify-between gap-6">
              <div className="flex items-center gap-5">
                <div className="w-18 h-18 sm:w-20 sm:h-20 rounded-2xl bg-white/10 backdrop-blur-sm border-2 border-white/30 flex items-center justify-center text-4xl sm:text-5xl shrink-0 shadow-inner">
                  🦊
                </div>
                <div>
                  <div className="inline-flex items-center gap-1.5 text-xs font-bold text-sky-200 uppercase tracking-wider mb-1">
                    <Compass className="w-3.5 h-3.5" />
                    <span>Quest Explorer · Day {currentDay}</span>
                  </div>
                  <h1 className="text-2xl sm:text-3xl font-extrabold tracking-tight">
                    {targetLang.label} Expedition Missions
                  </h1>
                  <p className="text-xs sm:text-sm text-sky-100 mt-1 max-w-lg">
                    Level up your conversational skills. Complete scenario quests to earn 3-star mastery badges!
                  </p>
                </div>
              </div>

              <div className="flex items-center gap-4 bg-black/20 backdrop-blur-sm rounded-xl p-3 border border-white/10 shrink-0">
                <div className="text-center px-2">
                  <div className="text-xl font-bold font-mono text-amber-300 tabular-nums">
                    {profile.totalStars}
                  </div>
                  <div className="text-[10px] text-sky-200">Stars</div>
                </div>
                <div className="h-8 w-px bg-white/20" />
                <div className="text-center px-2">
                  <div className="text-xl font-bold font-mono text-emerald-300 tabular-nums">
                    {profile.totalXp}
                  </div>
                  <div className="text-[10px] text-sky-200">XP Points</div>
                </div>
              </div>
            </div>
          </div>
        )}

        {isAcademy && (
          <div className="mb-8 p-6 rounded-2xl bg-white border border-purple-100 shadow-sm text-slate-900">
            <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-6">
              <div>
                <div className="inline-flex items-center gap-2 text-xs font-semibold text-purple-700 bg-purple-50 px-3 py-1 rounded-md mb-2">
                  <span>🚀</span>
                  <span>Academy Lab · Day {currentDay} ({profile.level})</span>
                </div>
                <h1 className="text-2xl sm:text-3xl font-extrabold tracking-tight text-slate-900">
                  {targetLang.label} Fluency Matrix
                </h1>
                <p className="text-xs sm:text-sm font-semibold text-slate-800 mt-1 leading-relaxed">
                  Targeted foundational conversational training across 15 real-life situational categories.
                </p>
              </div>

              <div className="bg-slate-50 border border-slate-200/80 rounded-xl p-4 min-w-[200px] shrink-0">
                <div className="flex items-center justify-between text-xs font-bold mb-1.5">
                  <span className="text-slate-600">Course Mastery</span>
                  <span className="text-purple-600 tabular-nums">{totalProgress}%</span>
                </div>
                <div className="w-full h-2 rounded-full bg-slate-200 overflow-hidden">
                  <div
                    className="h-full bg-purple-600 rounded-full transition-all duration-500"
                    style={{ width: `${totalProgress}%` }}
                  />
                </div>
                <div className="flex items-center justify-between text-[11px] text-slate-400 mt-2 font-medium">
                  <span>{completedCount} Topics Finished</span>
                  <span>Day {currentDay}/90</span>
                </div>
              </div>
            </div>
          </div>
        )}

        {isTeen && (
          <div className="mb-8 p-6 sm:p-7 rounded-2xl bg-slate-900 border border-slate-800 text-slate-100 shadow-2xl">
            <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-6">
              <div>
                <div className="flex items-center gap-2 text-xs font-mono font-medium text-emerald-400 mb-2">
                  <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
                  <span>DAY {currentDay}/90 · SPRINT TRACK · {profile.level.toUpperCase()} LEVEL</span>
                </div>
                <h1 className="text-2xl sm:text-3xl font-extrabold tracking-tight font-tech text-white">
                  {targetLang.nativeName} ({targetLang.label}) Real-World Missions
                </h1>
                <p className="text-xs sm:text-sm font-semibold text-slate-100 mt-1 max-w-xl leading-relaxed">
                  Natural cadence recognition, foundational fluency drills, and travel readiness indicators.
                </p>
              </div>

              <div className="grid grid-cols-2 gap-3 shrink-0">
                <div className="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center min-w-[100px]">
                  <div className="text-lg font-bold font-mono text-emerald-400 tabular-nums">
                    {totalProgress}%
                  </div>
                  <div className="text-[10px] text-slate-400 font-medium">Mastery</div>
                </div>
                <div className="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center min-w-[100px]">
                  <div className="text-lg font-bold font-mono text-amber-400 tabular-nums">
                    {profile.totalXp}
                  </div>
                  <div className="text-[10px] text-slate-400 font-medium">Total XP</div>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* =========================================================================
            CATEGORY FILTER TABS (15 Comprehensive Categories, >=5 topics each)
            ========================================================================= */}
        <div className="mb-6 flex items-center gap-1.5 overflow-x-auto pb-2 scrollbar-none">
          <div className="flex items-center gap-1 text-xs text-slate-400 mr-2 shrink-0">
            <Filter className="w-3.5 h-3.5" />
            <span>Categories:</span>
          </div>
          {categories.map((cat) => {
            const isActive = selectedCategory === cat;
            return (
              <button
                key={cat}
                onClick={() => {
                  playTapClick();
                  setSelectedCategory(cat);
                }}
                className={`px-3.5 py-2 text-xs font-semibold rounded-xl whitespace-nowrap transition-all active:scale-95 min-h-[44px] cursor-pointer ${
                  isActive
                    ? isTeen
                      ? 'bg-emerald-500 text-slate-950 font-bold shadow-sm'
                      : isAcademy
                      ? 'bg-purple-600 text-white shadow-sm'
                      : 'bg-indigo-600 text-white shadow-sm'
                    : isTeen
                    ? 'bg-slate-900 hover:bg-slate-800 text-slate-300 border border-slate-800'
                    : 'bg-white hover:bg-slate-100 text-slate-600 border border-slate-200'
                }`}
              >
                {cat}
              </button>
            );
          })}
        </div>

        {/* =========================================================================
            TOPIC CARDS GRID (ALL 15 CATEGORIES, ALL >= 5 TOPICS)
            ========================================================================= */}
        <div
          className={`grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5 ${
            isWonderland ? 'gap-6' : ''
          }`}
        >
          {filteredTopics.map((topic) => {
            const isCompleted = profile.completedTopics.includes(topic.id);
            const topicWeekNum = Math.ceil(currentDay / 7);
            const isRemediationB = Boolean(
              profile.remediationWeeks?.[topicWeekNum] || (profile.weekSeeds?.[topicWeekNum] || 0) > 0
            );

            const curriculum = getConversationalCurriculum({
              day: currentDay,
              ageGroup: profile.ageGroup,
              level: profile.level,
              category: topic.category,
              topicId: topic.id,
              targetLanguage: profile.targetLanguage,
              motherTongue: profile.motherTongue,
              remediationVariant: isRemediationB ? 'B' : 'A',
              weekSeed: profile.weekSeeds?.[topicWeekNum] || 0,
            });

            return (
              <div
                key={topic.id}
                onClick={() => {
                  playTapClick();
                  onSelectTopic(topic.id);
                }}
                className={`group relative flex flex-col justify-between transition-all duration-200 cursor-pointer active:scale-[0.99] ${
                  isWonderland
                    ? 'p-6 rounded-3xl bg-white border-4 border-amber-300 hover:border-amber-400 shadow-md hover:shadow-xl hover:-translate-y-1'
                    : isQuest
                    ? 'p-5 rounded-2xl bg-white border-2 border-indigo-100 hover:border-indigo-400 shadow-sm hover:shadow-md hover:-translate-y-0.5'
                    : isAcademy
                    ? 'p-5 rounded-2xl bg-white border border-slate-200 hover:border-purple-300 shadow-sm hover:shadow-md'
                    : 'p-5 rounded-2xl bg-slate-900 border border-slate-800 hover:border-emerald-500/50 shadow-md'
                }`}
              >
                <div>
                  <div className="flex items-start justify-between gap-3 mb-3">
                    <div
                      className={`flex items-center justify-center shrink-0 transition-transform group-hover:scale-110 ${
                        isWonderland
                          ? 'w-16 h-16 rounded-2xl bg-amber-100 text-4xl border-2 border-amber-300'
                          : isTeen
                          ? 'w-12 h-12 rounded-xl bg-slate-800 border border-slate-700 text-2xl'
                          : 'w-12 h-12 rounded-xl bg-slate-100 text-2xl border border-slate-200'
                      }`}
                    >
                      {topic.badgeEmoji}
                    </div>

                    <div className="flex items-center gap-1.5" onClick={(e) => e.stopPropagation()}>
                      <button
                        onClick={() => {
                          playTapClick();
                          onOpenVideo(topic.youtubeVideoId, topic.videoTitle);
                        }}
                        className={`p-2 rounded-xl transition-colors min-w-[44px] min-h-[44px] flex items-center justify-center cursor-pointer ${
                          isTeen
                            ? 'hover:bg-slate-800 text-red-400'
                            : 'hover:bg-red-50 text-red-500'
                        }`}
                        title="Watch safe educational companion video"
                        aria-label={`Watch video lesson for ${topic.title}`}
                      >
                        <Tv className="w-4 h-4" />
                      </button>

                      {isCompleted && (
                        <div
                          className="flex items-center justify-center text-emerald-500 p-1"
                          title="Topic Mastered!"
                        >
                          <CheckCircle2 className="w-5 h-5 fill-emerald-100 text-emerald-600" />
                        </div>
                      )}
                    </div>
                  </div>

                  <div className="text-[11px] font-bold uppercase tracking-wider text-slate-400 mb-1">
                    {topic.category}
                  </div>

                  <h3
                    className={`font-bold tracking-tight mb-2 group-hover:text-amber-500 transition-colors ${
                      isWonderland
                        ? 'text-xl font-playful text-slate-900'
                        : isTeen
                        ? 'text-lg font-tech text-slate-100'
                        : 'text-lg text-slate-900'
                    }`}
                  >
                    {topic.title}
                  </h3>

                  <p
                    className={`text-xs leading-relaxed line-clamp-2 ${
                      isTeen ? 'text-slate-400' : 'text-slate-500'
                    }`}
                  >
                    {topic.description}
                  </p>

                  {/* 3 Progressive Day-Aware Practice Items (Speaking) */}
                  <div className="mt-3.5 pt-3 border-t border-dashed border-slate-200/80 dark:border-slate-800 space-y-1.5">
                    <div className="flex items-center justify-between text-[10px] font-bold uppercase tracking-wider text-slate-400">
                      <span className="flex items-center gap-1">
                        <span className="w-1.5 h-1.5 rounded-full bg-amber-500" />
                        <span>Day {currentDay} Target Items {isRemediationB ? '(Remediation B)' : ''}</span>
                      </span>
                      <span className="font-mono text-[10px] text-amber-600 dark:text-amber-400">
                        {curriculum.targetWordCount} words / sentence
                      </span>
                    </div>
                    <div className="space-y-1.5">
                      {curriculum.items.map((item, idx) => (
                        <div
                          key={idx}
                          className={`flex items-baseline gap-2 px-2.5 py-1.5 rounded-lg text-xs transition-colors ${
                            isTeen
                              ? 'bg-slate-800/80 text-slate-200 border border-slate-700/60'
                              : 'bg-slate-50 text-slate-800 border border-slate-200/70'
                          }`}
                        >
                          <span className="w-4 h-4 rounded-full bg-amber-500/10 text-amber-600 dark:text-amber-400 text-[10px] font-extrabold flex items-center justify-center shrink-0">
                            {idx + 1}
                          </span>
                          <div className="min-w-0 flex-1 flex flex-col">
                            <span className="font-bold truncate leading-tight" title={item.targetText}>
                              {item.targetText}
                            </span>
                            <span className="text-[11px] text-slate-500 dark:text-slate-400 truncate">
                              {item.english}
                            </span>
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>
                </div>

                <div
                  className={`mt-5 pt-3.5 border-t flex items-center justify-between ${
                    isTeen ? 'border-slate-800' : 'border-slate-100'
                  }`}
                >
                  <div className="flex items-center gap-1 text-xs">
                    <span
                      className={`font-semibold ${
                        isCompleted
                          ? 'text-emerald-500 font-bold'
                          : isTeen
                          ? 'text-slate-400'
                          : 'text-slate-500'
                      }`}
                    >
                      {isCompleted ? '✓ Completed' : '3 Sentences'}
                    </span>
                  </div>

                  <div
                    className={`inline-flex items-center gap-1 text-xs font-bold transition-transform group-hover:translate-x-1 ${
                      isWonderland
                        ? 'text-amber-600 font-playful text-sm'
                        : isTeen
                        ? 'text-emerald-400'
                        : 'text-indigo-600'
                    }`}
                  >
                    <span>Practice</span>
                    <ChevronRight className="w-4 h-4" />
                  </div>
                </div>
              </div>
            );
          })}
        </div>

        {/* Footer info & preferences quick link */}
        <div className="mt-14 text-center border-t border-slate-200 dark:border-slate-800 pt-8">
          <p className="text-xs text-slate-400">
            LinguaJunior · Day {currentDay}/90 · Level: {profile.level} · {sourceLang.label} to {targetLang.label} ({profile.learningGoal} Mode)
          </p>
          <button
            onClick={() => {
              playTapClick();
              onOpenPreferences();
            }}
            className="mt-2 text-xs font-semibold text-amber-600 dark:text-amber-400 hover:underline min-h-[44px] inline-flex items-center justify-center cursor-pointer"
          >
            Change Age, Level, Languages, or Learning Goal
          </button>
        </div>
      </div>
    </div>
  );
};
