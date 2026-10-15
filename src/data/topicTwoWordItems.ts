import { LanguageCode } from '../types';
import { MultilingualTwoWordItem } from './multilingual/types';
import { CAT1_W1, CAT1_W2 } from './multilingual/cat1_home_family_travel';
import { CAT2_W1, CAT2_W2 } from './multilingual/cat2_shopping_health_school';
import { CAT3_W1, CAT3_W2 } from './multilingual/cat3_friends_nature_manners';
import { CAT4_W1, CAT4_W2 } from './multilingual/cat4_tech_weather_holidays';
import { CAT5_W1, CAT5_W2 } from './multilingual/cat5_sports_clothes_chores';

export type TwoWordItem = MultilingualTwoWordItem;

/**
 * AGE 7-9 BEGINNER: WEEK 1 (Days 1 to 7)
 * STRICT 100% [MODIFIER / ADJECTIVE] + [NOUN] PATTERN
 * Strictly TWO (2) words across all 15 categories and 77 topics.
 * Authentic native natural spoken phrasing across all 15 languages (Zero literal translations).
 * Zero action verbs.
 */
export const TOPIC_TWO_WORD_ITEMS_W1: Record<string, [TwoWordItem, TwoWordItem, TwoWordItem]> = {
  ...CAT1_W1,
  ...CAT2_W1,
  ...CAT3_W1,
  ...CAT4_W1,
  ...CAT5_W1,
};

/**
 * AGE 7-9 BEGINNER: WEEK 2 (Days 8 to 14)
 * STRICT 100% [ACTION VERB] + [NOUN] PATTERN
 * Strictly TWO (2) words across all 15 categories and 77 topics.
 * Active everyday domestic verbs followed by topic-related nouns across all 15 languages.
 */
export const TOPIC_TWO_WORD_ITEMS_W2: Record<string, [TwoWordItem, TwoWordItem, TwoWordItem]> = {
  ...CAT1_W2,
  ...CAT2_W2,
  ...CAT3_W2,
  ...CAT4_W2,
  ...CAT5_W2,
};

/**
 * Backwards compatibility alias
 */
export const TOPIC_TWO_WORD_ITEMS = TOPIC_TWO_WORD_ITEMS_W1;

/**
 * Resolves a two-word item into a full PhraseBundle with authentic natural speech
 * across all 15 supported languages:
 * 1. English (en)
 * 2. Arabic (ar)
 * 3. Urdu (ur)
 * 4. Hindi (hi)
 * 5. Spanish (es)
 * 6. French (fr)
 * 7. Mandarin (zh)
 * 8. Turkish (tr)
 * 9. Indonesian (id)
 * 10. Italian (it)
 * 11. German (de)
 * 12. Japanese (ja)
 * 13. Portuguese (pt)
 * 14. Russian (ru)
 * 15. Korean (ko)
 */
export function resolveTwoWordBundle(
  item: TwoWordItem,
  targetLanguage: LanguageCode
): {
  target: Record<LanguageCode, string>;
  romanized: Record<LanguageCode, string>;
  wordCount: number;
} {
  return {
    target: item.target,
    romanized: item.romanized,
    wordCount: 2,
  };
}
