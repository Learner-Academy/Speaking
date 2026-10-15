import React, { useState, useEffect } from 'react';
import confetti from 'canvas-confetti';
import { LanguageCode, LearnerLevel, TopicCategory } from '../types';
import { SUPPORTED_LANGUAGES } from '../data/languages';
import { playSuccessChime, playTryAgainChime, playTapClick } from '../utils/audio';
import {
  Award,
  AlertTriangle,
  CheckCircle2,
  XCircle,
  HelpCircle,
  X,
  RotateCcw,
  Sparkles,
} from 'lucide-react';

interface ExamModalProps {
  isOpen: boolean;
  onClose: () => void;
  dayNumber: number;
  level: LearnerLevel;
  targetLanguage: LanguageCode;
  motherTongue: LanguageCode;
  onPass: (score: number) => void;
  onFail?: (score: number) => void;
  onFailRestart: () => void;
  soundEnabled: boolean;
}

export const ExamModal: React.FC<ExamModalProps> = ({
  isOpen,
  onClose,
  dayNumber,
  level,
  targetLanguage,
  motherTongue,
  onPass,
  onFail,
  onFailRestart,
  soundEnabled,
}) => {
  const [currentQ, setCurrentQ] = useState(0);
  const [selectedAnswers, setSelectedAnswers] = useState<number[]>([]);
  const [examFinished, setExamFinished] = useState(false);
  const [scorePercent, setScorePercent] = useState(0);

  useEffect(() => {
    if (!isOpen) return;
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        onClose();
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isOpen, onClose]);

  if (!isOpen) return null;

  const weekNumber = Math.ceil(dayNumber / 7);
  const isMonthly = dayNumber === 30 || dayNumber === 60 || dayNumber === 90;
  const isFinalCert = dayNumber === 90;

  const targetLang = SUPPORTED_LANGUAGES[targetLanguage];
  const sourceLang = SUPPORTED_LANGUAGES[motherTongue];

  // 5 contextual assessment questions calibrated to level & target language
  const questions = [
    {
      prompt: `Which polite phrase best expresses "Could I please have" in ${targetLang.label}?`,
      options: [
        targetLanguage === 'es' ? '¿Podría darme... por favor?' : targetLanguage === 'fr' ? 'Pourriez-vous me donner...' : targetLanguage === 'zh' ? '请问我可以要...' : 'Could I please have...',
        targetLanguage === 'es' ? '¡Dame eso rápido!' : targetLanguage === 'fr' ? 'Donne-moi ça vite !' : targetLanguage === 'zh' ? '快点给我那个！' : 'Give me that fast!',
        targetLanguage === 'es' ? 'No quiero nada ahora.' : targetLanguage === 'fr' ? 'Je ne veux rien.' : targetLanguage === 'zh' ? '我现在什么都不要。' : 'I don\'t want anything.',
      ],
      correct: 0,
      explanation: 'Polite inquiry chunks ensure warm, respectful communication in native contexts.',
    },
    {
      prompt: `How do you courteously say "if it is not too much trouble" in ${targetLang.label}?`,
      options: [
        targetLanguage === 'es' ? 'con cara seria.' : targetLanguage === 'fr' ? 'sans aucune politesse.' : targetLanguage === 'zh' ? '非常不礼貌。' : 'with no patience.',
        targetLanguage === 'es' ? 'si no es mucha molestia, por favor.' : targetLanguage === 'fr' ? 'si cela ne vous dérange pas.' : targetLanguage === 'zh' ? '如果不太麻烦的话，拜托了。' : 'if it is not too much trouble, please.',
        targetLanguage === 'es' ? 'porque yo lo digo.' : targetLanguage === 'fr' ? 'parce que je le dis.' : targetLanguage === 'zh' ? '因为我说了算。' : 'because I said so.',
      ],
      correct: 1,
      explanation: 'Conditional polite markers soften requests and demonstrate high cultural fluency.',
    },
    {
      prompt: `When ordering breakfast or lunch in ${targetLang.label}, which is the most natural start?`,
      options: [
        targetLanguage === 'es' ? 'Me gustaría pedir...' : targetLanguage === 'fr' ? 'J\'aimerais commander...' : targetLanguage === 'zh' ? '我想点一份...' : 'I would like to order...',
        targetLanguage === 'es' ? 'Oye tú, tráeme comida.' : targetLanguage === 'fr' ? 'Hé toi, apporte la nourriture.' : targetLanguage === 'zh' ? '喂，把吃的拿来。' : 'Hey you, bring food.',
        targetLanguage === 'es' ? 'Tengo sueño.' : targetLanguage === 'fr' ? 'J\'ai sommeil.' : targetLanguage === 'zh' ? '我困了。' : 'I am sleepy.',
      ],
      correct: 0,
      explanation: 'Expressing desires with native modal phrases shows confidence and manners.',
    },
    {
      prompt: `What is the best way to ask for train platform directions politely in ${targetLang.label}?`,
      options: [
        targetLanguage === 'es' ? '¡El tren se fue!' : targetLanguage === 'fr' ? 'Le train est parti !' : targetLanguage === 'zh' ? '火车开走了！' : 'The train is gone!',
        targetLanguage === 'es' ? '¿Me puedes mostrar las indicaciones para llegar al andén?' : targetLanguage === 'fr' ? 'Pouvez-vous me montrer les indications vers le quai ?' : targetLanguage === 'zh' ? '你能给我看一下前往火车月台的路线吗？' : 'Can you show me directions to the platform?',
        targetLanguage === 'es' ? 'No sé viajar.' : targetLanguage === 'fr' ? 'Je ne sais pas voyager.' : targetLanguage === 'zh' ? '我不会旅行。' : 'I cannot travel.',
      ],
      correct: 1,
      explanation: 'Navigation queries in public spaces prevent confusion and delays.',
    },
    {
      prompt: `To thank someone for their patient guidance, which expression is warmest?`,
      options: [
        targetLanguage === 'es' ? 'con mucho cariño y una gran sonrisa, ¡muchas gracias!' : targetLanguage === 'fr' ? 'avec toute mon affection et un grand sourire !' : targetLanguage === 'zh' ? '带着满满的感激和微笑，非常感谢！' : 'with warm appreciation and a cheerful smile, thank you!',
        targetLanguage === 'es' ? 'Bueno, adiós.' : targetLanguage === 'fr' ? 'Bon, au revoir.' : targetLanguage === 'zh' ? '好吧，再见。' : 'Well, bye.',
        targetLanguage === 'es' ? 'No importa.' : targetLanguage === 'fr' ? 'Peu importe.' : targetLanguage === 'zh' ? '无所谓。' : 'Whatever.',
      ],
      correct: 0,
      explanation: 'A grateful conclusion builds lasting bonds and leaves an exceptional impression.',
    },
  ];

  const handleSelectOption = (optIdx: number) => {
    playTapClick();
    const updated = [...selectedAnswers];
    updated[currentQ] = optIdx;
    setSelectedAnswers(updated);
  };

  const handleNextQuestion = () => {
    playTapClick();
    if (currentQ < questions.length - 1) {
      setCurrentQ((prev) => prev + 1);
    } else {
      // Calculate final score
      let correctCount = 0;
      questions.forEach((q, idx) => {
        if (selectedAnswers[idx] === q.correct) correctCount++;
      });
      const pct = Math.round((correctCount / questions.length) * 100);
      setScorePercent(pct);
      setExamFinished(true);

      if (pct >= 80) {
        if (soundEnabled) playSuccessChime();
        try {
          confetti({
            particleCount: 80,
            spread: 80,
            origin: { y: 0.6 },
          });
        } catch {
          // ignore
        }
        onPass(pct);
      } else {
        if (soundEnabled) playTryAgainChime();
        onFail?.(pct);
      }
    }
  };

  const isCurrentAnswered = selectedAnswers[currentQ] !== undefined;

  return (
    <div
      role="dialog"
      aria-modal="true"
      className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-6 md:p-8 backdrop-blur-md bg-slate-950/60 animate-fade-in overflow-y-auto"
    >
      <div
        className="relative w-full max-w-lg max-h-[calc(100dvh-1.5rem)] sm:max-h-[calc(100dvh-4rem)] flex flex-col bg-white dark:bg-slate-900 rounded-3xl shadow-2xl border border-slate-200 dark:border-slate-800 p-4 sm:p-8 my-auto text-left transition-all overflow-y-auto pb-safe"
        onClick={(e) => e.stopPropagation()}
      >
        {!examFinished ? (
          <div>
            {/* Header */}
            <div className="flex items-center justify-between pb-3 sm:pb-4 border-b border-slate-200 dark:border-slate-800 mb-4 sm:mb-5">
              <div>
                <span className="text-xs font-bold uppercase tracking-wider text-amber-500 block">
                  {isFinalCert
                    ? 'Final Certification Exam'
                    : isMonthly
                    ? `Month ${dayNumber / 30} Milestone Exam`
                    : `Week ${weekNumber} Mastery Test`}
                </span>
                <h3 className="text-lg sm:text-xl font-extrabold text-slate-900 dark:text-slate-100 text-balance">
                  Day {dayNumber} Verification (80% Required)
                </h3>
              </div>
              <button
                onClick={onClose}
                className="p-2 text-slate-400 hover:text-slate-600 rounded-full min-w-[44px] min-h-[44px] flex items-center justify-center cursor-pointer"
                aria-label="Close test"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            {/* Progress indicator */}
            <div className="flex items-center justify-between text-xs text-slate-400 mb-2">
              <span>Question {currentQ + 1} of {questions.length}</span>
              <span className="font-mono">80% passing threshold</span>
            </div>
            <div className="w-full h-1.5 rounded-full bg-slate-200 dark:bg-slate-800 mb-6 overflow-hidden">
              <div
                className="h-full bg-amber-500 transition-all duration-300"
                style={{ width: `${((currentQ + 1) / questions.length) * 100}%` }}
              />
            </div>

            {/* Question Prompt */}
            <h4 className="text-base sm:text-lg font-bold text-slate-900 dark:text-slate-100 mb-4 leading-relaxed">
              {questions[currentQ].prompt}
            </h4>

            {/* Options */}
            <div className="space-y-3 mb-6">
              {questions[currentQ].options.map((opt, optIdx) => {
                const isSelected = selectedAnswers[currentQ] === optIdx;
                return (
                  <button
                    key={optIdx}
                    onClick={() => handleSelectOption(optIdx)}
                    className={`w-full text-left p-3.5 rounded-2xl border text-sm font-medium transition-all cursor-pointer min-h-[50px] flex items-center justify-between ${
                      isSelected
                        ? 'border-amber-500 bg-amber-50 dark:bg-amber-950/40 text-amber-950 dark:text-amber-100 font-bold shadow-sm'
                        : 'border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800/60 text-slate-700 dark:text-slate-200 hover:border-amber-300'
                    }`}
                  >
                    <span>{opt}</span>
                    <span
                      className={`w-5 h-5 rounded-full border flex items-center justify-center text-xs shrink-0 ml-2 ${
                        isSelected ? 'border-amber-600 bg-amber-500 text-white' : 'border-slate-300'
                      }`}
                    >
                      {isSelected ? '✓' : ''}
                    </span>
                  </button>
                );
              })}
            </div>

            {/* Action */}
            <button
              onClick={handleNextQuestion}
              disabled={!isCurrentAnswered}
              className={`w-full h-12 rounded-2xl font-extrabold text-sm flex items-center justify-center shadow-md transition-all ${
                isCurrentAnswered
                  ? 'bg-amber-500 hover:bg-amber-600 text-white cursor-pointer active:scale-98 shadow-amber-500/20'
                  : 'bg-slate-200 dark:bg-slate-800 text-slate-400 cursor-not-allowed'
              }`}
            >
              {currentQ < questions.length - 1 ? 'Next Question' : 'Submit Exam'}
            </button>
          </div>
        ) : (
          /* RESULT SCREEN */
          <div className="text-center py-4">
            {scorePercent >= 80 ? (
              <div>
                <div className="w-16 h-16 rounded-full bg-emerald-100 text-emerald-600 mx-auto flex items-center justify-center mb-4">
                  <CheckCircle2 className="w-9 h-9 stroke-[2.5]" />
                </div>
                <h3 className="text-2xl font-black text-slate-900 dark:text-slate-100 mb-1">
                  Mastery Verified! ({scorePercent}%)
                </h3>
                <p className="text-xs text-slate-500 dark:text-slate-400 max-w-sm mx-auto mb-6">
                  Outstanding performance! You surpassed the 80% passing threshold. Forward progress unlocked!
                </p>

                <button
                  onClick={onClose}
                  className="w-full h-12 rounded-2xl bg-emerald-600 hover:bg-emerald-700 text-white font-extrabold text-sm shadow-lg shadow-emerald-600/25 active:scale-98 cursor-pointer"
                >
                  Continue Learning Journey
                </button>
              </div>
            ) : (
              /* WARNING MODAL: < 80% STRICT RESTART LOGIC */
              <div>
                <div className="w-16 h-16 rounded-full bg-red-100 text-red-600 mx-auto flex items-center justify-center mb-4">
                  <AlertTriangle className="w-9 h-9 stroke-[2.5]" />
                </div>
                <h3 className="text-2xl font-black text-slate-900 dark:text-slate-100 mb-1">
                  Score: {scorePercent}% (80% Needed)
                </h3>
                <div className="p-3.5 rounded-2xl bg-amber-50 dark:bg-amber-950/40 border border-amber-300 text-amber-900 dark:text-amber-200 text-xs font-medium text-left my-4 leading-relaxed">
                  <strong>Strict Mastery Rule:</strong> Forward progress is locked until 80% mastery is achieved. You must restart Week {weekNumber} to reinforce fundamentals.
                  <br />
                  <span className="opacity-90 block mt-1">
                    * Sentences for Week {weekNumber} will be shuffled/regenerated with new variations to prevent rote memorization upon retry!
                  </span>
                </div>

                <button
                  onClick={() => {
                    playTapClick();
                    onFailRestart();
                    onClose();
                  }}
                  className="w-full h-12 rounded-2xl bg-amber-500 hover:bg-amber-600 text-white font-extrabold text-sm flex items-center justify-center gap-2 shadow-lg shadow-amber-500/25 active:scale-98 cursor-pointer"
                >
                  <RotateCcw className="w-4 h-4" />
                  <span>Start Again</span>
                </button>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
};
