import fs from 'fs';
import path from 'path';

// Helper to construct dictionary items with all 15 languages
export function makeItem(en, ur, ur_rom, hi, hi_rom, ar, ar_rom, es, es_rom, fr, fr_rom, de, de_rom, it, it_rom, pt, pt_rom, ru, ru_rom, tr, tr_rom, id, id_rom, zh, zh_rom, ja, ja_rom, ko, ko_rom) {
  return {
    en,
    ur,
    ur_rom,
    es,
    es_rom,
    target: {
      en,
      ur,
      hi,
      ar,
      es,
      fr,
      de,
      it,
      pt,
      ru,
      tr,
      id,
      zh,
      ja,
      ko
    },
    romanized: {
      en,
      ur: ur_rom,
      hi: hi_rom,
      ar: ar_rom,
      es: es_rom,
      fr: fr_rom,
      de: de_rom,
      it: it_rom,
      pt: pt_rom,
      ru: ru_rom,
      tr: tr_rom,
      id: id_rom,
      zh: zh_rom,
      ja: ja_rom,
      ko: ko_rom
    }
  };
}

console.log("Lexicon builder helper loaded successfully.");
