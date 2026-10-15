/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React, { useState, useEffect, useCallback } from 'react';
import { UserProfile, CardStepQuotas } from './types';
import { TOPIC_SCENARIOS } from './data/topics';
import { Header } from './components/Header';
import { HeroLanding } from './components/HeroLanding';
import { PreferencesModal } from './components/PreferencesModal';
import { LearningHub } from './components/LearningHub';
import { PracticeRoom } from './components/PracticeRoom';
import { VideoModal } from './components/VideoModal';
import { ExamModal } from './components/ExamModal';
import { RewardsModal } from './components/RewardsModal';
import { isAudioMuted, setGlobalAudioMuted, playTapClick } from './utils/audio';

const STORAGE_KEY = 'linguajunior_user_profile_v2';

const DEFAULT_PROFILE: UserProfile = {
  ageGroup: '4-6',
  level: 'Beginner',
  motherTongue: 'en',
  targetLanguage: 'es',
  learningGoal: 'Speaking',
  completedTopics: [],
  phraseMastery: {},
  totalXp: 120,
  totalStars: 4,
  speechRate: 1.0,
  autoPlayTts: true,

  // 90-Day Progression
  currentDay: 1,
  completedDays: [],
  weekSeeds: {},

  sentenceStepQuotas: {},

  rewards: {
    dailyBadges: [1],
    categoryBadges: [],
    topicBadges: [],
    cardRewards: {
      listeningCount: 0,
      watchingCount: 0,
      practiceCount: 0,
      speakingCount: 0,
    },
  },

  examScores: {},
};

export default function App() {
  const [profile, setProfile] = useState<UserProfile>(() => {
    try {
      const saved = localStorage.getItem(STORAGE_KEY);
      if (saved) {
        return { ...DEFAULT_PROFILE, ...JSON.parse(saved) };
      }
    } catch {
      // ignore
    }
    return DEFAULT_PROFILE;
  });

  const [hasStarted, setHasStarted] = useState<boolean>(() => {
    try {
      return Boolean(localStorage.getItem(STORAGE_KEY));
    } catch {
      return false;
    }
  });

  const [activeTopicId, setActiveTopicId] = useState<string | null>(null);
  const [isPreferencesOpen, setIsPreferencesOpen] = useState(false);
  const [isRewardsOpen, setIsRewardsOpen] = useState(false);
  const [isExamOpen, setIsExamOpen] = useState(false);
  const [soundEnabled, setSoundEnabled] = useState<boolean>(() => !isAudioMuted());

  // Keep React state and browser Audio API in two-way synchronization
  useEffect(() => {
    // Initial sync
    setGlobalAudioMuted(!soundEnabled);

    const handleMuteChange = (e: Event) => {
      const customEvent = e as CustomEvent<{ muted: boolean }>;
      if (customEvent.detail && typeof customEvent.detail.muted === 'boolean') {
        setSoundEnabled(!customEvent.detail.muted);
      } else {
        setSoundEnabled(!isAudioMuted());
      }
    };

    const handleMediaVolumeChange = (event: Event) => {
      const target = event.target as HTMLMediaElement;
      if (target && typeof target.muted === 'boolean') {
        if (target.muted === soundEnabled) {
          setSoundEnabled(!target.muted);
          setGlobalAudioMuted(target.muted);
        }
      }
    };

    window.addEventListener('audiomutestatechange', handleMuteChange);

    const mediaElements = document.querySelectorAll<HTMLMediaElement>('audio, video');
    mediaElements.forEach((el) => {
      el.addEventListener('volumechange', handleMediaVolumeChange);
    });

    return () => {
      window.removeEventListener('audiomutestatechange', handleMuteChange);
      mediaElements.forEach((el) => {
        el.removeEventListener('volumechange', handleMediaVolumeChange);
      });
    };
  }, [soundEnabled]);

  const handleToggleSound = useCallback(() => {
    const nextState = !soundEnabled;
    setSoundEnabled(nextState);
    setGlobalAudioMuted(!nextState);
    if (nextState) {
      playTapClick();
    }
  }, [soundEnabled]);

  const [videoModalData, setVideoModalData] = useState<{
    videoId: string;
    title: string;
  } | null>(null);

  // Sync to localStorage
  useEffect(() => {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(profile));
    } catch {
      // ignore
    }
  }, [profile]);

  // Synchronize root dark mode class for Tailwind dark: variants
  useEffect(() => {
    if (profile.ageGroup === '13-16') {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }, [profile.ageGroup]);

  // Save Preferences: Reset progression to Day 1 whenever preferences change
  const handleSavePreferences = (updated: Partial<UserProfile>) => {
    setProfile((prev) => {
      const prevLevel = prev.level || 'Beginner';
      const isAgeChanged = updated.ageGroup !== undefined && updated.ageGroup !== prev.ageGroup;
      const isLevelChanged = updated.level !== undefined && updated.level !== prevLevel;
      const isMotherTongueChanged =
        updated.motherTongue !== undefined && updated.motherTongue !== prev.motherTongue;
      const isTargetLangChanged =
        updated.targetLanguage !== undefined && updated.targetLanguage !== prev.targetLanguage;
      const isGoalChanged =
        updated.learningGoal !== undefined && updated.learningGoal !== prev.learningGoal;

      const hasPreferenceChanged =
        isAgeChanged || isLevelChanged || isMotherTongueChanged || isTargetLangChanged || isGoalChanged;

      if (hasPreferenceChanged || updated.currentDay === 1) {
        // Reset active learning calendar day to currentDay = 1
        // Reset progress tracker display, active step indicators, unlock states, mastery badges
        const resetProfile: UserProfile = {
          ...prev,
          ...updated,
          currentDay: 1,
          completedDays: [],
          completedTopics: [],
          phraseMastery: {},
          sentenceStepQuotas: {},
          examScores: {},
          remediationWeeks: {},
          weekSeeds: {},
          rewards: {
            ...prev.rewards,
            dailyBadges: [1],
            categoryBadges: [],
            topicBadges: [],
            cardRewards: {
              listeningCount: 0,
              watchingCount: 0,
              practiceCount: 0,
              speakingCount: 0,
            },
          },
        };

        // Cache & Storage Normalization: Immediately persist reset profile
        try {
          localStorage.setItem(STORAGE_KEY, JSON.stringify(resetProfile));
        } catch {
          // ignore
        }

        return resetProfile;
      }

      const mergedProfile = {
        ...prev,
        ...updated,
      };

      try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(mergedProfile));
      } catch {
        // ignore
      }

      return mergedProfile;
    });

    setActiveTopicId(null);
    setHasStarted(true);
  };

  // Update Step Quotas (Listening 3, Watching 5, Practice 10, Speaking 3)
  const handleUpdateStepQuotas = (
    sentenceKey: string,
    step: 'listening' | 'watching' | 'practice' | 'speaking'
  ) => {
    setProfile((prev) => {
      const currentQuotas = prev.sentenceStepQuotas[sentenceKey] || {
        listening: 0,
        watching: 0,
        practice: 0,
        speaking: 0,
      };

      const updatedVal = (currentQuotas[step] || 0) + 1;
      const updatedQuotas: CardStepQuotas = {
        ...currentQuotas,
        [step]: updatedVal,
      };

      // Check if threshold achieved and grant card rewards
      const cardRewards = { ...prev.rewards.cardRewards };
      const quotaThresholds = {
        listening: 3,
        watching: 5,
        practice: 10,
        speaking: 3,
      };

      if (updatedVal === quotaThresholds[step]) {
        if (step === 'listening') cardRewards.listeningCount += 1;
        if (step === 'watching') cardRewards.watchingCount += 1;
        if (step === 'practice') cardRewards.practiceCount += 1;
        if (step === 'speaking') cardRewards.speakingCount += 1;
      }

      return {
        ...prev,
        sentenceStepQuotas: {
          ...prev.sentenceStepQuotas,
          [sentenceKey]: updatedQuotas,
        },
        rewards: {
          ...prev.rewards,
          cardRewards,
        },
      };
    });
  };

  // Progress update inside Practice Room
  const handleUpdateProgress = (
    phraseId: string,
    score: number,
    starsEarned: number,
    xpEarned: number
  ) => {
    setProfile((prev) => {
      const phraseMastery = { ...prev.phraseMastery, [phraseId]: score };
      let completedTopics = [...prev.completedTopics];
      const categoryBadges = [...prev.rewards.categoryBadges];
      const topicBadges = [...prev.rewards.topicBadges];

      if (activeTopicId && !completedTopics.includes(activeTopicId)) {
        completedTopics.push(activeTopicId);
        if (!topicBadges.includes(activeTopicId)) {
          topicBadges.push(activeTopicId);
        }

        const activeTop = TOPIC_SCENARIOS.find((t) => t.id === activeTopicId);
        if (activeTop && !categoryBadges.includes(activeTop.category)) {
          categoryBadges.push(activeTop.category);
        }
      }

      return {
        ...prev,
        phraseMastery,
        completedTopics,
        totalStars: prev.totalStars + starsEarned,
        totalXp: prev.totalXp + xpEarned,
        rewards: {
          ...prev.rewards,
          categoryBadges,
          topicBadges,
        },
      };
    });
  };

  // Day Progression Engine: [ Complete Day X & Unlock Day Y ]
  const handleCompleteDay = (dayNum: number) => {
    setProfile((prev) => {
      const completedDays = prev.completedDays.includes(dayNum)
        ? prev.completedDays
        : [...prev.completedDays, dayNum];

      const dailyBadges = prev.rewards.dailyBadges.includes(dayNum)
        ? prev.rewards.dailyBadges
        : [...prev.rewards.dailyBadges, dayNum];

      const nextDay = Math.min(90, dayNum + 1);

      return {
        ...prev,
        currentDay: nextDay,
        completedDays,
        totalXp: prev.totalXp + 50,
        rewards: {
          ...prev.rewards,
          dailyBadges,
        },
      };
    });
    // Return to existing same learning main page (Learning Hub)
    setActiveTopicId(null);
    setHasStarted(true);
  };

  // Exam Passing
  const handleExamPass = (score: number) => {
    const weekNumber = Math.ceil(profile.currentDay / 7);
    setProfile((prev) => {
      const remediationWeeks = { ...prev.remediationWeeks };
      remediationWeeks[weekNumber] = false;
      return {
        ...prev,
        examScores: {
          ...prev.examScores,
          [prev.currentDay]: score,
        },
        remediationWeeks,
        totalXp: prev.totalXp + 100,
        totalStars: prev.totalStars + 3,
      };
    });
  };

  // Exam Score recorded on failure (< 80%)
  const handleExamFail = (score: number) => {
    const weekNumber = Math.ceil(profile.currentDay / 7);
    setProfile((prev) => {
      const remediationWeeks = { ...prev.remediationWeeks };
      remediationWeeks[weekNumber] = true; // Marks week in Remediation Variant B!
      return {
        ...prev,
        examScores: {
          ...prev.examScores,
          [prev.currentDay]: score,
        },
        remediationWeeks,
      };
    });
  };

  // Exam Failing & Shuffle Regeneration: "Start Again"
  const handleExamFailRestart = () => {
    const weekNumber = Math.ceil(profile.currentDay / 7);
    setProfile((prev) => {
      const weekSeeds = { ...prev.weekSeeds };
      weekSeeds[weekNumber] = (weekSeeds[weekNumber] || 0) + 1; // Shuffles sentences for this week!
      const remediationWeeks = { ...prev.remediationWeeks };
      remediationWeeks[weekNumber] = true; // Ensures Remediation Variant B active!

      return {
        ...prev,
        weekSeeds,
        remediationWeeks,
      };
    });
  };

  const activeTopic = TOPIC_SCENARIOS.find((t) => t.id === activeTopicId) || null;

  return (
    <div
      className={`min-h-screen flex flex-col font-sans transition-colors duration-200 ${
        profile.ageGroup === '13-16' ? 'bg-slate-950 text-slate-100' : 'bg-slate-50 text-slate-900'
      }`}
    >
      {/* Universal Top Bar */}
      <Header
        profile={profile}
        onOpenPreferences={() => setIsPreferencesOpen(true)}
        onOpenRewards={() => setIsRewardsOpen(true)}
        activeTopicId={activeTopicId}
        onBackToHub={() => setActiveTopicId(null)}
        onGoHome={() => {
          setActiveTopicId(null);
          setHasStarted(false);
        }}
        soundEnabled={soundEnabled}
        onToggleSound={handleToggleSound}
      />

      <main className="flex-1">
        {!hasStarted ? (
          <HeroLanding
            onGetStarted={() => {
              setIsPreferencesOpen(true);
            }}
            isTeenMode={profile.ageGroup === '13-16'}
            currentDay={profile.currentDay}
          />
        ) : activeTopic ? (
          <PracticeRoom
            topic={activeTopic}
            profile={profile}
            onUpdateStepQuotas={handleUpdateStepQuotas}
            onUpdateProgress={handleUpdateProgress}
            onOpenVideo={(videoId, title) => setVideoModalData({ videoId, title })}
            onBack={() => setActiveTopicId(null)}
            soundEnabled={soundEnabled}
            onCompleteDay={handleCompleteDay}
          />
        ) : (
          <LearningHub
            profile={profile}
            onSelectTopic={(topicId) => setActiveTopicId(topicId)}
            onOpenVideo={(videoId, title) => setVideoModalData({ videoId, title })}
            onOpenPreferences={() => setIsPreferencesOpen(true)}
            onCompleteDay={handleCompleteDay}
            onOpenRewards={() => setIsRewardsOpen(true)}
            onOpenExam={() => setIsExamOpen(true)}
            onFailRestart={handleExamFailRestart}
            soundEnabled={soundEnabled}
          />
        )}
      </main>

      {/* Preferences Modal (Fix #1) */}
      <PreferencesModal
        isOpen={isPreferencesOpen}
        onClose={() => setIsPreferencesOpen(false)}
        currentProfile={profile}
        onSave={handleSavePreferences}
      />

      {/* Distraction-Free Embedded YouTube Video Modal */}
      {videoModalData && (
        <VideoModal
          isOpen={Boolean(videoModalData)}
          onClose={() => setVideoModalData(null)}
          videoId={videoModalData.videoId}
          title={videoModalData.title}
        />
      )}

      {/* Multi-Tier Rewards Vault Modal (Fix #5) */}
      <RewardsModal
        isOpen={isRewardsOpen}
        onClose={() => setIsRewardsOpen(false)}
        profile={profile}
      />

      {/* Mandatory Exam Modal (Fix #6) */}
      <ExamModal
        isOpen={isExamOpen}
        onClose={() => setIsExamOpen(false)}
        dayNumber={profile.currentDay}
        level={profile.level}
        targetLanguage={profile.targetLanguage}
        motherTongue={profile.motherTongue}
        onPass={handleExamPass}
        onFail={handleExamFail}
        onFailRestart={handleExamFailRestart}
        soundEnabled={soundEnabled}
      />
    </div>
  );
}
