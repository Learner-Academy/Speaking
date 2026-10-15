import { useMemo } from 'react';
import {
  ConversationalCurriculumResult,
  ConversationalSentenceItem,
  AgeGroup,
  LearnerLevel,
  LanguageCode,
  CardPracticeData,
  CardPracticeItem,
} from '../types';
import {
  getCardPracticeData,
  getConversationalCurriculum,
  GetConversationalCurriculumOptions,
  getTargetWordCount,
  getTierForDay,
  tokenizeSentence,
} from '../data/conversationalCurriculum';

export {
  getCardPracticeData,
  getConversationalCurriculum,
  getTargetWordCount,
  getTierForDay,
  tokenizeSentence,
};
export type { GetConversationalCurriculumOptions };

/**
 * useConversationalCurriculum:
 * Reactive data-resolution hook supplying 3 unique, progressive sentences
 * for any combination of (Day 1–90, Age, Level, Category, Topic, Target Language, Mother Tongue, and Remediation Variant).
 */
export function useConversationalCurriculum(
  options: GetConversationalCurriculumOptions
): ConversationalCurriculumResult & CardPracticeData {
  return useMemo(() => {
    return getCardPracticeData(options);
  }, [
    options.ageGroup,
    options.level,
    options.currentDay ?? options.day,
    options.topicId,
    options.targetLanguage,
    options.motherTongue,
    options.category,
    options.remediationVariant,
    options.weekSeed,
  ]);
}
