import React, { useState, useRef, useEffect } from 'react';
import { AgeGroup, LanguageCode, UserProfilePro } from '../types';
import { SUPPORTED_LANGUAGES, LANGUAGE_LIST } from '../data/languages';
import {
  ChevronDown,
  Volume2,
  VolumeX,
  Sparkles,
  ArrowLeft,
  Calendar,
  Globe,
  Award,
} from 'lucide-react';
import { playTapClick } from '../utils/audio';

interface HeaderProProps {
  profile: UserProfilePro;
  onChangeAge: (age: AgeGroup) => void;
  onChangeTargetLang: (lang: LanguageCode) => void;
  onChangeMotherTongue: (lang: LanguageCode) => void;
  onOpenDiploma: () => void;
  onOpenExamHub: () => void;
  activeScenarioId: string | null;
  onBackToHub: () => void;
  soundEnabled: boolean;
  onToggleSound: () => void;
}

export const HeaderPro: React.FC<HeaderProProps> = ({
  profile,
  onChangeAge,
  onChangeTargetLang,
  onChangeMotherTongue,
  onOpenDiploma,
  onOpenExamHub,
  activeScenarioId,
  onBackToHub,
  soundEnabled,
  onToggleSound,
}) => {
  const [isAgeMenuOpen, setIsAgeMenuOpen] = useState(false);
  const [isTargetMenuOpen, setIsTargetMenuOpen] = useState(false);
  const [isSourceMenuOpen, setIsSourceMenuOpen] = useState(false);

  const ageMenuRef = useRef<HTMLDivElement>(null);
  const targetMenuRef = useRef<HTMLDivElement>(null);
  const sourceMenuRef = useRef<HTMLDivElement>(null);

  // Close menus when clicking outside
  useEffect(() => {
    function handleClickOutside(event: MouseEvent) {
      if (ageMenuRef.current && !ageMenuRef.current.contains(event.target as Node)) {
        setIsAgeMenuOpen(false);
      }
      if (targetMenuRef.current && !targetMenuRef.current.contains(event.target as Node)) {
        setIsTargetMenuOpen(false);
      }
      if (sourceMenuRef.current && !sourceMenuRef.current.contains(event.target as Node)) {
        setIsSourceMenuOpen(false);
      }
    }
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  const targetLang = SUPPORTED_LANGUAGES[profile.targetLanguage];
  const sourceLang = SUPPORTED_LANGUAGES[profile.motherTongue];

  const ageOptions: { value: AgeGroup; label: string; sub: string }[] = [
    { value: '4-6', label: '4-6', sub: 'Wonderland' },
    { value: '7-9', label: '7-9', sub: 'Quest Explorer' },
    { value: '10-12', label: '10-12', sub: 'Academy Lab' },
    { value: '13-16', label: '13-16', sub: 'Fluency Sprint' },
  ];

  const isTeen = profile.ageGroup === '13-16';

  return (
    <header className="sticky top-0 z-40 px-3 sm:px-6 pt-3 pb-2 transition-all">
      {/* Floating frosted glass control bar (FIX #1) */}
      <div className="max-w-6xl mx-auto flex items-center justify-between gap-2 sm:gap-4 bg-white/80 dark:bg-slate-900/80 backdrop-blur-xl border border-white/20 dark:border-slate-800/80 shadow-lg rounded-2xl px-3 sm:px-4 py-2 text-slate-900 dark:text-slate-100">
        
        {/* Left: Brand or Back Button */}
        <div className="flex items-center gap-2 sm:gap-3 shrink-0">
          {activeScenarioId ? (
            <button
              onClick={() => {
                playTapClick();
                onBackToHub();
              }}
              className="p-2 rounded-xl bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 transition-transform active:scale-95 flex items-center justify-center min-w-[40px] min-h-[40px]"
              aria-label="Back to scenarios"
            >
              <ArrowLeft className="w-4 h-4" />
            </button>
          ) : null}

          <button
            onClick={() => {
              playTapClick();
              if (activeScenarioId) onBackToHub();
            }}
            className="text-left group cursor-pointer focus:outline-none flex items-center gap-1.5"
          >
            <span className="text-base sm:text-lg font-black tracking-tight bg-gradient-to-r from-amber-500 via-orange-500 to-amber-600 bg-clip-text text-transparent">
              LinguaJunior
            </span>
            <span className="px-1.5 py-0.5 text-[10px] font-black uppercase tracking-wider rounded-md bg-amber-500 text-white shadow-sm">
              PRO
            </span>
          </button>

          {/* Active Day Indicator Pill */}
          <div className="hidden md:flex items-center gap-1.5 px-2.5 py-1 rounded-xl bg-slate-100 dark:bg-slate-800/90 text-xs font-bold text-slate-600 dark:text-slate-300">
            <Calendar className="w-3.5 h-3.5 text-amber-500" />
            <span>Day {profile.activeDay}/90</span>
          </div>
        </div>

        {/* Center: Quick XP / Diplomas / Stats */}
        <div className="hidden lg:flex items-center gap-3 text-xs font-semibold">
          <div className="flex items-center gap-1 text-amber-500">
            <span>★</span>
            <span className="tabular-nums font-mono">{profile.totalStars}</span>
          </div>
          <div className="flex items-center gap-1 text-emerald-500">
            <Sparkles className="w-3.5 h-3.5" />
            <span className="tabular-nums font-mono">{profile.totalXp} XP</span>
          </div>
          <button
            onClick={() => {
              playTapClick();
              onOpenDiploma();
            }}
            className="flex items-center gap-1 px-2 py-0.5 rounded-lg bg-amber-50 dark:bg-amber-950/40 text-amber-700 dark:text-amber-300 border border-amber-200 dark:border-amber-800/60 hover:scale-105 transition-transform"
          >
            <Award className="w-3.5 h-3.5 text-amber-600" />
            <span>Diploma</span>
          </button>
        </div>

        {/* Right: TOP-RIGHT STATUS HUB WITH TWO GLASSMORPHIC PILL SELECTORS (FIX #1) */}
        <div className="flex items-center gap-1.5 sm:gap-2">
          
          {/* 1. [Age: 4-6 ▾] Interactive Pill Selector */}
          <div className="relative" ref={ageMenuRef}>
            <button
              onClick={() => {
                playTapClick();
                setIsAgeMenuOpen(!isAgeMenuOpen);
                setIsTargetMenuOpen(false);
                setIsSourceMenuOpen(false);
              }}
              className="flex items-center gap-1.5 px-2.5 sm:px-3 py-1.5 rounded-xl bg-slate-100/90 dark:bg-slate-800/90 hover:bg-slate-200/80 dark:hover:bg-slate-700/80 border border-slate-200/80 dark:border-slate-700/80 text-xs font-bold transition-all min-h-[40px] cursor-pointer"
              aria-label="Change learner age group"
            >
              <span className="opacity-70 text-[11px] hidden xs:inline">Age:</span>
              <span className="font-extrabold">{profile.ageGroup}</span>
              <ChevronDown className={`w-3.5 h-3.5 text-slate-400 transition-transform ${isAgeMenuOpen ? 'rotate-180' : ''}`} />
            </button>

            {isAgeMenuOpen && (
              <div className="absolute right-0 mt-2 w-48 bg-white dark:bg-slate-900 rounded-2xl shadow-2xl border border-slate-200 dark:border-slate-800 p-2 z-50 animate-fade-in text-left">
                <div className="px-2 py-1 text-[10px] font-bold uppercase tracking-wider text-slate-400">
                  Select Age Track
                </div>
                {ageOptions.map((opt) => (
                  <button
                    key={opt.value}
                    onClick={() => {
                      playTapClick();
                      onChangeAge(opt.value);
                      setIsAgeMenuOpen(false);
                    }}
                    className={`w-full flex items-center justify-between px-3 py-2 rounded-xl text-xs font-bold transition-colors cursor-pointer ${
                      profile.ageGroup === opt.value
                        ? 'bg-amber-500 text-white'
                        : 'hover:bg-slate-100 dark:hover:bg-slate-800 text-slate-700 dark:text-slate-300'
                    }`}
                  >
                    <span>{opt.label}</span>
                    <span className="text-[10px] opacity-75 font-normal">{opt.sub}</span>
                  </button>
                ))}
              </div>
            )}
          </div>

          {/* 2. [Target: Spanish ▾] Interactive Pill Selector */}
          <div className="relative" ref={targetMenuRef}>
            <button
              onClick={() => {
                playTapClick();
                setIsTargetMenuOpen(!isTargetMenuOpen);
                setIsAgeMenuOpen(false);
                setIsSourceMenuOpen(false);
              }}
              className="flex items-center gap-1.5 px-2.5 sm:px-3 py-1.5 rounded-xl bg-amber-50 dark:bg-amber-950/40 hover:bg-amber-100/80 dark:hover:bg-amber-900/60 border border-amber-200 dark:border-amber-800/80 text-xs font-bold text-amber-900 dark:text-amber-200 transition-all min-h-[40px] cursor-pointer"
              aria-label="Change target learning language"
            >
              <span className="text-base leading-none">{targetLang.flag}</span>
              <span className="font-extrabold max-w-[70px] truncate">{targetLang.label}</span>
              <ChevronDown className={`w-3.5 h-3.5 text-amber-600 dark:text-amber-400 transition-transform ${isTargetMenuOpen ? 'rotate-180' : ''}`} />
            </button>

            {isTargetMenuOpen && (
              <div className="absolute right-0 mt-2 w-52 bg-white dark:bg-slate-900 rounded-2xl shadow-2xl border border-slate-200 dark:border-slate-800 p-2 z-50 animate-fade-in text-left max-h-[172px] overflow-y-auto overscroll-contain">
                <div className="px-2 py-1 text-[10px] font-bold uppercase tracking-wider text-slate-400 sticky top-0 bg-white dark:bg-slate-900 z-10">
                  Target Language
                </div>
                {LANGUAGE_LIST.map((lang) => (
                  <button
                    key={lang.code}
                    onClick={() => {
                      playTapClick();
                      onChangeTargetLang(lang.code);
                      setIsTargetMenuOpen(false);
                    }}
                    className={`w-full flex items-center justify-between px-3 py-2 rounded-xl text-xs font-bold transition-colors cursor-pointer ${
                      profile.targetLanguage === lang.code
                        ? 'bg-amber-500 text-white'
                        : 'hover:bg-slate-100 dark:hover:bg-slate-800 text-slate-700 dark:text-slate-300'
                    }`}
                  >
                    <span className="flex items-center gap-2">
                      <span className="text-base">{lang.flag}</span>
                      <span>{lang.label}</span>
                    </span>
                    <span className="text-[10px] opacity-75 font-mono">{lang.nativeName}</span>
                  </button>
                ))}
              </div>
            )}
          </div>

          {/* Mother Tongue Quick Trigger */}
          <div className="relative" ref={sourceMenuRef}>
            <button
              onClick={() => {
                playTapClick();
                setIsSourceMenuOpen(!isSourceMenuOpen);
                setIsAgeMenuOpen(false);
                setIsTargetMenuOpen(false);
              }}
              className="p-2 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700 transition-colors min-w-[40px] min-h-[40px] flex items-center justify-center text-xs"
              title={`Mother tongue: ${sourceLang.label}`}
              aria-label="Change native mother tongue"
            >
              <Globe className="w-4 h-4" />
            </button>

            {isSourceMenuOpen && (
              <div className="absolute right-0 mt-2 w-48 bg-white dark:bg-slate-900 rounded-2xl shadow-2xl border border-slate-200 dark:border-slate-800 p-2 z-50 animate-fade-in text-left max-h-[172px] overflow-y-auto overscroll-contain">
                <div className="px-2 py-1 text-[10px] font-bold uppercase tracking-wider text-slate-400 sticky top-0 bg-white dark:bg-slate-900 z-10">
                  Mother Tongue (Source)
                </div>
                {LANGUAGE_LIST.map((lang) => (
                  <button
                    key={lang.code}
                    onClick={() => {
                      playTapClick();
                      onChangeMotherTongue(lang.code);
                      setIsSourceMenuOpen(false);
                    }}
                    className={`w-full flex items-center justify-between px-3 py-2 rounded-xl text-xs font-bold transition-colors cursor-pointer ${
                      profile.motherTongue === lang.code
                        ? 'bg-slate-900 text-white dark:bg-slate-100 dark:text-slate-900'
                        : 'hover:bg-slate-100 dark:hover:bg-slate-800 text-slate-700 dark:text-slate-300'
                    }`}
                  >
                    <span>{lang.flag} {lang.label}</span>
                  </button>
                ))}
              </div>
            )}
          </div>

          {/* Mute/Unmute Sound Button */}
          <button
            onClick={onToggleSound}
            className="p-2 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700 transition-colors min-w-[40px] min-h-[40px] flex items-center justify-center cursor-pointer"
            title={soundEnabled ? 'Mute sound effects' : 'Enable sound effects'}
            aria-label={soundEnabled ? 'Mute sound effects' : 'Enable sound effects'}
          >
            {soundEnabled ? (
              <Volume2 className="w-4 h-4 text-emerald-500" />
            ) : (
              <VolumeX className="w-4 h-4 text-slate-400" />
            )}
          </button>
        </div>
      </div>
    </header>
  );
};
