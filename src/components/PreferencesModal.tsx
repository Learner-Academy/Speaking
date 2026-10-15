import React, { useState, useRef, useEffect } from 'react';
import { AgeGroup, LanguageCode, LearnerLevel, LearningGoal, UserProfile } from '../types';
import { LANGUAGE_LIST } from '../data/languages';
import { Mic, BookOpen, PenTool, X, Check, Sparkles, ChevronDown } from 'lucide-react';
import { playTapClick, playSuccessChime } from '../utils/audio';

interface PreferencesModalProps {
  isOpen: boolean;
  onClose: () => void;
  currentProfile: UserProfile;
  onSave: (updated: Partial<UserProfile>) => void;
}

interface DropdownOption<T> {
  value: T;
  label: string;
  badge?: string;
  desc?: string;
  flag?: string;
  nativeName?: string;
}

interface CustomSelectProps<T> {
  id: string;
  value: T;
  options: DropdownOption<T>[];
  isOpen: boolean;
  onToggle: (e: React.MouseEvent) => void;
  onSelect: (val: T) => void;
  direction?: 'down' | 'auto';
}

function CustomSelect<T extends string>({
  id,
  value,
  options,
  isOpen,
  onToggle,
  onSelect,
  direction = 'auto',
}: CustomSelectProps<T>) {
  const triggerRef = useRef<HTMLButtonElement>(null);
  const [openUpward, setOpenUpward] = useState(false);

  useEffect(() => {
    if (isOpen && triggerRef.current) {
      if (direction === 'down') {
        setOpenUpward(false);
      } else {
        const rect = triggerRef.current.getBoundingClientRect();
        const spaceBelow = window.innerHeight - rect.bottom;
        setOpenUpward(spaceBelow < 200 && rect.top > 200);
      }
    }
  }, [isOpen, direction]);

  const selectedOption = options.find((opt) => opt.value === value) || options[0];

  return (
    <div className="relative w-full">
      <button
        ref={triggerRef}
        id={id}
        type="button"
        aria-haspopup="listbox"
        aria-expanded={isOpen}
        onClick={onToggle}
        className={`w-full h-12 px-4 rounded-2xl border flex items-center justify-between text-left transition-all duration-150 min-h-[48px] cursor-pointer ${
          isOpen
            ? 'bg-amber-500/10 dark:bg-amber-500/15 border-amber-500 ring-2 ring-amber-500/20 shadow-sm'
            : 'bg-slate-50 dark:bg-slate-800/80 border-slate-200 dark:border-slate-700/80 hover:border-slate-300 dark:hover:border-slate-600 hover:bg-slate-100/60 dark:hover:bg-slate-800'
        }`}
      >
        <div className="flex items-center gap-2.5 min-w-0 pr-2">
          {selectedOption?.flag && (
            <span className="text-xl leading-none shrink-0" aria-hidden="true">
              {selectedOption.flag}
            </span>
          )}
          <span className="text-sm font-semibold text-slate-900 dark:text-slate-100 truncate">
            {selectedOption?.label}
            {selectedOption?.nativeName && (
              <span className="ml-1.5 opacity-60 font-normal">
                ({selectedOption.nativeName})
              </span>
            )}
          </span>
          {selectedOption?.badge && (
            <span className="hidden sm:inline-flex text-xs text-slate-400 dark:text-slate-400 font-normal shrink-0">
              · {selectedOption.badge}
            </span>
          )}
        </div>
        <ChevronDown
          className={`w-4 h-4 text-slate-400 shrink-0 transition-transform duration-200 ease-out ${
            isOpen ? 'rotate-180 text-amber-500' : ''
          }`}
        />
      </button>

      {isOpen && (
        <div
          role="listbox"
          aria-labelledby={`${id}-label`}
          onClick={(e) => e.stopPropagation()}
          className={`absolute left-0 right-0 z-50 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl shadow-2xl shadow-slate-950/25 p-1.5 max-h-[172px] overflow-y-auto overscroll-contain animate-in fade-in-0 zoom-in-95 duration-150 ease-out space-y-1 ${
            openUpward ? 'bottom-full mb-2 origin-bottom' : 'top-full mt-2 origin-top'
          }`}
        >
          {options.map((opt) => {
            const isSelected = opt.value === value;
            return (
              <button
                key={String(opt.value)}
                type="button"
                role="option"
                aria-selected={isSelected}
                onClick={() => {
                  onSelect(opt.value);
                }}
                className={`w-full flex items-center justify-between px-3.5 py-2.5 rounded-xl text-left transition-all duration-150 min-h-[44px] cursor-pointer group ${
                  isSelected
                    ? 'bg-amber-500/10 dark:bg-amber-500/20 text-amber-900 dark:text-amber-200 font-bold border border-amber-300/80 dark:border-amber-700/60'
                    : 'text-slate-700 dark:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800/80 border border-transparent'
                }`}
              >
                <div className="flex items-center gap-2.5 min-w-0 pr-2">
                  {opt.flag && (
                    <span className="text-xl leading-none shrink-0" aria-hidden="true">
                      {opt.flag}
                    </span>
                  )}
                  <div className="min-w-0">
                    <div className="flex items-center gap-1.5 flex-nowrap whitespace-nowrap">
                      <span className="text-sm font-semibold truncate text-slate-900 dark:text-slate-100">
                        {opt.label}
                      </span>
                      {opt.nativeName && (
                        <span className="text-xs text-slate-400 dark:text-slate-400 font-normal truncate">
                          ({opt.nativeName})
                        </span>
                      )}
                      {opt.badge && (
                        <span className="text-xs text-slate-400 dark:text-slate-400 font-normal">
                          · {opt.badge}
                        </span>
                      )}
                    </div>
                    {opt.desc && (
                      <p className="text-xs text-slate-500 dark:text-slate-400 font-normal line-clamp-1 mt-0.5">
                        {opt.desc}
                      </p>
                    )}
                  </div>
                </div>
                {isSelected && (
                  <Check className="w-4 h-4 text-amber-500 shrink-0 stroke-[2.5]" />
                )}
              </button>
            );
          })}
        </div>
      )}
    </div>
  );
}

export const PreferencesModal: React.FC<PreferencesModalProps> = ({
  isOpen,
  onClose,
  currentProfile,
  onSave,
}) => {
  const [selectedAge, setSelectedAge] = useState<AgeGroup>(currentProfile.ageGroup);
  const [selectedLevel, setSelectedLevel] = useState<LearnerLevel>(currentProfile.level || 'Beginner');
  const [selectedSource, setSelectedSource] = useState<LanguageCode>(currentProfile.motherTongue);
  const [selectedTarget, setSelectedTarget] = useState<LanguageCode>(currentProfile.targetLanguage);
  const [selectedGoal, setSelectedGoal] = useState<LearningGoal>(currentProfile.learningGoal);
  const [openDropdownId, setOpenDropdownId] = useState<string | null>(null);

  // Synchronize internal state whenever modal opens or currentProfile changes
  useEffect(() => {
    if (isOpen) {
      setSelectedAge(currentProfile.ageGroup);
      setSelectedLevel(currentProfile.level || 'Beginner');
      setSelectedSource(currentProfile.motherTongue);
      setSelectedTarget(currentProfile.targetLanguage);
      setSelectedGoal(currentProfile.learningGoal);
      setOpenDropdownId(null);
    }
  }, [isOpen, currentProfile]);

  // Close dropdown on outside click or escape
  useEffect(() => {
    const handleClickOutside = () => {
      setOpenDropdownId(null);
    };
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        if (openDropdownId) {
          setOpenDropdownId(null);
        } else {
          onClose();
        }
      }
    };
    document.addEventListener('click', handleClickOutside);
    document.addEventListener('keydown', handleKeyDown);
    return () => {
      document.removeEventListener('click', handleClickOutside);
      document.removeEventListener('keydown', handleKeyDown);
    };
  }, [openDropdownId, onClose]);

  if (!isOpen) return null;

  const ageOptions: DropdownOption<AgeGroup>[] = [
    {
      value: '4-6',
      label: 'Ages 4–6',
      badge: 'Wonderland',
      desc: 'Chicky 🐥 · Visual phonics & playful stories',
    },
    {
      value: '7-9',
      label: 'Ages 7–9',
      badge: 'Quest Explorer',
      desc: 'Rusty 🦊 · Everyday adventures & quests',
    },
    {
      value: '10-12',
      label: 'Ages 10–12',
      badge: 'Academy Lab',
      desc: 'Rocket 🚀 · Interactive dialogues & vocabulary',
    },
    {
      value: '13-16',
      label: 'Ages 13–16',
      badge: 'Fluency Sprint',
      desc: 'Sleek Dark · Situational problems & native cadence',
    },
  ];

  const levelOptions: DropdownOption<LearnerLevel>[] = [
    {
      value: 'Beginner',
      label: 'Beginner Level',
      badge: 'Sprint 1',
      desc: 'Foundational vocabulary, core greetings, basic words',
    },
    {
      value: 'Intermediate',
      label: 'Intermediate Level',
      badge: 'Sprint 2',
      desc: 'Situational dialogues, ordering food, asking directions',
    },
    {
      value: 'Advanced',
      label: 'Advanced Level',
      badge: 'Sprint 3',
      desc: 'Idiomatic fluency, natural cadence, native nuance',
    },
  ];

  const languageOptions: DropdownOption<LanguageCode>[] = LANGUAGE_LIST.map((lang) => ({
    value: lang.code,
    label: lang.label,
    nativeName: lang.nativeName,
    flag: lang.flag,
  }));

  const goalOptions: { value: LearningGoal; icon: typeof Mic; title: string; desc: string }[] = [
    { value: 'Speaking', icon: Mic, title: 'Speaking', desc: 'Voice recognition & pronunciation' },
    { value: 'Reading', icon: BookOpen, title: 'Reading', desc: 'Phonetics & comprehension' },
    { value: 'Writing', icon: PenTool, title: 'Writing', desc: 'Sentence tile building' },
  ];

  const handleToggle = (id: string, e: React.MouseEvent) => {
    e.stopPropagation();
    playTapClick();
    setOpenDropdownId((prev) => (prev === id ? null : id));
  };

  const handleSelect = (field: 'age' | 'level' | 'source' | 'target', val: any) => {
    playTapClick();
    if (field === 'age') setSelectedAge(val);
    else if (field === 'level') setSelectedLevel(val);
    else if (field === 'source') setSelectedSource(val);
    else if (field === 'target') setSelectedTarget(val);
    setOpenDropdownId(null);
  };

  const handleContinue = () => {
    playSuccessChime();
    const prevLevel = currentProfile.level || 'Beginner';
    const isAgeChanged = selectedAge !== currentProfile.ageGroup;
    const isLevelChanged = selectedLevel !== prevLevel;
    const isSourceChanged = selectedSource !== currentProfile.motherTongue;
    const isTargetChanged = selectedTarget !== currentProfile.targetLanguage;
    const isGoalChanged = selectedGoal !== currentProfile.learningGoal;

    const hasPreferenceChanged =
      isAgeChanged || isLevelChanged || isSourceChanged || isTargetChanged || isGoalChanged;

    onSave({
      ageGroup: selectedAge,
      level: selectedLevel,
      motherTongue: selectedSource,
      targetLanguage: selectedTarget,
      learningGoal: selectedGoal,
      ...(hasPreferenceChanged
        ? {
            currentDay: 1,
            completedDays: [],
            completedTopics: [],
            phraseMastery: {},
            sentenceStepQuotas: {},
            examScores: {},
            remediationWeeks: {},
            weekSeeds: {},
            rewards: {
              ...currentProfile.rewards,
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
          }
        : {}),
    });
    onClose();
  };

  return (
    <div
      role="dialog"
      aria-modal="true"
      aria-labelledby="preferences-modal-title"
      className="fixed inset-0 z-50 flex items-center justify-center p-4 sm:p-6 md:p-8 backdrop-blur-md bg-slate-950/50 animate-fade-in overflow-y-auto"
      onClick={onClose}
    >
      <div
        className="relative w-full max-w-xl max-h-[calc(100dvh-1.5rem)] sm:max-h-[calc(100dvh-4rem)] flex flex-col bg-white dark:bg-slate-900 rounded-3xl shadow-2xl border border-slate-200 dark:border-slate-800 my-auto text-left transition-all duration-200 overflow-hidden"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Close Button */}
        <button
          onClick={() => {
            playTapClick();
            onClose();
          }}
          className="absolute top-4 right-4 sm:top-5 sm:right-5 z-20 p-2 rounded-full hover:bg-slate-100 dark:hover:bg-slate-800 text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 transition-colors min-w-[44px] min-h-[44px] flex items-center justify-center cursor-pointer"
          aria-label="Close preferences modal"
        >
          <X className="w-5 h-5" />
        </button>

        {/* Modal Header (Fixed at top of modal card) */}
        <div className="p-5 sm:p-8 pb-2 sm:pb-3 shrink-0 pr-12 sm:pr-14">
          <div className="inline-flex items-center gap-1.5 text-xs font-semibold text-amber-600 dark:text-amber-400 mb-1.5 sm:mb-2">
            <Sparkles className="w-4 h-4" />
            <span>Learner Setup</span>
          </div>
          <h2
            id="preferences-modal-title"
            className="text-xl sm:text-3xl font-extrabold text-slate-900 dark:text-slate-100 tracking-tight text-balance"
          >
            Personalize Your Mission
          </h2>
          <p className="text-xs sm:text-sm text-slate-500 dark:text-slate-400 mt-1 text-pretty">
            Choose your learning track. Interface, dialogues, and audio adapt automatically.
          </p>
        </div>

        {/* Scrollable Form Content */}
        <div className="px-5 sm:px-8 py-3 sm:py-4 overflow-y-auto space-y-4 sm:space-y-5 flex-1">
          {/* 1. Age Group: Custom styled dropdown (Always opens downward) */}
          <div className={`relative ${openDropdownId === 'age' ? 'z-30' : 'z-10'}`}>
            <label
              id="age-group-label"
              htmlFor="age-group-select"
              className="block text-xs font-bold uppercase tracking-wider text-slate-700 dark:text-slate-300 mb-2"
            >
              1. Age Group
            </label>
            <CustomSelect
              id="age-group-select"
              value={selectedAge}
              options={ageOptions}
              isOpen={openDropdownId === 'age'}
              onToggle={(e) => handleToggle('age', e)}
              onSelect={(val) => handleSelect('age', val)}
              direction="down"
            />
          </div>

          {/* 2. Your Level: Custom styled dropdown (Always opens downward) */}
          <div className={`relative ${openDropdownId === 'level' ? 'z-30' : 'z-10'}`}>
            <label
              id="learner-level-label"
              htmlFor="learner-level-select"
              className="block text-xs font-bold uppercase tracking-wider text-slate-700 dark:text-slate-300 mb-2"
            >
              2. Your Level
            </label>
            <CustomSelect
              id="learner-level-select"
              value={selectedLevel}
              options={levelOptions}
              isOpen={openDropdownId === 'level'}
              onToggle={(e) => handleToggle('level', e)}
              onSelect={(val) => handleSelect('level', val)}
              direction="down"
            />
          </div>

          {/* 3. Mother Tongue (Opens up or down according to screen space) */}
          <div className={`relative ${openDropdownId === 'source' ? 'z-30' : 'z-10'}`}>
            <label
              id="mother-tongue-label"
              htmlFor="mother-tongue-select"
              className="block text-xs font-bold uppercase tracking-wider text-slate-700 dark:text-slate-300 mb-2"
            >
              3. Mother Tongue
            </label>
            <CustomSelect
              id="mother-tongue-select"
              value={selectedSource}
              options={languageOptions}
              isOpen={openDropdownId === 'source'}
              onToggle={(e) => handleToggle('source', e)}
              onSelect={(val) => handleSelect('source', val)}
              direction="auto"
            />
          </div>

          {/* 4. Target Language (Opens up or down according to screen space) */}
          <div className={`relative ${openDropdownId === 'target' ? 'z-30' : 'z-10'}`}>
            <label
              id="target-language-label"
              htmlFor="target-language-select"
              className="block text-xs font-bold uppercase tracking-wider text-slate-700 dark:text-slate-300 mb-2"
            >
              4. Target Language
            </label>
            <CustomSelect
              id="target-language-select"
              value={selectedTarget}
              options={languageOptions}
              isOpen={openDropdownId === 'target'}
              onToggle={(e) => handleToggle('target', e)}
              onSelect={(val) => handleSelect('target', val)}
              direction="auto"
            />
          </div>

          {/* 5. Learning Goal (Existing 3 boxes: KEEP AS IS) */}
          <div className="relative z-0">
            <label className="block text-xs font-bold uppercase tracking-wider text-slate-700 dark:text-slate-300 mb-2.5">
              5. Learning Goal
            </label>
            <div className="grid grid-cols-3 gap-2.5">
              {goalOptions.map((goal) => {
                const IconComponent = goal.icon;
                const isActive = selectedGoal === goal.value;
                return (
                  <button
                    key={goal.value}
                    type="button"
                    onClick={() => {
                      playTapClick();
                      setSelectedGoal(goal.value);
                    }}
                    className={`flex flex-col items-center justify-center p-3 rounded-2xl border text-center transition-all min-h-[74px] cursor-pointer ${
                      isActive
                        ? 'bg-amber-50 dark:bg-amber-950/40 border-amber-500 text-amber-700 dark:text-amber-300 font-bold shadow-sm'
                        : 'bg-slate-50 dark:bg-slate-800/60 border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-400 hover:border-slate-300'
                    }`}
                  >
                    <IconComponent className={`w-5 h-5 mb-1.5 ${isActive ? 'text-amber-600 dark:text-amber-400' : 'text-slate-400'}`} />
                    <span className="text-xs font-bold">{goal.title}</span>
                  </button>
                );
              })}
            </div>
          </div>
        </div>

        {/* Action Button: [ Continue ] (Pinned at bottom of modal card) */}
        <div className="p-5 sm:p-8 pt-3 sm:pt-4 border-t border-slate-200 dark:border-slate-800 shrink-0 bg-white dark:bg-slate-900 z-10 pb-safe">
          <button
            onClick={handleContinue}
            className="w-full h-12 sm:h-13 rounded-2xl bg-amber-500 hover:bg-amber-600 active:scale-[0.99] text-white font-extrabold text-base flex items-center justify-center gap-2 shadow-lg shadow-amber-500/25 transition-all cursor-pointer"
          >
            <span>[ Continue ]</span>
            <Check className="w-5 h-5 stroke-[2.5]" />
          </button>
        </div>
      </div>
    </div>
  );
};
