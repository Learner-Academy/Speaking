import { LanguageCode, LanguageInfo } from '../types';

export const SUPPORTED_LANGUAGES: Record<LanguageCode, LanguageInfo> = {
  // Primary Languages
  en: {
    code: 'en',
    label: 'English',
    nativeName: 'English',
    flag: '🇬🇧',
    speechLocale: 'en-US',
    dir: 'ltr',
  },
  es: {
    code: 'es',
    label: 'Spanish',
    nativeName: 'Español',
    flag: '🇪🇸',
    speechLocale: 'es-ES',
    dir: 'ltr',
  },
  fr: {
    code: 'fr',
    label: 'French',
    nativeName: 'Français',
    flag: '🇫🇷',
    speechLocale: 'fr-FR',
    dir: 'ltr',
  },
  zh: {
    code: 'zh',
    label: 'Chinese',
    nativeName: '中文',
    flag: '🇨🇳',
    speechLocale: 'zh-CN',
    dir: 'ltr',
  },
  tr: {
    code: 'tr',
    label: 'Turkish',
    nativeName: 'Türkçe',
    flag: '🇹🇷',
    speechLocale: 'tr-TR',
    dir: 'ltr',
  },
  id: {
    code: 'id',
    label: 'Indonesian',
    nativeName: 'Bahasa Indonesia',
    flag: '🇮🇩',
    speechLocale: 'id-ID',
    dir: 'ltr',
  },
  it: {
    code: 'it',
    label: 'Italian',
    nativeName: 'Italiano',
    flag: '🇮🇹',
    speechLocale: 'it-IT',
    dir: 'ltr',
  },

  // Extended World Languages
  de: {
    code: 'de',
    label: 'German',
    nativeName: 'Deutsch',
    flag: '🇩🇪',
    speechLocale: 'de-DE',
    dir: 'ltr',
  },
  pt: {
    code: 'pt',
    label: 'Portuguese',
    nativeName: 'Português',
    flag: '🇵🇹',
    speechLocale: 'pt-PT',
    dir: 'ltr',
  },
  ru: {
    code: 'ru',
    label: 'Russian',
    nativeName: 'Русский',
    flag: '🇷🇺',
    speechLocale: 'ru-RU',
    dir: 'ltr',
  },
  ja: {
    code: 'ja',
    label: 'Japanese',
    nativeName: '日本語',
    flag: '🇯🇵',
    speechLocale: 'ja-JP',
    dir: 'ltr',
  },
  ko: {
    code: 'ko',
    label: 'Korean',
    nativeName: '한국어',
    flag: '🇰🇷',
    speechLocale: 'ko-KR',
    dir: 'ltr',
  },
  ur: {
    code: 'ur',
    label: 'Urdu',
    nativeName: 'اردو',
    flag: '🇵🇰',
    speechLocale: 'ur-PK',
    dir: 'rtl',
  },
  hi: {
    code: 'hi',
    label: 'Hindi',
    nativeName: 'हिन्दी',
    flag: '🇮🇳',
    speechLocale: 'hi-IN',
    dir: 'ltr',
  },
  ar: {
    code: 'ar',
    label: 'Arabic',
    nativeName: 'العربية',
    flag: '🇸🇦',
    speechLocale: 'ar-SA',
    dir: 'rtl',
  },
};

export const LANGUAGE_LIST = Object.values(SUPPORTED_LANGUAGES);

// Dynamic rotating language array for homepage hero CTA
export const ROTATING_HERO_LANGUAGES = [
  'English',
  'Spanish',
  'French',
  'Chinese',
  'Turkish',
  'Indonesian',
  'Italian',
] as const;
