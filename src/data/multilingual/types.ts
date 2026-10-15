import { LanguageCode } from '../../types';

export interface MultilingualTwoWordItem {
  en: string;
  ur: string;
  ur_rom: string;
  es: string;
  es_rom: string;
  target: Record<LanguageCode, string>;
  romanized: Record<LanguageCode, string>;
}
