import React, { useState, useEffect } from 'react';
import { UserProfile, TopicCategory } from '../types';
import { CATEGORY_REWARDS, CARD_STEP_REWARDS } from '../data/rewards';
import { TOPIC_SCENARIOS } from '../data/topics';
import { Award, Trophy, Star, X, CheckCircle2, Lock, Flame } from 'lucide-react';
import { playTapClick } from '../utils/audio';

interface RewardsModalProps {
  isOpen: boolean;
  onClose: () => void;
  profile: UserProfile;
}

export const RewardsModal: React.FC<RewardsModalProps> = ({
  isOpen,
  onClose,
  profile,
}) => {
  const [activeTab, setActiveTab] = useState<'card' | 'category' | 'daily' | 'topics'>('card');

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

  const categories = Object.values(CATEGORY_REWARDS);

  return (
    <div
      role="dialog"
      aria-modal="true"
      className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-6 md:p-8 backdrop-blur-md bg-slate-950/60 animate-fade-in overflow-y-auto"
      onClick={onClose}
    >
      <div
        className="relative w-full max-w-2xl max-h-[calc(100dvh-1.5rem)] sm:max-h-[calc(100dvh-4rem)] flex flex-col bg-white dark:bg-slate-900 rounded-3xl shadow-2xl border border-slate-200 dark:border-slate-800 my-auto text-left transition-all overflow-hidden"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header & Tabs (Pinned at top of modal card) */}
        <div className="p-4 sm:p-8 pb-0 shrink-0">
          <div className="flex items-center justify-between pb-3 sm:pb-4 border-b border-slate-200 dark:border-slate-800 mb-3 sm:mb-5">
            <div className="flex items-center gap-2.5">
              <div className="w-10 h-10 rounded-xl bg-amber-100 dark:bg-amber-950 text-amber-600 dark:text-amber-300 flex items-center justify-center text-xl shrink-0">
                🏆
              </div>
              <div>
                <h3 className="text-lg sm:text-xl font-extrabold text-slate-900 dark:text-slate-100 text-balance">
                  Multi-Tier Rewards Vault
                </h3>
                <p className="text-xs text-slate-500 dark:text-slate-400 text-pretty">
                  Track your Card-Level, Topic, Category, and Daily Achievements
                </p>
              </div>
            </div>
            <button
              onClick={() => {
                playTapClick();
                onClose();
              }}
              className="p-2 text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 rounded-full min-w-[44px] min-h-[44px] flex items-center justify-center cursor-pointer"
              aria-label="Close rewards vault"
            >
              <X className="w-5 h-5" />
            </button>
          </div>

          {/* Segmented Control Tabs */}
          <div className="flex items-center gap-1.5 p-1 bg-slate-100 dark:bg-slate-800 rounded-xl mb-3 sm:mb-4 overflow-x-auto scrollbar-none">
            <button
              onClick={() => {
                playTapClick();
                setActiveTab('card');
              }}
              className={`flex-1 min-w-[90px] py-2 text-xs font-bold rounded-lg transition-colors whitespace-nowrap min-h-[40px] flex items-center justify-center ${
                activeTab === 'card'
                  ? 'bg-white dark:bg-slate-700 text-slate-900 dark:text-slate-100 shadow-sm'
                  : 'text-slate-600 dark:text-slate-400 hover:text-slate-900'
              }`}
            >
              Card Badges
            </button>
            <button
              onClick={() => {
                playTapClick();
                setActiveTab('category');
              }}
              className={`flex-1 min-w-[90px] py-2 text-xs font-bold rounded-lg transition-colors whitespace-nowrap min-h-[40px] flex items-center justify-center ${
                activeTab === 'category'
                  ? 'bg-white dark:bg-slate-700 text-slate-900 dark:text-slate-100 shadow-sm'
                  : 'text-slate-600 dark:text-slate-400 hover:text-slate-900'
              }`}
            >
              15 Categories
            </button>
            <button
              onClick={() => {
                playTapClick();
                setActiveTab('daily');
              }}
              className={`flex-1 min-w-[90px] py-2 text-xs font-bold rounded-lg transition-colors whitespace-nowrap min-h-[40px] flex items-center justify-center ${
                activeTab === 'daily'
                  ? 'bg-white dark:bg-slate-700 text-slate-900 dark:text-slate-100 shadow-sm'
                  : 'text-slate-600 dark:text-slate-400 hover:text-slate-900'
              }`}
            >
              Daily Streak
            </button>
            <button
              onClick={() => {
                playTapClick();
                setActiveTab('topics');
              }}
              className={`flex-1 min-w-[90px] py-2 text-xs font-bold rounded-lg transition-colors whitespace-nowrap min-h-[40px] flex items-center justify-center ${
                activeTab === 'topics'
                  ? 'bg-white dark:bg-slate-700 text-slate-900 dark:text-slate-100 shadow-sm'
                  : 'text-slate-600 dark:text-slate-400 hover:text-slate-900'
              }`}
            >
              Topics (11)
            </button>
          </div>
        </div>

        {/* Scrollable Tab Content Body */}
        <div className="px-4 sm:px-8 py-3 overflow-y-auto flex-1 pb-safe">
          {/* Tab 1: 4 Card-Level Rewards */}
        {activeTab === 'card' && (
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 max-h-[360px] overflow-y-auto pr-1">
            {Object.values(CARD_STEP_REWARDS).map((rew) => {
              const count =
                profile.rewards.cardRewards[
                  `${rew.id}Count` as keyof typeof profile.rewards.cardRewards
                ] || 0;
              const isUnlocked = count > 0;

              return (
                <div
                  key={rew.id}
                  className={`p-4 rounded-2xl border transition-all ${
                    isUnlocked
                      ? 'bg-amber-50/60 dark:bg-amber-950/20 border-amber-300 dark:border-amber-800'
                      : 'bg-slate-50 dark:bg-slate-800/40 border-slate-200 dark:border-slate-800 opacity-70'
                  }`}
                >
                  <div className="flex items-center justify-between mb-2">
                    <span className="text-3xl">{rew.badgeEmoji}</span>
                    <span
                      className={`text-xs font-mono font-bold px-2 py-0.5 rounded-full ${
                        isUnlocked
                          ? 'bg-amber-500 text-white'
                          : 'bg-slate-200 dark:bg-slate-700 text-slate-500'
                      }`}
                    >
                      {count} Earned
                    </span>
                  </div>
                  <h4 className="text-sm font-bold text-slate-900 dark:text-slate-100">{rew.name}</h4>
                  <p className="text-xs text-slate-500 dark:text-slate-400 mt-1">{rew.desc}</p>
                </div>
              );
            })}
          </div>
        )}

        {/* Tab 2: 15 Category Rewards */}
        {activeTab === 'category' && (
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 max-h-[360px] overflow-y-auto pr-1">
            {categories.map((cat) => {
              const isUnlocked = profile.rewards.categoryBadges.includes(cat.category);
              return (
                <div
                  key={cat.category}
                  className={`p-3.5 rounded-2xl border text-center transition-all ${
                    isUnlocked
                      ? 'bg-emerald-50 dark:bg-emerald-950/30 border-emerald-300 dark:border-emerald-800 shadow-sm'
                      : 'bg-slate-50 dark:bg-slate-800/40 border-slate-200 dark:border-slate-800 opacity-60'
                  }`}
                >
                  <span className="text-3xl block mb-1">{cat.badgeEmoji}</span>
                  <h5 className="text-xs font-bold text-slate-900 dark:text-slate-100 truncate">
                    {cat.name}
                  </h5>
                  <span className="text-[10px] text-slate-400 block truncate mt-0.5">
                    {cat.category}
                  </span>
                  <div className="mt-2 text-[10px] font-bold">
                    {isUnlocked ? (
                      <span className="text-emerald-600 dark:text-emerald-400 flex items-center justify-center gap-1">
                        <CheckCircle2 className="w-3 h-3" /> Unlocked
                      </span>
                    ) : (
                      <span className="text-slate-400 flex items-center justify-center gap-1">
                        <Lock className="w-3 h-3" /> Locked
                      </span>
                    )}
                  </div>
                </div>
              );
            })}
          </div>
        )}

        {/* Tab 3: Daily Streak Badges */}
        {activeTab === 'daily' && (
          <div className="text-center py-4">
            <div className="inline-flex items-center gap-2 px-4 py-2 rounded-2xl bg-orange-100 dark:bg-orange-950 text-orange-600 dark:text-orange-400 font-bold text-sm mb-4">
              <Flame className="w-5 h-5 fill-orange-500" />
              <span>Current Progress: Day {profile.currentDay} of 90</span>
            </div>

            <div className="grid grid-cols-6 sm:grid-cols-10 gap-2 max-h-[260px] overflow-y-auto p-2">
              {Array.from({ length: 90 }, (_, i) => i + 1).map((d) => {
                const isCompleted = profile.completedDays.includes(d);
                const isCurrent = profile.currentDay === d;

                return (
                  <div
                    key={d}
                    className={`h-10 rounded-xl flex items-center justify-center font-mono text-xs font-bold transition-all ${
                      isCompleted
                        ? 'bg-amber-500 text-white shadow-sm'
                        : isCurrent
                        ? 'bg-amber-100 dark:bg-amber-950 text-amber-700 dark:text-amber-300 border-2 border-amber-400 animate-pulse'
                        : 'bg-slate-100 dark:bg-slate-800 text-slate-400'
                    }`}
                  >
                    D{d}
                  </div>
                );
              })}
            </div>
          </div>
        )}

        {/* Tab 4: Topic Trophies */}
        {activeTab === 'topics' && (
          <div className="grid grid-cols-2 sm:grid-cols-3 gap-2.5 max-h-[360px] overflow-y-auto pr-1">
            {TOPIC_SCENARIOS.slice(0, 30).map((top) => {
              const isDone = profile.completedTopics.includes(top.id);
              return (
                <div
                  key={top.id}
                  className={`p-3 rounded-xl border flex items-center gap-2.5 ${
                    isDone
                      ? 'border-amber-300 bg-amber-50/60 dark:bg-amber-950/20'
                      : 'border-slate-200 dark:border-slate-800 opacity-60'
                  }`}
                >
                  <span className="text-xl">{top.badgeEmoji}</span>
                  <div className="text-left overflow-hidden">
                    <span className="text-xs font-bold text-slate-800 dark:text-slate-200 truncate block">
                      {top.title}
                    </span>
                    <span className="text-[10px] text-amber-600 dark:text-amber-400 font-semibold block">
                      {top.rewardName}
                    </span>
                  </div>
                </div>
              );
            })}
          </div>
        )}
        </div>

        {/* Footer (Pinned at bottom of modal card) */}
        <div className="p-6 sm:p-8 pt-4 border-t border-slate-200 dark:border-slate-800 shrink-0 bg-white dark:bg-slate-900 flex items-center justify-between text-xs text-slate-500">
          <span>Earn XP, stars, and step quotas to unlock full vault tiers.</span>
          <button
            onClick={onClose}
            className="font-bold text-amber-600 dark:text-amber-400 hover:underline min-h-[44px] flex items-center cursor-pointer"
          >
            Close Vault
          </button>
        </div>
      </div>
    </div>
  );
};
