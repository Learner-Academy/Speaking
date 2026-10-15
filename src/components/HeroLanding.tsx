import React, { useState, useEffect } from 'react';
import { Mic, Sparkles, BookOpen, PenTool, CheckCircle2, Globe2, ShieldCheck } from 'lucide-react';
import { playTapClick } from '../utils/audio';
import { ROTATING_HERO_LANGUAGES } from '../data/languages';

interface HeroLandingProps {
  onGetStarted: () => void;
  isTeenMode?: boolean;
  currentDay?: number;
}

export const HeroLanding: React.FC<HeroLandingProps> = ({
  onGetStarted,
  isTeenMode,
  currentDay = 1,
}) => {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [prevIndex, setPrevIndex] = useState<number | null>(null);

  useEffect(() => {
    const intervalId = window.setInterval(() => {
      setCurrentIndex((current) => {
        setPrevIndex(current);
        return (current + 1) % ROTATING_HERO_LANGUAGES.length;
      });
    }, 1000);

    return () => {
      window.clearInterval(intervalId);
    };
  }, []);

  const currentLanguage = ROTATING_HERO_LANGUAGES[currentIndex] || ROTATING_HERO_LANGUAGES[0];
  const ctaAriaLabel = `Start Speaking ${currentLanguage} Right Now`;

  return (
    <div className="relative overflow-hidden py-12 md:py-20 px-4 sm:px-6">
      {/* Subtle organic gradient blurs */}
      <div
        className="absolute top-10 left-1/2 -translate-x-1/2 w-[300px] sm:w-[600px] h-[220px] sm:h-[350px] bg-gradient-to-tr from-amber-200/40 via-sky-200/40 to-emerald-200/40 rounded-full blur-3xl -z-10 pointer-events-none"
        aria-hidden="true"
      />

      <div className="max-w-4xl mx-auto text-center">
        {/* Anti-slop clean kicker */}
        <div className="inline-flex items-center gap-2 text-xs font-bold tracking-wide text-indigo-900 dark:text-indigo-200 bg-indigo-50 dark:bg-indigo-950/80 px-3.5 py-1.5 rounded-full mb-4 sm:mb-6 border border-indigo-200 dark:border-indigo-700 shadow-xs">
          <Sparkles className="w-3.5 h-3.5 text-amber-500" />
          <span>Interactive Speech & Pronunciation Missions</span>
        </div>

        {/* Required Headline */}
        <h1 className="text-3xl sm:text-5xl md:text-6xl font-extrabold tracking-tight text-slate-950 dark:text-white mb-4 sm:mb-6 text-balance leading-tight">
          What would you like to learn?
        </h1>

        {/* Sub-headline with maximum contrast and highlighted foundational fluency focus */}
        <p className={`text-base sm:text-xl max-w-2xl mx-auto mb-8 sm:mb-10 leading-relaxed font-semibold transition-colors text-pretty ${
          isTeenMode ? 'text-slate-100' : 'text-slate-900'
        }`}>
          Choose your preferences to build{' '}
          <span className={`font-bold underline decoration-amber-500 decoration-2 underline-offset-4 ${
            isTeenMode ? 'text-amber-400' : 'text-amber-700'
          }`}>
            foundational
          </span>{' '}
          speaking fluency with interactive daily conversational missions.
        </p>

        {/* Prominent CTA Button with smooth bounce & hover */}
        <div className="flex flex-col sm:flex-row items-center justify-center gap-4 mb-12 sm:mb-16">
          <button
            onClick={() => {
              playTapClick();
              onGetStarted();
            }}
            className="group relative inline-flex items-center justify-center px-4 sm:px-8 py-3.5 sm:py-4 text-xs xs:text-sm sm:text-base md:text-lg font-bold text-white bg-gradient-to-r from-amber-500 via-orange-500 to-amber-600 rounded-2xl shadow-xl shadow-amber-500/25 hover:shadow-amber-500/40 hover:-translate-y-0.5 active:translate-y-0 active:scale-95 transition-all min-h-[52px] sm:min-h-[56px] w-full xs:w-auto min-w-0 sm:min-w-[360px] cursor-pointer select-none"
            aria-label={ctaAriaLabel}
          >
            <span className="inline-flex items-baseline justify-center whitespace-nowrap gap-x-1 sm:gap-x-2 tracking-wide">
              <span>Start Speaking</span>
              <span
                className="inline-grid grid-cols-1 grid-rows-1 items-baseline justify-center overflow-hidden h-[1.35em] text-[1.1em] font-extrabold text-amber-200 align-baseline whitespace-nowrap select-none"
                aria-hidden="true"
              >
                {ROTATING_HERO_LANGUAGES.map((lang, idx) => {
                  const isCurrent = idx === currentIndex;
                  const isPrev = idx === prevIndex;
                  return (
                    <span
                      key={lang}
                      className={`col-start-1 row-start-1 inline-flex items-baseline justify-center transition-all duration-300 ease-out ${
                        isCurrent
                          ? 'opacity-100 translate-y-0'
                          : isPrev
                          ? 'opacity-0 -translate-y-2 pointer-events-none'
                          : 'opacity-0 translate-y-2 pointer-events-none'
                      }`}
                    >
                      {lang}
                    </span>
                  );
                })}
              </span>
              <span>Right Now</span>
            </span>
          </button>
        </div>

        {/* Feature Highlights Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-5 text-left max-w-3xl mx-auto">
          <div className="p-5 rounded-2xl bg-white/90 dark:bg-slate-900/90 backdrop-blur-sm border border-slate-200/80 dark:border-slate-800 shadow-sm hover:shadow-md transition-shadow">
            <div className="w-10 h-10 rounded-xl bg-amber-100 dark:bg-amber-950/60 text-amber-700 dark:text-amber-400 flex items-center justify-center mb-3">
              <Mic className="w-5 h-5" />
            </div>
            <h3 className="text-sm font-bold text-slate-900 dark:text-slate-100 mb-1">Live Pronunciation Scoring</h3>
            <p className="text-xs text-slate-600 dark:text-slate-300 leading-relaxed font-normal">
              Integrated speech recognition matches real voice against native phrases with joyful feedback.
            </p>
          </div>

          <div className="p-5 rounded-2xl bg-white/90 dark:bg-slate-900/90 backdrop-blur-sm border border-slate-200/80 dark:border-slate-800 shadow-sm hover:shadow-md transition-shadow">
            <div className="w-10 h-10 rounded-xl bg-sky-100 dark:bg-sky-950/60 text-sky-700 dark:text-sky-400 flex items-center justify-center mb-3">
              <Globe2 className="w-5 h-5" />
            </div>
            <h3 className="text-sm font-bold text-slate-900 dark:text-slate-100 mb-1">11 Real-Life Scenarios</h3>
            <p className="text-xs text-slate-600 dark:text-slate-300 leading-relaxed font-normal">
              From breakfast and airport gates to doctor clinics and playgrounds, speak in real contexts.
            </p>
          </div>

          <div className="p-5 rounded-2xl bg-white/90 dark:bg-slate-900/90 backdrop-blur-sm border border-slate-200/80 dark:border-slate-800 shadow-sm hover:shadow-md transition-shadow">
            <div className="w-10 h-10 rounded-xl bg-emerald-100 dark:bg-emerald-950/60 text-emerald-700 dark:text-emerald-400 flex items-center justify-center mb-3">
              <ShieldCheck className="w-5 h-5" />
            </div>
            <h3 className="text-sm font-bold text-slate-900 dark:text-slate-100 mb-1">Adaptive 4 Age Tiers</h3>
            <p className="text-xs text-slate-600 dark:text-slate-300 leading-relaxed font-normal">
              Playful wonderland for 4-6 up to high-density fluency sprints for teens with zero childish clutter.
            </p>
          </div>
        </div>

        {/* Languages and proof line */}
        <div className="mt-12 pt-8 border-t border-slate-200/60 dark:border-slate-800 flex flex-wrap items-center justify-center gap-6 text-xs text-slate-700 dark:text-slate-300 font-medium">
          <div className="flex items-center gap-2">
            <CheckCircle2 className="w-4 h-4 text-emerald-500" />
            <span>Spanish · English · Urdu · Hindi · Arabic · French</span>
          </div>
          <span className="hidden sm:inline opacity-60" aria-hidden="true">·</span>
          <span>Zero account setup required</span>
          <span className="hidden sm:inline opacity-60" aria-hidden="true">·</span>
          <span>100% Client-Side Audio & Privacy Safe</span>
        </div>
      </div>
    </div>
  );
};
