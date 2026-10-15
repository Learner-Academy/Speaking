import React from 'react';
import { UserProfilePro } from '../types';
import {
  Calendar,
  Lock,
  CheckCircle2,
  Sparkles,
  Trophy,
  ChevronRight,
  ShieldAlert,
} from 'lucide-react';
import { playTapClick } from '../utils/audio';

interface TimelineDaySelectorProps {
  profile: UserProfilePro;
  onSelectDay: (day: number) => void;
  onUnlockNextDay: () => void;
  onOpenExam: (day: number) => void;
}

export const TimelineDaySelector: React.FC<TimelineDaySelectorProps> = ({
  profile,
  onSelectDay,
  onUnlockNextDay,
  onOpenExam,
}) => {
  const activeDay = profile.activeDay;
  const unlockedDays = profile.unlockedDays;

  // Determine current month phase
  const currentMonth = activeDay <= 30 ? 1 : activeDay <= 60 ? 2 : 3;
  const monthPhaseTitle =
    currentMonth === 1
      ? 'Month 1 (Days 1–30): Survival Chunks & Core Needs'
      : currentMonth === 2
      ? 'Month 2 (Days 31–60): Daily Social Dialogues & Turn-Taking'
      : 'Month 3 (Days 61–90): Fluent Native Scenarios & Cadence';

  // Check if current active day is completed
  const isCurrentDayCompleted = profile.completedDays.includes(activeDay);
  const isNextDayLocked = unlockedDays <= activeDay && activeDay < 90;

  // Check if today is a test day
  const isWeeklyExamDay = activeDay % 7 === 0 && activeDay % 30 !== 0;
  const isMonthlyExamDay = activeDay === 30 || activeDay === 60 || activeDay === 90;
  const hasPassedCurrentExam = Boolean(profile.passedExams[`exam-day-${activeDay}`]);

  // Generate day pills around activeDay (window of 10 days for quick thumb access)
  const startDay = Math.max(1, activeDay - 4);
  const endDay = Math.min(90, startDay + 9);
  const dayRange = [];
  for (let d = startDay; d <= endDay; d++) {
    dayRange.push(d);
  }

  const isTeen = profile.ageGroup === '13-16';

  return (
    <div
      className={`mb-6 p-4 sm:p-6 rounded-3xl border transition-all ${
        isTeen
          ? 'bg-slate-900/90 border-slate-800 text-slate-100 shadow-xl'
          : currentMonth === 1
          ? 'bg-gradient-to-r from-amber-50 to-orange-50 border-amber-200 shadow-sm'
          : currentMonth === 2
          ? 'bg-gradient-to-r from-sky-50 to-indigo-50 border-indigo-200 shadow-sm'
          : 'bg-gradient-to-r from-purple-50 to-slate-50 border-purple-200 shadow-sm'
      }`}
    >
      {/* Month Phase Banner */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 mb-4">
        <div>
          <div className="inline-flex items-center gap-1.5 text-xs font-bold uppercase tracking-wider text-amber-600 dark:text-amber-400 mb-1">
            <Sparkles className="w-3.5 h-3.5" />
            <span>90-Day Mastery Curriculum</span>
          </div>
          <h2 className="text-base sm:text-lg font-black tracking-tight">{monthPhaseTitle}</h2>
        </div>

        {/* Month 1 to Month 2 / Month 3 Milestone Badge */}
        <div className="flex items-center gap-2 self-start sm:self-auto text-xs font-bold">
          <span className="px-3 py-1 rounded-xl bg-white dark:bg-slate-800 shadow-sm border border-slate-200 dark:border-slate-700">
            {profile.completedDays.length} / 90 Days Completed
          </span>
        </div>
      </div>

      {/* Horizontal Day Carousel */}
      <div className="flex items-center gap-2 overflow-x-auto pb-2 scrollbar-none">
        {dayRange.map((d) => {
          const isUnlocked = d <= unlockedDays;
          const isSelected = d === activeDay;
          const isCompleted = profile.completedDays.includes(d);
          const isExam = d % 7 === 0 || d === 30 || d === 60 || d === 90;

          return (
            <button
              key={d}
              disabled={!isUnlocked}
              onClick={() => {
                playTapClick();
                onSelectDay(d);
              }}
              className={`relative flex flex-col items-center justify-center p-2.5 rounded-2xl min-w-[58px] min-h-[58px] text-center border transition-all cursor-pointer ${
                isSelected
                  ? 'bg-amber-500 border-amber-600 text-white font-black shadow-md shadow-amber-500/25 scale-105'
                  : isCompleted
                  ? 'bg-emerald-50 dark:bg-emerald-950/40 border-emerald-300 dark:border-emerald-700 text-emerald-800 dark:text-emerald-300 font-bold'
                  : isUnlocked
                  ? 'bg-white dark:bg-slate-800 border-slate-200 dark:border-slate-700 text-slate-800 dark:text-slate-200 font-bold hover:border-amber-300'
                  : 'bg-slate-100 dark:bg-slate-800/40 border-slate-200 dark:border-slate-800 text-slate-400 cursor-not-allowed opacity-60'
              }`}
            >
              <span className="text-[10px] font-bold uppercase tracking-tight">
                {isExam ? 'Exam' : `Day`}
              </span>
              <span className="text-base font-extrabold leading-none mt-0.5 font-mono">
                {d}
              </span>
              <div className="mt-1">
                {!isUnlocked ? (
                  <Lock className="w-3 h-3 text-slate-400" />
                ) : isCompleted ? (
                  <CheckCircle2 className="w-3 h-3 text-emerald-500" />
                ) : (
                  <span className="w-1.5 h-1.5 rounded-full bg-amber-400" />
                )}
              </div>
            </button>
          );
        })}
      </div>

      {/* Daily Progression Gate Action Bar */}
      <div className="mt-4 pt-3 border-t border-slate-200/80 dark:border-slate-800 flex flex-wrap items-center justify-between gap-3">
        <div className="text-xs text-slate-500 dark:text-slate-400 flex items-center gap-1.5">
          <span>Active Practice: <strong>Day {activeDay}</strong></span>
          <span>·</span>
          <span>{isCurrentDayCompleted ? '✓ Completed' : 'In Progress'}</span>
        </div>

        <div className="flex items-center gap-2">
          {/* If it's an Exam Day (Day 7, 14, 21, 28, 30, 60, 90) */}
          {(isWeeklyExamDay || isMonthlyExamDay) && (
            <button
              onClick={() => {
                playTapClick();
                onOpenExam(activeDay);
              }}
              className="flex items-center gap-1.5 px-4 py-2 rounded-xl text-xs font-black bg-indigo-600 hover:bg-indigo-700 text-white shadow-md shadow-indigo-600/20 active:scale-95 transition-all min-h-[44px] cursor-pointer"
            >
              <Trophy className="w-4 h-4 text-amber-300" />
              <span>
                {hasPassedCurrentExam ? 'Retake Mastery Exam' : 'Start Mandatory Exam (80% Pass)'}
              </span>
            </button>
          )}

          {/* Day Progression Completion Button - Static / Unclickable */}
          {isNextDayLocked && (
            <button
              type="button"
              disabled
              className="flex items-center justify-center px-4 py-2 rounded-xl text-xs font-black bg-amber-500/80 text-white shadow-xs min-h-[44px] cursor-default select-none pointer-events-none opacity-90"
              aria-disabled="true"
            >
              <span>Complete Day {activeDay} & Unlock {activeDay + 1}</span>
            </button>
          )}
        </div>
      </div>
    </div>
  );
};
