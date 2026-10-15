import React from 'react';
import { UserProfile } from '../types';
import { SUPPORTED_LANGUAGES } from '../data/languages';
import { Sparkles, Sliders, Volume2, VolumeX, ArrowLeft, Trophy } from 'lucide-react';
import { playTapClick } from '../utils/audio';

interface HeaderProps {
  profile: UserProfile;
  onOpenPreferences: () => void;
  onOpenRewards: () => void;
  activeTopicId: string | null;
  onBackToHub: () => void;
  onGoHome?: () => void;
  soundEnabled: boolean;
  onToggleSound: () => void;
}

export const Header: React.FC<HeaderProps> = ({
  profile,
  onOpenPreferences,
  onOpenRewards,
  activeTopicId,
  onBackToHub,
  onGoHome,
  soundEnabled,
  onToggleSound,
}) => {
  const targetLang = SUPPORTED_LANGUAGES[profile.targetLanguage] || SUPPORTED_LANGUAGES.es;
  const sourceLang = SUPPORTED_LANGUAGES[profile.motherTongue] || SUPPORTED_LANGUAGES.en;

  const isTeenMode = profile.ageGroup === '13-16';

  return (
    <header
      className={`sticky top-0 z-30 transition-colors duration-200 border-b backdrop-blur-md ${
        isTeenMode
          ? 'bg-slate-950/90 border-slate-800 text-slate-100'
          : 'bg-white/90 border-slate-200/80 text-slate-900'
      }`}
    >
      <div className="max-w-6xl mx-auto px-4 sm:px-6 h-16 flex items-center justify-between gap-4">
        {/* Zone 1: Single text element wordmark */}
        <div className="flex items-center gap-3 shrink-0">
          {activeTopicId && (
            <button
              onClick={() => {
                playTapClick();
                onBackToHub();
              }}
              className={`p-2 rounded-xl transition-transform active:scale-95 flex items-center justify-center min-w-[44px] min-h-[44px] cursor-pointer ${
                isTeenMode
                  ? 'hover:bg-slate-800 text-slate-300'
                  : 'hover:bg-slate-100 text-slate-700'
              }`}
              aria-label="Back to topics hub"
            >
              <ArrowLeft className="w-5 h-5" />
            </button>
          )}

          <button
            onClick={() => {
              playTapClick();
              if (onGoHome) {
                onGoHome();
              } else if (activeTopicId) {
                onBackToHub();
              }
            }}
            className="text-left group cursor-pointer focus:outline-none"
            aria-label="LinguaJunior Home"
          >
            <span
              className={`text-xl font-bold tracking-tight ${
                profile.ageGroup === '4-6'
                  ? 'font-playful text-amber-500'
                  : profile.ageGroup === '7-9'
                  ? 'text-indigo-600'
                  : profile.ageGroup === '10-12'
                  ? 'text-purple-600'
                  : 'font-tech text-emerald-400'
              }`}
            >
              LinguaJunior
            </span>
          </button>
        </div>

        {/* Zone 2: Clean unboxed metadata / mission navigation */}
        <div className="hidden md:flex items-center gap-4 text-xs font-medium">
          <div className="flex items-center gap-1.5 opacity-80">
            <span>Day {profile.currentDay}/90</span>
            <span aria-hidden="true">·</span>
            <span>{profile.level}</span>
            <span aria-hidden="true">·</span>
            <span>{sourceLang.label} to {targetLang.label}</span>
          </div>

          <div className="flex items-center gap-3 pl-2 border-l border-slate-300 dark:border-slate-700">
            <span className="flex items-center gap-1 font-semibold text-amber-500">
              <span>★</span>
              <span className="tabular-nums">{profile.totalStars}</span>
            </span>
            <span className="flex items-center gap-1 font-semibold text-emerald-500">
              <Sparkles className="w-3.5 h-3.5" />
              <span className="tabular-nums">{profile.totalXp} XP</span>
            </span>
          </div>
        </div>

        {/* Zone 3: 1-2 primary actions */}
        <div className="flex items-center gap-2">
          {/* Rewards Vault Button */}
          <button
            onClick={() => {
              playTapClick();
              onOpenRewards();
            }}
            className={`min-w-[44px] min-h-[44px] flex items-center justify-center rounded-xl transition-colors cursor-pointer ${
              isTeenMode
                ? 'hover:bg-slate-800 text-amber-400'
                : 'hover:bg-amber-50 text-amber-600'
            }`}
            title="Rewards Vault"
            aria-label="Rewards Vault"
          >
            <Trophy className="w-4 h-4" />
          </button>

          {/* Sound Toggle */}
          <button
            onClick={onToggleSound}
            className={`min-w-[44px] min-h-[44px] flex items-center justify-center rounded-xl transition-colors cursor-pointer ${
              isTeenMode
                ? 'hover:bg-slate-800 text-slate-400 hover:text-slate-200'
                : 'hover:bg-slate-100 text-slate-500 hover:text-slate-800'
            }`}
            title={soundEnabled ? 'Mute sound effects' : 'Enable sound effects'}
            aria-label={soundEnabled ? 'Mute sound effects' : 'Enable sound effects'}
          >
            {soundEnabled ? (
              <Volume2 className="w-4 h-4 text-emerald-500" />
            ) : (
              <VolumeX className="w-4 h-4 text-slate-400" />
            )}
          </button>

          {/* Preferences Button */}
          <button
            onClick={() => {
              playTapClick();
              onOpenPreferences();
            }}
            className={`min-h-[44px] px-3.5 py-2 text-xs font-semibold rounded-xl flex items-center gap-2 transition-all active:scale-95 shadow-sm whitespace-nowrap cursor-pointer ${
              isTeenMode
                ? 'bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700'
                : 'bg-slate-900 hover:bg-slate-800 text-white'
            }`}
            aria-label="Open learning preferences"
          >
            <Sliders className="w-3.5 h-3.5" />
            <span className="hidden sm:inline">Preferences</span>
            <span className="text-base leading-none">{targetLang.flag}</span>
          </button>
        </div>
      </div>
    </header>
  );
};
