import {
  AgeGroup,
  LearnerLevel,
  LanguageCode,
  ConversationalSentenceItem,
  ConversationalCurriculumResult,
  CardPracticeData,
  CardPracticeItem,
} from '../types';
import {
  TOPIC_TWO_WORD_ITEMS,
  TOPIC_TWO_WORD_ITEMS_W1,
  TOPIC_TWO_WORD_ITEMS_W2,
  resolveTwoWordBundle,
} from './topicTwoWordItems';
import {
  TOPIC_SINGLE_WORD_ITEMS,
  resolveSingleWordBundle,
} from './multilingual/topicSingleWordItems';
import {
  TOPIC_AGE4TO6_W4,
  TOPIC_AGE4TO6_TIER2,
  TOPIC_AGE4TO6_TIER3,
  resolveAge4to6Bundle,
} from './multilingual/topicAge4to6Curriculum';

// ============================================================================
// 90-DAY CONVERSATIONAL SPEAKING DATA ENGINE
// ============================================================================

/**
 * 1. 90-DAY PROGRESSION ARCHITECTURE (3 TIERS × 30 DAYS)
 * - Tier 1: Days 1–30 (Foundation & Habit Formation)
 * - Tier 2: Days 31–60 (Expansion & Conversational Rhythm)
 * - Tier 3: Days 61–90 (Fluency, Spontaneous Dialogues & Real-life Questions)
 */
export function getTierForDay(day: number): 1 | 2 | 3 {
  if (day <= 30) return 1;
  if (day <= 60) return 2;
  return 3;
}

/**
 * 2. STRICT SPEAKING PROGRESSION LADDER BY AGE & LEVEL
 * Computes exact target word count for any combination of ageGroup, level, and day.
 */
export function getTargetWordCount(
  ageGroup: AgeGroup,
  level: LearnerLevel,
  day: number,
  sentenceIdx: number = 1
): number {
  const week = Math.ceil(day / 7);

  // --- A. Age Group 4–6 ---
  if (ageGroup === '4-6') {
    if (level === 'Beginner') {
      // WEEK 1 (Days 1 to 7) -> STRICTLY 1 SINGLE WORD PER ITEM
      if (week === 1) return 1;
      // WEEK 2 (Days 8 to 14) -> STRICTLY 2 WORDS: "MODIFIER + NOUN"
      if (week === 2) return 2;
      // WEEK 3 (Days 15 to 21) -> STRICTLY 2 WORDS: "ACTION VERB + NOUN"
      if (week === 3) return 2;
      // WEEK 4 (Days 22 to 30) -> STRICTLY 3 WORDS PER ITEM
      if (week === 4 || day <= 30) return 3;
      // TIER 2 (Days 31 to 60) -> STRICTLY 4 TO 5 WORDS PER ITEM
      if (day <= 60) {
        return (day + sentenceIdx) % 2 === 0 ? 5 : 4;
      }
      // TIER 3 (Days 61 to 90) -> STRICTLY 5 TO 6 WORDS PER ITEM
      return (day + sentenceIdx) % 2 === 0 ? 6 : 5;
    }
    if (level === 'Intermediate') {
      // Week 1 (Days 1 to 7): Exactly 2 words per item.
      if (week === 1) return 2;
      // Week 2 (Days 8 to 14): Exactly 3 words per item.
      if (week === 2) return 3;
      // Week 3 (Days 15 to 21): Exactly 4 words per item.
      if (week === 3) return 4;
      // Week 4 (Days 22 to 30): Exactly 5 words per item.
      if (week === 4 || day <= 30) return 5;
      // Tier 2 (Days 31 to 60): Exactly 5 to 6 words per item.
      if (day <= 60) {
        return (day + sentenceIdx) % 2 === 0 ? 6 : 5;
      }
      // Tier 3 (Days 61 to 90): Exactly 6 to 7 words per item.
      return (day + sentenceIdx) % 2 === 0 ? 7 : 6;
    }
    // Advanced
    // Week 1 (Days 1 to 7): Exactly 3 words per item.
    if (week === 1) return 3;
    // Week 2 (Days 8 to 14): Exactly 4 words per item.
    if (week === 2) return 4;
    // Week 3 (Days 15 to 21): Exactly 5 words per item.
    if (week === 3) return 5;
    // Week 4 (Days 22 to 30): Exactly 6 words per item.
    if (week === 4 || day <= 30) return 6;
    // Tier 2 (Days 31 to 60): Exactly 6 to 7 words per item.
    if (day <= 60) {
      return (day + sentenceIdx) % 2 === 0 ? 7 : 6;
    }
    // Tier 3 (Days 61 to 90): Exactly 7 to 8 words per item.
    return (day + sentenceIdx) % 2 === 0 ? 8 : 7;
  }

  // --- B. Age Group 7–9 ---
  if (ageGroup === '7-9') {
    if (level === 'Beginner') {
      if (week === 1 || week === 2) {
        // Week 1 (Days 1–7): Strictly 2-word [Modifier + Noun] pairs across all 15 categories & 77 topics
        // Week 2 (Days 8–14): Strictly 2-word [Action Verb + Noun] pairs across all 15 categories & 77 topics
        return 2;
      }
      if (week === 3) return 5; // Days 15-21: Exactly 5 words
      if (week === 4) return 6; // Days 22-30: Exactly 6 words
      // Days 31-90: Conversational 5 to 6-word social dialogue
      return (day + sentenceIdx) % 2 === 0 ? 6 : 5;
    }
    if (level === 'Intermediate') {
      if (week === 1) return 3;
      if (week === 2) return 4;
      if (week === 3) return 5;
      if (week === 4) return 6;
      // Days 31-90: 6 to 7 words
      return (day + sentenceIdx) % 2 === 0 ? 7 : 6;
    }
    // Advanced
    if (week === 1) return 4;
    if (week === 2) return 5;
    if (week === 3) return 6;
    if (week === 4) return 7;
    // Days 31-90: 7 to 8 words
    return (day + sentenceIdx) % 2 === 0 ? 8 : 7;
  }

  // --- C. Age Group 10–12 ---
  if (ageGroup === '10-12') {
    if (level === 'Beginner') {
      if (week === 1) return day <= 3 ? 2 : 3;
      if (week === 2) return 4;
      if (week === 3) return 5;
      if (week === 4) return 6;
      return (day + sentenceIdx) % 2 === 0 ? 7 : 6;
    }
    if (level === 'Intermediate') {
      if (week === 1) return day <= 3 ? 3 : 4;
      if (week === 2) return 5;
      if (week === 3) return 6;
      if (week === 4) return 7;
      return (day + sentenceIdx) % 2 === 0 ? 8 : 7;
    }
    // Advanced
    if (week === 1) return day <= 3 ? 4 : 5;
    if (week === 2) return 6;
    if (week === 3) return 7;
    if (week === 4) return 8;
    return (day + sentenceIdx) % 2 === 0 ? 9 : 8;
  }

  // --- D. Age Group 13–16 ---
  if (level === 'Beginner') {
    if (week === 1) return day <= 3 ? 2 : 3;
    if (week === 2) return 4;
    if (week === 3) return 5;
    if (week === 4) return 6;
    return (day + sentenceIdx) % 2 === 0 ? 8 : 7;
  }
  if (level === 'Intermediate') {
    if (week === 1) return 4;
    if (week === 2) return 5;
    if (week === 3) return 6;
    if (week === 4) return 7;
    return (day + sentenceIdx) % 2 === 0 ? 9 : 8;
  }
  // Advanced
  if (week === 1) return 5;
  if (week === 2) return 6;
  if (week === 3) return 7;
  if (week === 4) return 8;
  return (day + sentenceIdx) % 2 === 0 ? 10 : 8;
}

// Tokenizer for Step 3 Assembly Tray
export function tokenizeSentence(text: string, lang: LanguageCode): string[] {
  if (!text) return [];

  // For Asian scripts without standard spacing (zh, ja)
  if (lang === 'zh') {
    const clean = text.replace(/[，。！？!?,]/g, '').trim();
    if (clean.includes(' ')) {
      return clean.split(/\s+/).filter(Boolean);
    }
    const tokens: string[] = [];
    for (let i = 0; i < clean.length; i += 2) {
      tokens.push(clean.slice(i, Math.min(clean.length, i + 2)));
    }
    return tokens.length > 0 ? tokens : [text];
  }

  if (lang === 'ja') {
    const clean = text.replace(/[、。！？!?,]/g, '').trim();
    if (clean.includes(' ')) {
      return clean.split(/\s+/).filter(Boolean);
    }
    const tokens: string[] = [];
    for (let i = 0; i < clean.length; i += 2) {
      tokens.push(clean.slice(i, Math.min(clean.length, i + 2)));
    }
    return tokens.length > 0 ? tokens : [text];
  }

  // Space-delimited languages (en, es, ur, hi, ar, fr, tr, id, it, de, pt, ru, ko)
  return text
    .split(/\s+/)
    .map((w) => w.trim())
    .filter((w) => w.length > 0);
}

// ============================================================================
// TOPIC LEXICAL CONVERSATION BLUEPRINTS
// ============================================================================

export interface PhraseBundle {
  target: Record<LanguageCode, string>;
  romanized: Record<LanguageCode, string>;
  wordCount: number;
}

interface TopicConversationalData {
  topicId: string;
  category: string;
  // 1-word single items (for 4-6 Day 1)
  singleWords: Record<LanguageCode, string[]>;
  singleWordsRomanized: Record<LanguageCode, string[]>;
  // Progressive sentence templates by target word count
  // Map from word count (2..10) to Variant A and Variant B (Remediation) bundles
  variantsByCountA: Record<number, PhraseBundle[]>;
  variantsByCountB: Record<number, PhraseBundle[]>;
}

// Build canonical 15-language phrase bundle
function makeBundle(
  en: string,
  es: string,
  ur: string,
  hi: string,
  ar: string,
  fr: string,
  de: string,
  it: string,
  pt: string,
  ru: string,
  tr: string,
  id: string,
  zh: string,
  ja: string,
  ko: string,
  roman: Partial<Record<LanguageCode, string>> = {}
): PhraseBundle {
  const enCount = en.replace(/[¡!¿?,.:;，。]/g, '').trim().split(/\s+/).filter(Boolean).length;
  return {
    wordCount: enCount,
    target: {
      en,
      es,
      ur,
      hi,
      ar,
      fr,
      de,
      it,
      pt,
      ru,
      tr,
      id,
      zh,
      ja,
      ko,
    },
    romanized: {
      en: roman.en || en,
      es: roman.es || es,
      ur: roman.ur || ur,
      hi: roman.hi || hi,
      ar: roman.ar || ar,
      fr: roman.fr || fr,
      de: roman.de || de,
      it: roman.it || it,
      pt: roman.pt || pt,
      ru: roman.ru || ru,
      tr: roman.tr || tr,
      id: roman.id || id,
      zh: roman.zh || zh,
      ja: roman.ja || ja,
      ko: roman.ko || ko,
    },
  };
}

// ============================================================================
// COMPREHENSIVE MULTI-WORD THEMATIC REPOSITORY (COVERS 15 CATEGORIES & 77 TOPICS)
// ============================================================================

// Key canonical topics with explicit authentic child and native conversational sentences:
const CANONICAL_TOPIC_DATA: Record<string, Partial<TopicConversationalData>> = {
  'breakfast-chat': {
    topicId: 'breakfast-chat',
    category: 'Home & Daily Life',
    singleWords: {
      en: ['Toast', 'Milk', 'Juice', 'Eggs', 'Water'],
      es: ['Pan', 'Leche', 'Jugo', 'Huevos', 'Agua'],
      ur: ['ٹوسٹ', 'دودھ', 'جوس', 'انڈے', 'پانی'],
      hi: ['टोस्ट', 'दूध', 'जूस', 'अंडे', 'पानी'],
      ar: ['خبز', 'حليب', 'عصير', 'بيض', 'ماء'],
      fr: ['Pain', 'Lait', 'Jus', 'Œufs', 'Eau'],
      de: ['Toast', 'Milch', 'Saft', 'Eier', 'Wasser'],
      it: ['Pane', 'Latte', 'Succo', 'Uova', 'Acqua'],
      pt: ['Pão', 'Leite', 'Suco', 'Ovos', 'Água'],
      ru: ['Тост', 'Молоко', 'Сок', 'Яйца', 'Вода'],
      tr: ['Tost', 'Süt', 'Meyve suyu', 'Yumurta', 'Su'],
      id: ['Roti', 'Susu', 'Jus', 'Telur', 'Air'],
      zh: ['吐司', '牛奶', '果汁', '鸡蛋', '水'],
      ja: ['パン', 'ミルク', 'ジュース', 'たまご', 'みず'],
      ko: ['토스트', '우유', '주스', '달걀', '물'],
    },
    singleWordsRomanized: {
      en: ['Toast', 'Milk', 'Juice', 'Eggs', 'Water'],
      es: ['Pahn', 'LEH-cheh', 'KHOO-goh', 'WEH-vohs', 'AH-gwah'],
      ur: ['Toast', 'Doodh', 'Juice', 'Anday', 'Paani'],
      hi: ['Toast', 'Doodh', 'Juice', 'Ande', 'Paani'],
      ar: ['Khubz', 'Haleeb', 'Aseer', 'Bayd', 'Maa'],
      fr: ['Pan', 'Lay', 'Zhoo', 'Uh', 'Oh'],
      de: ['Tohst', 'Milsh', 'Zahft', 'Eye-er', 'Vahs-ser'],
      it: ['Pah-neh', 'Laht-teh', 'Sook-koh', 'WOH-vah', 'AHK-wah'],
      pt: ['Pohn', 'LAY-chee', 'SOO-koo', 'OH-voos', 'AH-gwah'],
      ru: ['Tohst', 'Mah-lah-KOH', 'Sohk', 'YAY-tsah', 'Vah-DAH'],
      tr: ['Tohst', 'Sewt', 'May-veh soo-yoo', 'Yoo-moor-tah', 'Soo'],
      id: ['Roh-tee', 'Soo-soo', 'Djoos', 'Teh-loor', 'Ah-yeer'],
      zh: ['Tǔsī', 'Niúnǎi', 'Guǒzhī', 'Jīdàn', 'Shuǐ'],
      ja: ['Pahn', 'Mee-roo-koo', 'Joo-soo', 'Tah-mah-goh', 'Mee-zoo'],
      ko: ['Toh-soo-teu', 'Oo-yoo', 'Joo-soo', 'Dahl-gyahl', 'Mool'],
    },
    variantsByCountA: {
      // 2 Words (Days 2-7, 4-6 Beginner)
      2: [
        makeBundle(
          'Warm toast.',
          'Pan caliente.',
          'گرم ٹوسٹ۔',
          'गरम टोस्ट।',
          'خبز دافئ.',
          'Pain chaud.',
          'Warmer Toast.',
          'Pane caldo.',
          'Pão quente.',
          'Тёплый тост.',
          'Sıcak tost.',
          'Roti hangat.',
          '热吐司。',
          '温かい パン。',
          '따뜻한 토스트.',
          { ur: 'Garam toast.', es: 'Pahn kah-LYEHN-teh', fr: 'Pan shoh' }
        ),
        makeBundle(
          'Fresh milk.',
          'Leche fresca.',
          'تازہ دودھ۔',
          'ताजा दूध।',
          'حليب طازج.',
          'Lait frais.',
          'Frische Milch.',
          'Latte fresco.',
          'Leite fresco.',
          'Свежее молоко.',
          'Taze süt.',
          'Susu segar.',
          '新鲜 牛奶。',
          'しんせん ミルク。',
          '신선한 우유.',
          { ur: 'Taaza doodh.', es: 'LEH-cheh FREHS-kah' }
        ),
        makeBundle(
          'Sweet juice.',
          'Jugo dulce.',
          'میٹھا جوس۔',
          'मीठा जूस।',
          'عصير حلو.',
          'Jus doux.',
          'Süßer Saft.',
          'Succo dolce.',
          'Suco doce.',
          'Сладкий сок.',
          'Tatlı meyve suyu.',
          'Jus manis.',
          '甜 果汁。',
          'あまい ジュース。',
          '달콤한 주스.',
          { ur: 'Meetha juice.', es: 'KHOO-goh DOOL-seh' }
        ),
      ],
      // 3 Words (Week 2, 4-6; Week 1, 7-9)
      3: [
        makeBundle(
          'I want milk.',
          'Quiero leche fresca.',
          'مجھے دودھ چاہیے۔',
          'मुझे दूध चाहिए।',
          'أريد حليباً طازجاً.',
          'Je veux lait.',
          'Ich will Milch.',
          'Voglio latte fresco.',
          'Eu quero leite.',
          'Я хочу молоко.',
          'Ben süt istiyorum.',
          'Saya mau susu.',
          '我 要 牛奶。',
          'ミルク ほしい です。',
          '우유 주세요.',
          { ur: 'Mujhe doodh chahiye.', es: 'Kyeh-roh LEH-cheh FREHS-kah' }
        ),
        makeBundle(
          'Pass the toast.',
          'Pasa el pan.',
          'ٹوسٹ ادھر دیں۔',
          'टोस्ट इधर दीजिए।',
          'مرر الخبز لي.',
          'Passe le pain.',
          'Gib den Toast.',
          'Passa il pane.',
          'Passe o pão.',
          'Передай мне тост.',
          'Tostu uzat lütfen.',
          'Operkan roti itu.',
          '把 吐司 递给我。',
          'パン を ください。',
          '토스트 주세요.',
          { ur: 'Toast idhar dein.', es: 'PAH-sah ehl pahn' }
        ),
        makeBundle(
          'Eat breakfast together.',
          'Comamos rico juntos.',
          'ساتھ ناشتہ کریں۔',
          'साथ नाश्ता करें।',
          'نتناول الإفطار معاً.',
          'Mangeons ensemble matin.',
          'Frühstücken wir zusammen.',
          'Facciamo colazione insieme.',
          'Tomemos café juntos.',
          'Позавтракаем вместе дружно.',
          'Birlikte kahvaltı yapalım.',
          'Sarapan bersama kita.',
          '一起 吃 早餐。',
          'いっしょに あさごはん。',
          '함께 아침 먹어요.',
          { ur: 'Saath nashta karein.', es: 'Koh-MAH-mohs REE-koh KHOON-tohs' }
        ),
      ],
      // 4 Words (e.g. Day 11 "Breakfast Chat", 7-9 Beginner: "I want warm toast." / "مجھے گرم ٹوسٹ چاہیے۔")
      4: [
        makeBundle(
          'I want warm toast.',
          'Quiero pan tostado caliente.',
          'مجھے گرم ٹوسٹ چاہیے۔',
          'मुझे गरम टोस्ट चाहिए।',
          'أريد خبزاً محمصاً دافئاً.',
          'Je veux pain chaud.',
          'Ich möchte warmen Toast.',
          'Voglio pane tostato caldo.',
          'Quero pão torrado quente.',
          'Я хочу тёплый тост.',
          'Sıcak kızarmış tost istiyorum.',
          'Saya mau roti hangat.',
          '我 想要 热 吐司。',
          'あたたかい パン が ほしい。',
          '따뜻한 토스트를 원해요.',
          { ur: 'Mujhe garam toast chahiye.', es: 'Kyeh-roh pahn tohs-TAH-doh kah-LYEHN-teh' }
        ),
        makeBundle(
          'Please pour fresh milk.',
          'Sirve leche fresca porfavor.',
          'براہ کرم تازہ دودھ ڈالیں۔',
          'कृपया ताजा दूध डालिए।',
          'اسكب الحليب الطازج فضلاً.',
          'Verse du lait frais.',
          'Schenke frische Milch ein.',
          'Versa il latte fresco.',
          'Por favor sirva leite.',
          'Налей пожалуйста свежее молоко.',
          'Lütfen taze süt koy.',
          'Tolong tuang susu segar.',
          '请 倒 新鲜 牛奶。',
          'しんせん ミルク を ください。',
          '신선한 우유를 부어주세요.',
          { ur: 'Barahe karam taaza doodh daalein.', es: 'SEER-veh LEH-cheh FREHS-kah pohr-fah-vohr' }
        ),
        makeBundle(
          'Pass the butter knife.',
          'Pásame el cuchillo mantequilla.',
          'مکھن والی چھری دیں۔',
          'मक्खन वाली छुरी दीजिए।',
          'مرر سكين الزبدة لي.',
          'Passe le couteau beurre.',
          'Reiche das Buttermesser herüber.',
          'Passami il coltello burro.',
          'Passe a faca manteiga.',
          'Передай мне нож масло.',
          'Tereyağı bıçağını uzat lütfen.',
          'Operkan pisau mentega itu.',
          '请 递给 我 黄油刀。',
          'バター ナイフ を ください。',
          '버터 나이프를 건네주세요.',
          { ur: 'Makkhan wali chhuri dein.', es: 'PAH-sah-meh ehl koo-CHEE-yoh mahn-teh-KEE-yah' }
        ),
      ],
      // 5 Words (Week 3, 7-9 Beginner; Week 4, 4-6)
      5: [
        makeBundle(
          'Please pass the orange juice.',
          'Pásame el jugo de naranja.',
          'براہ کرم مالٹے کا جوس دیں۔',
          'कृपया संतरे का रस दीजिए।',
          'ناولني عصير البرتقال لو سمحت.',
          'Passe le jus d\'orange s\'il-te-plaît.',
          'Reiche mir bitte den Orangensaft.',
          'Passami il succo d\'arancia per favore.',
          'Passe o suco de laranja.',
          'Передай пожалуйста вкусный апельсиновый сок.',
          'Lütfen portakal suyunu bana uzat.',
          'Tolong operkan jus jeruk segar.',
          '请 递给 我 橙汁。',
          'オレンジ ジュース を ください な。',
          '오렌지 주스를 건네주세요 부탁해요.',
          { ur: 'Barahe karam maltay ka juice dein.', es: 'PAH-sah-meh ehl KHOO-goh deh nah-RAHN-khah' }
        ),
        makeBundle(
          'I like crunchy breakfast cereal.',
          'Me gusta el cereal crujiente.',
          'مجھے خستہ اناج پسند ہے۔',
          'मुझे क्रंची नाश्ता अनाज पसंद।',
          'أحب رقائق الإفطار المقرمشة اللذيذة.',
          'J\'aime les céréales bien croustillantes.',
          'Ich mag knuspriges Frühstücks-Müsli sehr.',
          'Mi piacciono i cereali croccanti.',
          'Gosto de cereal bem crocante.',
          'Мне нравятся хрустящие утренние хлопья.',
          'Çıtır kahvaltılık gevrekleri çok severim.',
          'Saya suka sereal sarapan renyah.',
          '我 喜欢 酥脆 的 谷物。',
          'サクサク の シリアル が すき。',
          '바삭한 아침 시리얼을 정말 좋아해요.',
          { ur: 'Mujhe khasta anaaj pasand hai.', es: 'Meh GOOS-tah ehl seh-reh-AHL kroo-khyehn-teh' }
        ),
        makeBundle(
          'Would you like some butter?',
          '¿Quieres un poco de mantequilla?',
          'کیا آپ کو مکھن چاہیے؟',
          'क्या आपको थोड़ा मक्खन चाहिए?',
          'هل ترغب بقليل من الزبدة؟',
          'Veux-tu un peu de beurre ?',
          'Möchtest du etwas weiche Butter?',
          'Vuoi un po\' di burro?',
          'Você quer um pouco de manteiga?',
          'Хочешь немного свежего сливочного масла?',
          'Biraz taze tereyağı ister misin?',
          'Apakah kamu mau sedikit mentega?',
          '你 想要 一些 黄油 吗？',
          'バター を すこし いかが ですか？',
          '버터를 조금 드시겠어요 지금?',
          { ur: 'Kya aap ko makhan chahiye?', es: 'KYEH-rehs oon POH-koh deh mahn-teh-KEE-yah' }
        ),
      ],
      // 6 Words (Week 4, 7-9 Beginner)
      6: [
        makeBundle(
          'May I please have scrambled eggs?',
          '¿Me das huevos revueltos por favor?',
          'کیا مجھے تلے ہوئے انڈے ملیں گے؟',
          'क्या मुझे भुर्जी वाले अंडे मिलेंगे?',
          'هل يمكنني الحصول على بيض مخفوق؟',
          'Puis-je avoir des œufs brouillés ?',
          'Kann ich bitte Rühreier zum Frühstück haben?',
          'Posso avere delle uova strapazzate per favore?',
          'Posso pedir ovos mexidos bem quentinhos?',
          'Можно мне пожалуйста порцию вкусного омлета?',
          'Bana çırpılmış lezzetli yumurta verir misiniz?',
          'Bolehkah saya minta telur orak-arik lezat?',
          '请问 我 可以 吃 炒鸡蛋 吗？',
          'いりたまご を いただいても いい ですか？',
          '스크램블 에그를 부탁드려도 괜찮을까요 지금?',
          { ur: 'Kya mujhe talay huay anday milein gay?', es: 'Meh dahs WEH-vohs reh-VWEHL-tohs pohr fah-vohr' }
        ),
        makeBundle(
          'This fresh berry jam tastes wonderful.',
          'Esta rica mermelada sabe deliciosa hoy.',
          'یہ تازہ بیری جیم بہت عمدہ ہے۔',
          'यह ताजा बेरी जैम बहुत स्वादिष्ट है।',
          'هذا المربى الطازج طعمه رائع للغاية.',
          'Cette confiture de baies est délicieuse.',
          'Diese frische Beeren-Marmelade schmeckt fantastisch gut.',
          'Questa marmellata fresca ai frutti è ottima.',
          'Esta geleia fresca de frutas é maravilhosa.',
          'Это свежее ягодное варенье просто восхитительно.',
          'Bu taze orman meyveli reçel harika.',
          'Selai buah beri segar ini sangat lezat.',
          '这个 新鲜 果酱 尝起来 太 棒了。',
          'この ベリー ジャム は とても おいしい。',
          '이 신선한 베리 잼은 정말 맛있어요.',
          { ur: 'Yeh taaza berry jam bohat umdah hai.', es: 'EHS-tah REE-kah mehr-meh-LAH-dah SAH-beh deh-lee-SYOH-sah' }
        ),
        makeBundle(
          'We always start breakfast with gratitude.',
          'Siempre desayunamos con mucha linda gratitud.',
          'ہم ہمیشہ شکرگزاری سے ناشتہ کرتے ہیں۔',
          'हम हमेशा धन्यवाद के साथ नाश्ता करते।',
          'نبدأ وجبة الإفطار دائماً بقلب شاكر.',
          'Nous commençons le petit déjeuner avec gratitude.',
          'Wir beginnen unser Frühstück immer mit Dankbarkeit.',
          'Iniziamo sempre la colazione con gratitudine sincera.',
          'Sempre começamos nosso café da manhã gratos.',
          'Мы всегда начинаем наш завтрак с благодарности.',
          'Kahvaltımıza her zaman içten şükranla başlarız.',
          'Kami selalu memulai sarapan dengan rasa syukur.',
          '我们 总是 怀着 感恩 吃 早餐。',
          'いつも かんしゃ して あさごはん を たべます。',
          '우리는 항상 감사하는 마음으로 아침을 시작해요.',
          { ur: 'Hum hamesha shukarguzari se nashta kartay hain.' }
        ),
      ],
      // 7-8 Words (13-16 Beginner, Intermediate & Advanced)
      7: [
        makeBundle(
          'Could you pass me that jar of honey?',
          '¿Podrías pasarme ese rico frasco de miel?',
          'کیا آپ مجھے وہ شہد کا جار دیں گے؟',
          'क्या आप मुझे वह शहद का जार देंगे?',
          'هل يمكنك أن تمرر لي جرة العسل؟',
          'Pourriez-vous me passer ce pot de miel ?',
          'Könntest du mir bitte das Honigglas herüberreichen?',
          'Potresti passarmi quel vasetto di miele fresco?',
          'Você poderia me passar aquele pote de mel?',
          'Не мог бы ты передать мне эту баночку?',
          'O leziz bal kavanozunu bana uzatabilir misiniz?',
          'Bisakah Anda mengoperkan toples madu manis itu?',
          '你可以 帮我 递一下 那罐 蜂蜜 吗？',
          'その はちみつ の びん を とって もらえますか？',
          '그 꿀단지를 저에게 건네주실 수 있나요?',
          { ur: 'Kya aap mujhe woh shehad ka jar dein gay?' }
        ),
        makeBundle(
          'Having a warm breakfast gives us morning energy.',
          'Desayunar calentito nos da mucha energía de mañana.',
          'گرم ناشتہ ہمیں صبح کی زبردست توانائی دیتا ہے۔',
          'गरम नाश्ता हमें सुबह बहुत ऊर्जा देता है।',
          'تناول وجبة إفطار دافئة يمنحنا طاقة صباحية.',
          'Prendre un bon déjeuner donne beaucoup d\'énergie matinale.',
          'Ein warmes gesundes Frühstück gibt uns viel Energie.',
          'Fare una buona colazione calda dona molta energia.',
          'Tomar um café da manhã quente dá energia.',
          'Тёплый питательный завтрак дарит нам бодрость с утра.',
          'Sıcak bir kahvaltı yapmak bize bol enerji verir.',
          'Sarapan hangat memberi kita banyak energi di pagi.',
          '吃 一顿 温暖的 早餐 给 我们 满满 活力。',
          'あたたかい あさごはん は あさの 元気 を くれます。',
          '따뜻한 아침 식사는 우리에게 활기찬 에너지를 선물해줘요.',
          { ur: 'Garam nashta humein subah ki zabardast tawanaai deta hai.' }
        ),
        makeBundle(
          'Please pour another hot cup of herbal tea.',
          'Por favor sírveme otra taza de té calientito.',
          'براہ کرم ہربل چائے کا ایک اور کپ ڈالیں۔',
          'कृपया हर्बल चाय का एक और प्याला दीजिए।',
          'يرجى سكب كوب آخر دافئ من شاي الأعشاب.',
          'Verse une autre tasse chaude d\'infusion aux herbes.',
          'Schenke mir bitte noch eine Tasse Kräutertee ein.',
          'Versami un\'altra tazza calda di tisana alle erbe.',
          'Por favor sirva outra xícara quente de chá.',
          'Налей пожалуйста ещё одну горячую чашечку травяного чая.',
          'Lütfen bir bardak daha sıcak bitki çayı koyunuz.',
          'Tolong tuangkan secangkir teh herbal hangat lagi untukku.',
          '请 再 倒 一杯 热腾腾的 草本 茶。',
          'あたたかい ハーブティー を もういっぱい ください な。',
          '따뜻한 허브차 한 잔만 더 부어주시겠어요?'
        ),
      ],
      8: [
        makeBundle(
          'Breakfast table etiquette shows courtesy and respect towards everyone.',
          'Los buenos modales en la mesa demuestran gran respeto.',
          'کھانے کی میز کے آداب سب کے لیے احترام ظاہر کرتے ہیں۔',
          'नाश्ते की मेज के शिष्टाचार सबका आदर प्रकट करते हैं।',
          'آداب طاولة الإفطار تعبر عن احترام وتقدير الجميع دائماً.',
          'La politesse à table montre un grand respect mutuel.',
          'Gute Tischmanieren beim Frühstück zeigen Höflichkeit und Respekt.',
          'Le buone maniere a tavola dimostrano rispetto verso tutti.',
          'A etiqueta à mesa do café demonstra cortesia a todos.',
          'Правила поведения за столом показывают вежливость и уважение.',
          'Kahvaltı masası nezaket kuralları herkese duyulan saygıyı yansıtır.',
          'Tata krama meja sarapan menunjukkan rasa hormat kepada semua.',
          '早餐 桌上 的 礼仪 展现 出 对 大家的 尊重。',
          'テーブル マナー は みんな に たいする おもいやり です。',
          '식탁에서의 바른 예절은 모든 사람에 대한 존중을 보여줘요.'
        ),
        makeBundle(
          'Would you mind slicing another sweet ripe red apple?',
          '¿Te importaría cortar otra rica manzana roja madura hoy?',
          'کیا آپ ایک اور پکا ہوا میٹھا سیب کاٹیں گے؟',
          'क्या आप एक और मीठा पका लाल सेब काटेंगे?',
          'هل تمانع في تقطيع تفاحة حمراء ناضجة وحلوة أخرى؟',
          'Pourriez-vous couper une autre belle pomme rouge sucrée ?',
          'Würdest du bitte noch einen süßen reifen Apfel schneiden?',
          'Ti dispiacerebbe tagliare un\'altra mela rossa dolce e matura?',
          'Você se importaria de fatiar outra maçã vermelha madura?',
          'Не мог бы ты нарезать ещё одно спелое красное яблоко?',
          'Bir tatlı olgun kırmızı elma daha dilimler misiniz lütfen?',
          'Maukah Anda mengiris satu apel merah manis yang matang lagi?',
          '你可以 帮我 再 切一个 熟透的 甜 红苹果 吗？',
          'あまい あかい りんご を もうひとつ きって もらえますか？',
          '달콤하게 익은 빨간 사과를 하나 더 깎아주시겠어요?'
        ),
        makeBundle(
          'I am ready for school right after eating breakfast.',
          'Estoy listo para ir a la escuela tras desayunar.',
          'میں ناشتہ کرنے کے فورا بعد سکول کے لیے تیار ہوں۔',
          'मैं नाश्ता करने के तुरंत बाद स्कूल जाने को तैयार।',
          'أنا جاهز تماماً للذهاب إلى المدرسة بعد هذا الفطور.',
          'Je suis prêt pour l\'école juste après le déjeuner.',
          'Ich bin direkt nach dem Frühstück fertig für die Schule.',
          'Sono pronto per la scuola subito dopo aver fatto colazione.',
          'Estou pronto para a escola logo após o café da manhã.',
          'Я готов отправиться в школу сразу после сытного завтрака.',
          'Kahvaltımı tamamladıktan sonra okula gitmek için tamamen hazırım.',
          'Saya siap berangkat ke sekolah tepat setelah selesai sarapan pagi.',
          '吃完 营养 早餐 后 我 就 准备好 去 上学了。',
          'あさごはん を たべたら すぐに がっこう へ いけます。',
          '든든한 아침 식사를 마치고 바로 학교 갈 준비가 끝났어요.'
        ),
      ],
    },
    // Remediation Variant B (Fresh sentence structures with SAME word count & breakfast theme!)
    variantsByCountB: {
      2: [
        makeBundle('Eat toast.', 'Come pan.', 'ٹوسٹ کھائیں۔', 'टोस्ट खाएं।', 'تناول خبزاً.', 'Mange pain.', 'Iss Toast.', 'Mangia pane.', 'Coma pão.', 'Ешь тост.', 'Tost ye.', 'Makan roti.', '吃 吐司。', 'パン たべて。', '토스트 드세요.'),
        makeBundle('Drink milk.', 'Bebe leche.', 'دودھ پیئیں۔', 'दूध पिएं।', 'اشرب حليباً.', 'Bois lait.', 'Trink Milch.', 'Bevi latte.', 'Beba leite.', 'Пей молоко.', 'Süt iç.', 'Minum susu.', '喝 牛奶。', 'ミルク のんで。', '우유 마셔요.'),
        makeBundle('More juice.', 'Más jugo.', 'مزید جوس۔', 'और जूस।', 'مزيد عصير.', 'Plus jus.', 'Mehr Saft.', 'Più succo.', 'Mais suco.', 'Ещё сока.', 'Daha meyve-suyu.', 'Tambah jus.', '还要 果汁。', 'ジュース もうすこし。', '주스 더.'),
      ],
      3: [
        makeBundle('Pass warm toast.', 'Pasa pan caliente.', 'گرم ٹوسٹ دیں۔', 'गरम टोस्ट दें।', 'مرر خبزاً دافئاً.', 'Passe pain chaud.', 'Gib warmen Toast.', 'Passa pane caldo.', 'Passe pão quente.', 'Передай тёплый тост.', 'Sıcak tostu uzat.', 'Operkan roti hangat.', '递上 热 吐司。', 'パン を ちょうだい。', '토스트를 건네주세요.', { ur: 'Garam toast dein.' }),
        makeBundle('I drink juice.', 'Bebo jugo dulce.', 'میں جوس پیتا ہوں۔', 'मैं जूस पीता।', 'أنا أشرب عصيراً.', 'Je bois jus.', 'Ich trinke Saft.', 'Bevo succo dolce.', 'Bebo suco doce.', 'Я пью сок.', 'Ben meyve-suyu içerim.', 'Saya minum jus.', '我 喝 果汁。', 'ジュース を のむ。', '주스를 마셔요.', { ur: 'Main juice peeta hoon.' }),
        makeBundle('Love morning meals.', 'Amo ricos desayunos.', 'صبح کا ناشتہ پسند۔', 'सुबह का नाश्ता।', 'أحب وجبة الصباح.', 'J\'adore petit déjeuner.', 'Liebe gutes Frühstück.', 'Amo la colazione.', 'Adoro café da manhã.', 'Люблю вкусный завтрак.', 'Sabah kahvaltısını severim.', 'Suka sarapan pagi.', '喜欢 晨间 美味。', 'あさごはん だいすき だよ。', '아침 식사 좋아요.', { ur: 'Subah ka nashta pasand.' }),
      ],
      4: [
        // Variant B Day 11 "Breakfast Chat" (4 words):
        makeBundle(
          'Please pass warm toast.',
          'Pasa pan caliente porfavor.',
          'براہ کرم گرم ٹوسٹ دیں۔',
          'कृपया गरम टोस्ट दीजिए।',
          'مرر الخبز الدافئ رجاءً.',
          'Passe du pain chaud.',
          'Gib bitte warmen Toast.',
          'Passa il pane caldo.',
          'Por favor passe pão.',
          'Передай пожалуйста тёплый тост.',
          'Lütfen sıcak tost uzat.',
          'Tolong operkan roti hangat.',
          '请 递给 我 吐司。',
          'あたたかい パン を ちょうだい。',
          '따뜻한 토스트를 건네주세요.',
          { ur: 'Barahe karam garam toast dein.', es: 'PAH-sah pahn kah-LYEHN-teh pohr-fah-vohr' }
        ),
        makeBundle(
          'I love cold juice.',
          'Amo el jugo frío.',
          'مجھے ٹھنڈا جوس پسند ہے۔',
          'मुझे ठंडा जूस पसंद है।',
          'أحب هذا العصير البارد.',
          'J\'aime le jus frais.',
          'Ich liebe kalten Saft.',
          'Amo il succo freddo.',
          'Adoro o suco gelado.',
          'Люблю этот холодный сок.',
          'Soğuk taze suyu severim.',
          'Saya suka jus dingin.',
          '我 喜爱 冰凉 果汁。',
          'つめたい ジュース が すき。',
          '시원한 주스를 정말 좋아해요.',
          { ur: 'Mujhe thanda juice pasand hai.' }
        ),
        makeBundle(
          'Thank you for breakfast.',
          'Gracias por el desayuno.',
          'ناشتے کے لیے شکریہ۔',
          'नाश्ते के लिए धन्यवाद।',
          'شكراً جزيلاً على الفطور.',
          'Merci pour le déjeuner.',
          'Danke für das Frühstück.',
          'Grazie per la colazione.',
          'Obrigado pelo café delicioso.',
          'Спасибо за вкусный завтрак.',
          'Güzel kahvaltı için teşekkürler.',
          'Terima kasih atas sarapannya.',
          '谢谢 这 丰盛 早餐。',
          'おいしい あさごはん ありがとう。',
          '맛있는 아침 식사 감사합니다.',
          { ur: 'Nashtay ke liye shukriya.' }
        ),
      ],
      5: [
        makeBundle(
          'Can you pass fresh butter?',
          '¿Me pasas la mantequilla fresca?',
          'کیا آپ تازہ مکھن دیں گے؟',
          'क्या आप ताजा मक्खन देंगे?',
          'هل تمرر لي الزبدة الطازجة؟',
          'Peux-tu passer beurre frais ?',
          'Kannst du frische Butter reichen?',
          'Puoi passarmi il burro fresco?',
          'Pode passar a manteiga fresca?',
          'Ты передашь мне свежее масло?',
          'Taze tereyağını uzatabilir misin lütfen?',
          'Bisakah Anda operkan mentega segar?',
          '你能 把 新鲜 黄油 递给我吗？',
          'バター を とって もらえますか？',
          '신선한 버터를 건네주실 수 있나요?',
          { ur: 'Kya aap taaza makhan dein gay?' }
        ),
        makeBundle(
          'I drink milk every morning.',
          'Bebo leche cada rica mañana.',
          'میں ہر صبح دودھ پیتا ہوں۔',
          'मैं हर सुबह दूध पीता हूँ।',
          'أشرب الحليب في كل صباح.',
          'Je bois du lait matin.',
          'Ich trinke jeden Morgen Milch.',
          'Bevo latte fresco ogni mattina.',
          'Bebo leite toda santa manhã.',
          'Я пью молоко каждое утро.',
          'Her sabah taze süt içerim.',
          'Saya minum susu setiap pagi.',
          '我 每天 早晨 喝 牛奶。',
          'まいあさ ミルク を のみます。',
          '저는 매일 아침 우유를 마셔요.',
          { ur: 'Main har subah doodh peeta hoon.' }
        ),
        makeBundle(
          'This warm bread smells amazing.',
          'Este pan huele muy rico.',
          'اس گرم روٹی کی خوشبو شاندار ہے۔',
          'इस गरम ब्रेड की खुशबू शानदार।',
          'رائحة هذا الخبز الدافئ رائعة.',
          'Ce pain chaud sent bon.',
          'Dieses warme Brot riecht herrlich.',
          'Questo pane caldo profuma deliziosamente.',
          'Este pão quente cheira bem.',
          'Этот тёплый хлеб замечательно пахнет.',
          'Bu sıcak ekmek harika kokuyor.',
          'Roti hangat ini harum sekali.',
          '这 烤面包 闻起来 太 香了。',
          'やきたて パン の いい におい。',
          '따뜻한 빵 냄새가 정말 좋아요.',
          { ur: 'Is garam roti ki khushboo shaandaar hai.' }
        ),
      ],
      6: [
        makeBundle(
          'Let us finish our healthy morning breakfast.',
          'Terminemos nuestro saludable y rico desayuno.',
          'آئیں اپنا صحت مند ناشتہ مکمل کریں۔',
          'आइए अपना स्वस्थ नाश्ता समाप्त करें।',
          'دعونا ننهي وجبة إفطارنا الصحية الآن.',
          'Finissons notre sain petit déjeuner ensemble.',
          'Lasst uns unser gesundes Frühstück beenden.',
          'Finiamo la nostra sana e ricca colazione.',
          'Vamos terminar nosso café da manhã saudável.',
          'Давайте доедим наш полезный питательный завтрак.',
          'Hadi sağlıklı sabah kahvaltımızı bitirelim güzelce.',
          'Mari kita selesaikan sarapan sehat kita.',
          '让我们 吃完 营养的 健康 早餐。',
          'けんこうてき な あさごはん を たべおえよう。',
          '건강한 아침 식사를 다 함께 마무리해요.'
        ),
        makeBundle(
          'Please wipe the clean kitchen table nicely.',
          'Por favor limpia bien la mesa.',
          'براہ کرم کھانے کی میز صاف کریں۔',
          'कृपया रसोई की मेज साफ कीजिए।',
          'يرجى مسح طاولة المطبخ النظيفة بلطف.',
          'Essuie la table de cuisine proprement.',
          'Wische bitte den Küchentisch sauber ab.',
          'Pulisci per bene il tavolo della cucina.',
          'Por favor limpe a mesa da cozinha.',
          'Протри пожалуйста чистый кухонный стол аккуратно.',
          'Lütfen mutfak masasını güzelce temizleyin silin.',
          'Tolong bersihkan meja dapur dengan rapi.',
          '请 把 厨房 餐桌 擦 干净。',
          'テーブル を きれいに ふいて ください。',
          '부엌 식탁을 깨끗하게 닦아주시겠어요 정성껏?'
        ),
        makeBundle(
          'I am ready for another cheerful day.',
          'Estoy listo para un día alegre.',
          'میں ایک اور خوشگوار دن کے لیے تیار ہوں۔',
          'मैं एक और खुशहाल दिन को तैयार।',
          'أنا مستعد ليوم جميل جديد مفعم بالحيوية.',
          'Je suis prêt pour journée joyeuse.',
          'Ich bin bereit für einen weiteren fröhlichen Tag.',
          'Sono pronto per un\'altra giornata serena.',
          'Estou pronto para mais um dia feliz.',
          'Я готов к ещё одному радостному дню.',
          'Neşeli güzel bir güne tamamen hazırım.',
          'Saya siap untuk hari menyenangkan berikutnya.',
          '我 准备好 迎接 快乐的 新 一天。',
          'きょう も たのしい いちにち を はじめよう。',
          '활기차고 즐거운 하루를 맞이할 준비가 되었어요.'
        ),
      ],
      7: [
        makeBundle(
          'Could you pass that bottle of fresh juice?',
          '¿Podrías pasar esa rica botella de jugo?',
          'کیا آپ تازہ جوس کی بوتل ادھر بڑھائیں گے؟',
          'क्या आप ताजे जूस की बोतल इधर देंगे?',
          'هل يمكنك تمرير زجاجة العصير الطازج هذه؟',
          'Pourriez-vous me passer cette bouteille de jus ?',
          'Könntest du mir die Flasche Saft herüberreichen?',
          'Potresti passarmi quella bottiglia di succo fresco?',
          'Poderia me passar aquela garrafa de suco?',
          'Не мог бы ты передать эту бутылку сока?',
          'O taze meyve suyu şişesini uzatabilir misiniz?',
          'Bisakah Anda operkan botol jus segar itu?',
          '你可以 帮我 递一下 那瓶 果汁 吗？',
          'その ジュース の ボトル を とって もらえますか？',
          '신선한 주스 병을 저에게 건네주실 수 있나요?'
        ),
        makeBundle(
          'A balanced breakfast helps my mind stay focused.',
          'Un buen desayuno ayuda a mantener la mente.',
          'متوازن ناشتہ میرے ذہن کو چاق و چوبند رکھتا ہے۔',
          'संतुलित नाश्ता मेरे दिमाग को केंद्रित रखता।',
          'الإفطار المتوازن يساعد عقلي على التركيز طوال اليوم.',
          'Un déjeuner équilibré aide à rester bien concentré.',
          'Ein ausgewogenes Frühstück hilft meinem Kopf sich zu konzentrieren.',
          'Una colazione equilibrata aiuta a mantenere la concentrazione.',
          'Um café balanceado ajuda minha mente a focar.',
          'Сбалансированный завтрак помогает мне сохранять внимание и бодрость.',
          'Dengeli bir kahvaltı zihnimi zinde tutmaya yardımcı olur.',
          'Sarapan seimbang membantu pikiran saya tetap fokus belajar.',
          '营养 均衡的 早餐 帮助 我的 大脑 保持 专注。',
          'バランス の よい あさごはん は しゅうちゅう できます。',
          '균형 잡힌 아침 식사는 두뇌 집중력을 높여줘요.'
        ),
        makeBundle(
          'We enjoyed delicious scrambled eggs and berry jam.',
          'Disfrutamos de ricos huevos revueltos con mermelada.',
          'ہم نے لذیذ انڈوں اور بیری جیم کا مزہ لیا۔',
          'हमने स्वादिष्ट भुर्जी और बेरी जैम का आनंद।',
          'لقد استمتعنا بتناول بيض مخفوق ومربى توت لذيذ.',
          'Nous avons dégusté de bons œufs et confiture.',
          'Wir haben leckere Rühreier und Beerenmarmelade genossen.',
          'Abbiamo gustato uova strapazzate e marmellata ai frutti.',
          'Aproveitamos deliciosos ovos mexidos e geleia de frutas.',
          'Мы с удовольствием поели вкусный омлет с вареньем.',
          'Lezzetli çırpılmış yumurtanın ve reçelin tadını çıkardık.',
          'Kami menikmati telur orak-arik dan selai yang lezat.',
          '我们 享用了 美味的 炒鸡蛋 和 甜 果酱。',
          'おいしい たまご と ジャム を たのしみました。',
          '맛있는 스크램블 에그와 베리 잼을 즐겁게 먹었어요.'
        ),
      ],
      8: [
        makeBundle(
          'Remember to say thank you before leaving the table.',
          'Recuerda dar las gracias antes de levantarte.',
          'کھانے کی میز چھوڑنے سے پہلے شکریہ ادا کرنا یاد رکھیں۔',
          'मेज छोड़ने से पहले धन्यवाद कहना हमेशा याद रखें।',
          'تذكر أن تقول شكراً قبل مغادرة طاولة الطعام.',
          'N\'oublie pas de dire merci avant de quitter.',
          'Denk daran, dich vor dem Aufstehen zu bedanken.',
          'Ricordati di dire grazie prima di alzarti da tavola.',
          'Lembre-se de agradecer antes de se levantar da mesa.',
          'Не забудь сказать спасибо перед тем как встать.',
          'Sofradan kalkmadan önce teşekkür etmeyi her zaman hatırla.',
          'Ingatlah untuk mengucapkan terima kasih sebelum meninggalkan meja makan.',
          '离开 餐桌 前 记得 一定 要 说 声 谢谢。',
          'せき を たつ まえ に ごちそうさま を いいましょう。',
          '식탁에서 일어나기 전에 꼭 감사 인사를 전하는 것을 기억해요.'
        ),
        makeBundle(
          'Could you please pass that clean cloth napkin to me?',
          '¿Me podrías pasar esa servilleta limpia de tela hoy?',
          'کیا آپ مجھے وہ کپڑے کا صاف نیپکن دیں گے؟',
          'क्या आप मुझे वह कपड़े का साफ नैपकिन देंगे?',
          'هل يمكنك تمرير منديل القماش النظيف هذا إلي رجاءً؟',
          'Pourriez-vous me passer cette serviette en tissu propre ?',
          'Könntest du mir bitte diese saubere Stoffserviette geben?',
          'Potresti passarmi quel tovagliolo di stoffa pulito per favore?',
          'Você poderia me passar aquele guardanapo de pano limpo?',
          'Не мог бы ты передать мне эту чистую салфетку?',
          'O temiz kumaş peçeteyi bana uzatabilir misiniz lütfen?',
          'Bisakah Anda mengoperkan serbet kain bersih itu kepada saya?',
          '请问 你 可以 帮我 递 那块 干净 餐巾 吗？',
          'その きれいな ナプキン を わたして もらえますか？',
          '그 깨끗한 천 냅킨을 저에게 건네주실 수 있나요?'
        ),
        makeBundle(
          'Healthy morning habits help us thrive throughout our busy day.',
          'Los hábitos saludables matutinos nos ayudan todo el día.',
          'صبح کی صحت مند عادات پورے دن ہمیں توانا رکھتی ہیں۔',
          'सुबह की स्वस्थ आदतें पूरे दिन सक्रिय रहने में मदद।',
          'العادات الصباحية الصحية تمنحنا الحيوية طوال اليوم الحافل.',
          'Les bonnes habitudes du matin nous aident toute la journée.',
          'Gesunde Gewohnheiten am Morgen helfen uns den ganzen Tag.',
          'Le sane abitudini mattutine ci aiutano per tutta la giornata.',
          'Hábitos matinais saudáveis nos ajudam ao longo de todo dia.',
          'Здоровые утренние привычки помогают нам быть активными весь день.',
          'Sağlıklı sabah alışkanlıkları gün boyunca zinde kalmamıza yardım eder.',
          'Kebiasaan pagi yang sehat membantu kita bersemangat sepanjang hari.',
          '健康的 晨间 习惯 帮助 我们 活力 充沛 度过 全天。',
          'あさ の よい しゅうかん は いちにち を 元気 にします。',
          '건강한 아침 습관은 하루 종일 활기차게 보낼 수 있도록 도와줘요.'
        ),
      ],
    },
  },
};

// Persona-differentiated canonical datasets: guarantees [ageGroup, level] permutations are strictly disjoint
const CANONICAL_PERSONA_DATA: Record<string, Record<number, PhraseBundle[]>> = {
  '7-9_Beginner': {
    4: [
      makeBundle(
        'I want warm toast.',
        'Quiero pan tostado caliente.',
        'مجھے گرم ٹوسٹ چاہیے۔',
        'मुझे गरम टोस्ट चाहिए।',
        'أريد خبزاً محمصاً دافئاً.',
        'Je veux pain chaud.',
        'Ich möchte warmen Toast.',
        'Voglio pane tostato caldo.',
        'Quero pão torrado quente.',
        'Я хочу тёплый тост.',
        'Sıcak kızarmış tost istiyorum.',
        'Saya mau roti hangat.',
        '我 想要 热 吐司。',
        'あたたかい パン が ほしい。',
        '따뜻한 토스트를 원해요.',
        { ur: 'Mujhe garam toast chahiye.', es: 'Kyeh-roh pahn tohs-TAH-doh kah-LYEHN-teh' }
      ),
      makeBundle(
        'Please pour fresh milk.',
        'Sirve leche fresca porfavor.',
        'براہ کرم تازہ دودھ ڈالیں۔',
        'कृपया ताजा दूध डालिए।',
        'اسكب الحليب الطازج فضلاً.',
        'Verse du lait frais.',
        'Schenke frische Milch ein.',
        'Versa il latte fresco.',
        'Por favor sirva leite.',
        'Налей пожалуйста свежее молоко.',
        'Lütfen taze süt koy.',
        'Tolong tuang susu segar.',
        '请 倒 新鲜 牛奶。',
        'しんせん ミルク を ください。',
        '신선한 우유를 부어주세요.',
        { ur: 'Barahe karam taaza doodh daalein.', es: 'SEER-veh LEH-cheh FREHS-kah pohr-fah-vohr' }
      ),
      makeBundle(
        'Pass the sweet honey.',
        'Pásame la miel dulce.',
        'میٹھا شہد ادھر بڑھائیں۔',
        'मीठा शहद इधर दीजिए।',
        'ناولني هذا العسل اللذيذ.',
        'Passe le miel doux.',
        'Reiche den süßen Honig.',
        'Passami il miele dolce.',
        'Passe o mel doce.',
        'Передай сладкий ароматный мёд.',
        'Tatlı balı uzat lütfen.',
        'Operkan madu manis itu.',
        '请 递给 我 蜂蜜。',
        'あまい はちみつ を ください。',
        '달콤한 꿀을 건네주세요.',
        { ur: 'Meetha shehad idhar barhaein.', es: 'PAH-sah-meh lah myehl DOOL-seh' }
      ),
    ],
  },
  '10-12_Beginner': {
    4: [
      makeBundle(
        'Pass me the toast.',
        'Pásame el pan tostado.',
        'ٹوسٹ ادھر بڑھائیں۔',
        'टोस्ट इधर दीजिए।',
        'مرر لي الخبز المحمص.',
        'Passe-moi le pain grillé.',
        'Reiche mir den Toast.',
        'Passami il pane tostato.',
        'Passe-me o pão torrado.',
        'Передай мне этот тост.',
        'Tostu bana uzat lütfen.',
        'Operkan roti panggang itu.',
        '把 烤面包 递给我。',
        'トースト を とって ください。',
        '토스트를 건네주세요.',
        { ur: 'Toast idhar barhaein.' }
      ),
      makeBundle(
        'I need more milk.',
        'Necesito más leche fresca.',
        'مجھے مزید دودھ چاہیے۔',
        'मुझे और दूध चाहिए।',
        'أحتاج مزيداً من الحليب.',
        'J\'ai besoin de lait.',
        'Ich brauche mehr Milch.',
        'Ho bisogno di latte.',
        'Preciso de mais leite.',
        'Мне нужно ещё молока.',
        'Daha fazla süt lazım.',
        'Saya butuh susu lagi.',
        '我 需要 更多 牛奶。',
        'ミルク が もっと ひつよう。',
        '우유가 더 필요해요.',
        { ur: 'Mujhe mazeed doodh chahiye.' }
      ),
      makeBundle(
        'Breakfast smells very good.',
        'El desayuno huele rico.',
        'ناشتے کی خوشبو عمدہ ہے۔',
        'नाश्ता बहुत अच्छा महकता।',
        'الإفطار رائحته طيبة جداً.',
        'Le déjeuner sent bon.',
        'Das Frühstück riecht herrlich.',
        'La colazione profuma bene.',
        'O café cheira bem.',
        'Завтрак пахнет очень вкусно.',
        'Kahvaltı çok güzel kokuyor.',
        'Sarapan ini berbau lezat.',
        '早餐 闻起来 特别 香。',
        'あさごはん の いい におい。',
        '아침 식사 냄새가 좋아요.',
        { ur: 'Nashtay ki khushboo umdah hai.' }
      ),
    ],
  },
  '13-16_Beginner': {
    4: [
      makeBundle(
        'I grab quick toast.',
        'Tomo una tostada rápida.',
        'میں جلدی ٹوسٹ لیتا ہوں۔',
        'मैं जल्दी टोस्ट लेता।',
        'أتناول خبزاً محمّصاً سريعاً.',
        'Je prends toast rapide.',
        'Ich nehme schnellen Toast.',
        'Prendo un toast veloce.',
        'Pego uma torrada rápida.',
        'Я быстро перекушу тостом.',
        'Hızlıca bir tost alıyorum.',
        'Saya ambil roti cepat.',
        '我 快速 拿了 吐司。',
        'すばやく トースト を たべる。',
        '간단히 토스트를 먹어요.',
        { ur: 'Main jaldi toast leta hoon.' }
      ),
      makeBundle(
        'Pass the fruit juice.',
        'Pásame el jugo natural.',
        'پھلوں کا جوس بڑھائیں۔',
        'फलों का जूस दीजिए।',
        'مرر عصير الفواكه لي.',
        'Passe le jus fruits.',
        'Reiche den Fruchtsaft herüber.',
        'Passa il succo naturale.',
        'Passe o suco natural.',
        'Передай пожалуйста фруктовый сок.',
        'Meyve suyunu bana uzat.',
        'Operkan jus buah segar.',
        '把 水果 汁 递给我。',
        'フルーツ ジュース を ください。',
        '과일 주스를 건네주세요.',
        { ur: 'Phalon ka juice barhaein.' }
      ),
      makeBundle(
        'Morning starts with breakfast.',
        'La mañana empieza desayunando.',
        'صبح کا آغاز ناشتے سے ہے۔',
        'सुबह की शुरुआत नाश्ते से।',
        'يبدأ الصباح دائماً بالفطور.',
        'Le matin commence déjeuner.',
        'Der Morgen beginnt frühstückend.',
        'La mattina comincia mangiando.',
        'A manhã começa comendo.',
        'Утро начинается с завтрака.',
        'Sabah güzel kahvaltıyla başlar.',
        'Pagi dimulai dengan sarapan.',
        '美好 早晨 始于 早餐。',
        'あさは ごはん から はじまる。',
        '아침은 식사로 시작해요.',
        { ur: 'Subah ka aaghaaz nashtay se hai.' }
      ),
    ],
  },
  '7-9_Intermediate': {
    4: [
      makeBundle(
        'I enjoy warm toast.',
        'Disfruto del pan caliente.',
        'مجھے گرم ٹوسٹ پسند ہے۔',
        'मुझे गरम टोस्ट पसंद है।',
        'أستمتع بتناول الخبز الدافئ.',
        'J\'apprécie le pain chaud.',
        'Ich genieße warmen Toast.',
        'Mi piace pane caldo.',
        'Aprecio o pão quente.',
        'Я наслаждаюсь тёплым тостом.',
        'Sıcak tostun tadını çıkarırım.',
        'Saya menikmati roti hangat.',
        '我 喜欢 享用 热吐司。',
        'あたたかい トースト が すき。',
        '따뜻한 토스트를 즐겨요.',
        { ur: 'Mujhe garam toast pasand hai.' }
      ),
      makeBundle(
        'Please pass the butter.',
        'Por favor pasa mantequilla.',
        'براہ کرم مکھن ادھر دیں۔',
        'कृपया मक्खन इधर दीजिए।',
        'مرر لي الزبدة رجاءً.',
        'Passe le beurre s\'il-te-plaît.',
        'Reiche bitte die Butter.',
        'Passa il burro per favore.',
        'Por favor passe manteiga.',
        'Передай пожалуйста сливочное масло.',
        'Lütfen tereyağını bana uzat.',
        'Tolong operkan mentega itu.',
        '请 把 黄油 递给我。',
        'バター を とって ください。',
        '버터를 건네주세요 부탁해요.',
        { ur: 'Barahe karam makhan idhar dein.' }
      ),
      makeBundle(
        'Drink all your milk.',
        'Toma toda tu leche.',
        'اپنا سارا دودھ پیئیں۔',
        'अपना पूरा दूध पिएं।',
        'اشرب حليبك كله الآن.',
        'Bois tout ton lait.',
        'Trink deine ganze Milch.',
        'Bevi tutto il latte.',
        'Beba todo seu leite.',
        'Допей всё своё молоко.',
        'Sütünün hepsini bitir lütfen.',
        'Minum habis susu kamu.',
        '喝完 你的 全部 牛奶。',
        'ミルク を ぜんぶ のんで。',
        '우유를 남김없이 다 마셔요.',
        { ur: 'Apna saara doodh peeyein.' }
      ),
    ],
  },
  '7-9_Advanced': {
    4: [
      makeBundle(
        'Breakfast is ready now.',
        'El desayuno está listo.',
        'ناشتہ اب تیار ہے۔',
        'नाश्ता अब तैयार है।',
        'وجبة الإفطار جاهزة الآن.',
        'Le petit-déjeuner est prêt.',
        'Das Frühstück ist fertig.',
        'La colazione è pronta.',
        'O café está pronto.',
        'Завтрак уже полностью готов.',
        'Kahvaltı şimdi tamamen hazır.',
        'Sarapan sekarang sudah siap.',
        '早餐 此时 已经 准备就绪。',
        'あさごはん の よういが できた。',
        '아침 식사가 준비되었습니다.',
        { ur: 'Nashta ab tayyar hai.' }
      ),
      makeBundle(
        'Pass the fresh toast.',
        'Pasa la tostada fresca.',
        'تازہ ٹوسٹ آگے بڑھائیں۔',
        'ताजा टोस्ट आगे बढ़ाइए।',
        'مرر لي التوست الطازج.',
        'Passe le toast frais.',
        'Reiche den frischen Toast.',
        'Passa il toast fresco.',
        'Passe a torrada fresca.',
        'Передай свежий хрустящий тост.',
        'Taze tostu uzat lütfen.',
        'Operkan roti panggang segar.',
        '递上 新鲜 烤 面包。',
        'やきたて トースト を ちょうだい。',
        '신선한 토스트를 건네주세요.',
        { ur: 'Taaza toast aagay barhaein.' }
      ),
      makeBundle(
        'Pour some orange juice.',
        'Sirve algo de jugo.',
        'تھوڑا اورنج جوس ڈالیں۔',
        'थोड़ा संतरे का जूस डालिए।',
        'اسكب بعض عصير البرتقال.',
        'Verse du jus d\'orange.',
        'Schenke etwas Orangensaft ein.',
        'Versa del succo d\'arancia.',
        'Sirva um pouco de suco.',
        'Налей немного апельсинового сока.',
        'Biraz portakal suyu koy.',
        'Tuangkan sedikit jus jeruk.',
        '倒 一些 橙汁 出来。',
        'オレンジ ジュース を ついで。',
        '오렌지 주스를 조금 따라주세요.',
        { ur: 'Thora orange juice daalein.' }
      ),
    ],
  },
};

// ============================================================================
// DYNAMIC ALGORITHMIC SYNTHESIS FOR ALL 77 TOPICS & 15 CATEGORIES
// ============================================================================

// Multi-lingual vocabulary for synthesis across all categories
const THEMATIC_OBJECT_DICTIONARY: Record<string, { en: string; es: string; ur: string; hi: string; ar: string; fr: string; de: string; it: string; pt: string; ru: string; tr: string; id: string; zh: string; ja: string; ko: string }> = {
  // Family
  'family-hug': { en: 'warm hug', es: 'abrazo cariñoso', ur: 'پیار بھرا گلے لگانا', hi: 'प्यारा सा गले लगना', ar: 'عناق دافئ', fr: 'câlin chaleureux', de: 'warme Umarmung', it: 'abbraccio caloroso', pt: 'abraço carinhoso', ru: 'тёплые объятия', tr: 'sıcak kucaklaşma', id: 'pelukan hangat', zh: '温暖的拥抱', ja: 'あたたかいハグ', ko: '따뜻한 포옹' },
  'kind-words': { en: 'kind words', es: 'palabras amables', ur: 'شیریں الفاظ', hi: 'मीठे बोल', ar: 'كلمات لطيفة', fr: 'mots doux', de: 'freundliche Worte', it: 'parole gentili', pt: 'palavras gentis', ru: 'добрые слова', tr: 'nazik sözler', id: 'kata-kata ramah', zh: '亲切的话语', ja: 'やさしいことば', ko: '다정한 말' },
  // Travel
  'bus-ticket': { en: 'bus ticket', es: 'boleto de autobús', ur: 'بس کا ٹکٹ', hi: 'बस का टिकट', ar: 'تذكرة الحافلة', fr: 'billet de bus', de: 'Busfahrkarte', it: 'biglietto dell\'autobus', pt: 'passagem de ônibus', ru: 'билет на автобус', tr: 'otobüs bileti', id: 'tiket bus', zh: '公交车票', ja: 'バスのきっぷ', ko: '버스 티켓' },
  'train-seat': { en: 'train seat', es: 'asiento de tren', ur: 'ٹرین کی سیٹ', hi: 'ट्रेन की सीट', ar: 'مقعد القطار', fr: 'siège de train', de: 'Zugsitzplatz', it: 'posto in treno', pt: 'assento do trem', ru: 'место в поезде', tr: 'tren koltuğu', id: 'kursi kereta', zh: '火车座位', ja: 'れっしゃのせき', ko: '기차 좌석' },
  // Shopping
  'apple-basket': { en: 'red apples', es: 'manzanas rojas', ur: 'سرخ سیب', hi: 'लाल सेब', ar: 'تفاح أحمر', fr: 'pommes rouges', de: 'rote Äpfel', it: 'mele rosse', pt: 'maçãs vermelhas', ru: 'красные яблоки', tr: 'kırmızı elmalar', id: 'apel merah', zh: '红苹果', ja: 'あかいりんご', ko: '빨간 사과' },
  'fresh-bread': { en: 'fresh bread', es: 'pan recién horneado', ur: 'تازہ پکی روٹی', hi: 'ताजा बेक ब्रेड', ar: 'خبز طازج', fr: 'pain frais', de: 'frisches Brot', it: 'pane fresco', pt: 'pão fresco', ru: 'свежий хлеб', tr: 'taze ekmek', id: 'roti segar', zh: '新鲜面包', ja: 'やきたてパン', ko: '갓 구운 빵' },
  // Health
  'warm-tea': { en: 'warm tea', es: 'té caliente', ur: 'گرم چائے', hi: 'गरम चाय', ar: 'شاي دافئ', fr: 'thé chaud', de: 'warmer Tee', it: 'tè caldo', pt: 'chá quentinho', ru: 'горячий чай', tr: 'sıcak çay', id: 'teh hangat', zh: '温热的茶', ja: 'あたたかいおちゃ', ko: '따뜻한 차' },
  'clean-bandage': { en: 'clean bandage', es: 'vendaje limpio', ur: 'صاف پٹی', hi: 'साफ पट्टी', ar: 'ضمادة نظيفة', fr: 'pansement propre', de: 'sauberer Verband', it: 'benda pulita', pt: 'curativo limpo', ru: 'чистый бинт', tr: 'temiz bandaj', id: 'perban bersih', zh: '干净创可贴', ja: 'きれいなばんそうこう', ko: '깨끗한 반창고' },
  // School
  'reading-book': { en: 'story book', es: 'libro de cuentos', ur: 'کہانی کی کتاب', hi: 'कहानी की किताब', ar: 'كتاب القصص', fr: 'livre d\'histoires', de: 'Geschichtenbuch', it: 'libro di favole', pt: 'livro de histórias', ru: 'книга сказок', tr: 'hikaye kitabı', id: 'buku cerita', zh: '精彩故事书', ja: 'おはなしのほん', ko: '재미있는 이야기책' },
  'blue-pencil': { en: 'sharp pencil', es: 'lápiz afilado', ur: 'تیز پنسل', hi: 'नुकीली पेंसिल', ar: 'قلم رصاص مبشور', fr: 'crayon taillé', de: 'spitzer Bleistift', it: 'matita appuntita', pt: 'lápis apontado', ru: 'острый карандаш', tr: 'sivri kalem', id: 'pensil runcing', zh: '削好的铅笔', ja: 'えんぴつ', ko: '뾰족한 연필' },
  // Play
  'yellow-ball': { en: 'bouncy ball', es: 'pelota saltarina', ur: 'اچھلتی گیند', hi: 'उछलती गेंद', ar: 'كرة نطاطة', fr: 'balle bondissante', de: 'Springball', it: 'palla rimbalzante', pt: 'bola saltitante', ru: 'прыгучий мячик', tr: 'zıpzıp top', id: 'bola memantul', zh: '弹力球', ja: 'ボール', ko: '탱탱볼' },
  'building-blocks': { en: 'color blocks', es: 'bloques de colores', ur: 'رنگ برنگے بلاکس', hi: 'रंगीन ब्लॉक्स', ar: 'مكعبات ملونة', fr: 'blocs colorés', de: 'bunte Bausteine', it: 'blocchi colorati', pt: 'blocos coloridos', ru: 'цветные кубики', tr: 'renkli bloklar', id: 'balok warna', zh: '彩色积木', ja: 'つみき', ko: '알록달록 블록' },
  // Nature
  'green-leaf': { en: 'green leaf', es: 'hoja verde', ur: 'سبز پتا', hi: 'हरा पत्ता', ar: 'ورقة خضراء', fr: 'feuille verte', de: 'grünes Blatt', it: 'foglia verde', pt: 'folha verde', ru: 'зелёный лист', tr: 'yeşil yaprak', id: 'daun hijau', zh: '碧绿树叶', ja: 'みどりの葉', ko: '초록 나뭇잎' },
  'bright-flower': { en: 'blooming flower', es: 'flor floreciente', ur: 'کھلا ہوا پھول', hi: 'खिलता हुआ फूल', ar: 'زهرة متفتحة', fr: 'fleur épanouie', de: 'blühende Blume', it: 'fiore sbocciato', pt: 'flor desabrochando', ru: 'цветущий цветок', tr: 'açan çiçek', id: 'bunga mekar', zh: '盛开的花朵', ja: 'さいたお花', ko: '활짝 핀 꽃' },
};

// Dedicated Day 11 canonical dialogue per ageGroup and level permutation
const BREAKFAST_DEDICATED_DAY11: Record<string, PhraseBundle[]> = {
  '7-9__Beginner': [
    makeBundle(
      'I want warm toast.',
      'Quiero pan tostado caliente.',
      'مجھے گرم ٹوسٹ چاہیے۔',
      'मुझे गरम टोस्ट चाहिए।',
      'أريد خبزاً محمصاً دافئاً.',
      'Je veux pain chaud.',
      'Ich möchte warmen Toast.',
      'Voglio pane tostato caldo.',
      'Quero pão torrado quente.',
      'Я хочу тёплый тост.',
      'Sıcak kızarmış tost istiyorum.',
      'Saya mau roti hangat.',
      '我 想要 热 吐司。',
      'あたたかい パン が ほしい。',
      '따뜻한 토스트를 원해요.',
      { ur: 'Mujhe garam toast chahiye.', es: 'Kyeh-roh pahn tohs-TAH-doh kah-LYEHN-teh' }
    ),
    makeBundle(
      'Please pour fresh milk.',
      'Sirve leche fresca porfavor.',
      'براہ کرم تازہ دودھ ڈالیں۔',
      'कृपया ताजा दूध डालिए।',
      'اسكب الحليب الطازج فضلاً.',
      'Verse du lait frais.',
      'Schenke frische Milch ein.',
      'Versa il latte fresco.',
      'Por favor sirva leite.',
      'Налей пожалуйста свежее молоко.',
      'Lütfen taze süt koy.',
      'Tolong tuang susu segar.',
      '请 倒 新鲜 牛奶。',
      'しんせん ミルク を ください。',
      '신선한 우유를 부어주세요.',
      { ur: 'Barahe karam taaza doodh daalein.', es: 'SEER-veh LEH-cheh FREHS-kah pohr-fah-vohr' }
    ),
    makeBundle(
      'Pass the butter knife.',
      'Pásame el cuchillo mantequilla.',
      'مکھن والی چھری دیں۔',
      'मक्खन वाली छुरी दीजिए।',
      'مرر سكين الزبدة لي.',
      'Passe le couteau beurre.',
      'Reiche das Buttermesser herüber.',
      'Passami il coltello burro.',
      'Passe a faca manteiga.',
      'Передай мне нож масло.',
      'Tereyağı bıçağını uzat lütfen.',
      'Operkan pisau mentega itu.',
      '请 递给 我 黄油刀。',
      'バター ナイフ を ください。',
      '버터 나이프를 건네주세요.',
      { ur: 'Makkhan wali chhuri dein.', es: 'PAH-sah-meh ehl koo-CHEE-yoh mahn-teh-KEE-yah' }
    ),
  ],
  '7-9__Intermediate': [
    makeBundle(
      'May I have juice?',
      '¿Puedo tomar jugo fresco?',
      'کیا مجھے جوس ملے گا؟',
      'क्या मुझे जूस मिलेगा?',
      'هل يمكنني تناول العصير؟',
      'Puis-je avoir du jus?',
      'Darf ich Saft haben?',
      'Posso avere del succo?',
      'Posso tomar um suco?',
      'Можно мне немного сока?',
      'Meyve suyu alabilir miyim?',
      'Bolehkah saya minta jus?',
      '我 可以 喝果汁 吗？',
      'ジュース を もらえますか？',
      '주스 마셔도 될까요?',
      { ur: 'Kya mujhe juice mile ga?' }
    ),
    makeBundle(
      'Let us share toast.',
      'Compartamos pan tostado rico.',
      'آئیں گرم ٹوسٹ بانٹیں۔',
      'आएं गरम टोस्ट बांटें।',
      'دعنا نتشارك الخبز المحمص.',
      'Partageons le pain grillé.',
      'Teilen wir den Toast.',
      'Condividiamo il pane tostato.',
      'Vamos compartilhar o pão.',
      'Давай разделим вкусный тост.',
      'Tostu birlikte paylaşalım hadi.',
      'Ayo kita berbagi roti.',
      '我们 一起 分享 吐司。',
      'トースト を わけあおう。',
      '토스트를 함께 나눠 먹어요.',
      { ur: 'Aayein garam toast baantein.' }
    ),
    makeBundle(
      'We love breakfast together.',
      'Nos encanta desayunar juntos.',
      'ہمیں ساتھ ناشتہ پسند ہے۔',
      'हमें साथ नाश्ता पसंद है।',
      'نحب تناول الفطور معاً.',
      'Nous aimons déjeuner ensemble.',
      'Wir lieben gemeinsames Frühstücken.',
      'Amiamo fare colazione insieme.',
      'Adoramos tomar café juntos.',
      'Мы любим завтракать вместе.',
      'Birlikte kahvaltı yapmayı severiz.',
      'Kami suka sarapan bersama.',
      '我们 喜欢 一起 吃早餐。',
      'みんなで あさごはん がすき。',
      '함께 아침 먹는것을 좋아해요.',
      { ur: 'Humein saath nashta pasand hai.' }
    ),
  ],
  '7-9__Advanced': [
    makeBundle(
      'Could you pass the butter?',
      '¿Podrías pasarme la mantequilla fresca?',
      'کیا آپ مکھن ادھر دیں گے؟',
      'क्या आप मक्खन इधर देंगे?',
      'هل يمكنك تمرير الزبدة لي؟',
      'Pourriez-vous me passer le beurre?',
      'Könntest du mir die Butter reichen?',
      'Potresti passarmi il burro fresco?',
      'Você poderia me passar a manteiga?',
      'Не мог бы ты передать масло?',
      'Tereyağını bana uzatabilir misiniz lütfen?',
      'Bisakah Anda mengoperkan mentega itu?',
      '你可以 把 黄油 递给我吗？',
      'バター を とって もらえますか？',
      '버터를 저에게 건네주시겠어요?',
      { ur: 'Kya aap makkhan idhar dein ge?' }
    ),
    makeBundle(
      'I really enjoy warm pancakes.',
      'Realmente disfruto los panqueques calientes.',
      'مجھے واقعی گرم پین کیک پسند ہیں۔',
      'मुझे सचमुच गरम पैनकेक पसंद हैं।',
      'أستمتع حقاً بتناول الفطائر الدافئة.',
      'J\'apprécie vraiment les crêpes chaudes.',
      'Ich genieße warme Pfannkuchen sehr.',
      'Mi piacciono molto i pancake caldi.',
      'Eu realmente aprecio panquecas quentes.',
      'Мне очень нравятся тёплые блинчики.',
      'Sıcak krepleri gerçekten çok severim.',
      'Saya sangat menikmati panekuk hangat.',
      '我 非常 喜欢 热 煎饼。',
      'あたたかい パンケーキ が だいすき。',
      '따뜻한 팬케이크를 정말 좋아해요.',
      { ur: 'Mujhe waqai garam pancake pasand hain.' }
    ),
    makeBundle(
      'Let us make breakfast now.',
      'Preparemos un desayuno delicioso juntos.',
      'آئیں اب ہم ناشتہ بنائیں۔',
      'आएं अब हम नाश्ता बनाएं।',
      'دعنا نعد وجبة الفطور الآن.',
      'Préparons le petit déjeuner maintenant.',
      'Lasst uns jetzt das Frühstück zubereiten.',
      'Prepariamo la colazione adesso insieme.',
      'Vamos preparar o café da manhã agora.',
      'Давай приготовим вкусный завтрак сейчас.',
      'Hadi şimdi kahvaltıyı hazırlayalım birlikte.',
      'Mari kita siapkan sarapan sekarang.',
      '让我们 现在 一起 做 早餐。',
      'いますぐ あさごはん を つくろう。',
      '지금 함께 아침을 만들어 봐요.',
      { ur: 'Aayein ab hum nashta banayein.' }
    ),
  ],
  '10-12__Beginner': [
    makeBundle(
      'Can I toast bread?',
      '¿Puedo tostar el pan?',
      'کیا میں ڈبل روٹی سینکوں؟',
      'क्या मैं डबल रोटी सेंकूं?',
      'هل يمكنني تحميص الخبز؟',
      'Puis-je griller le pain?',
      'Kann ich Brot toasten?',
      'Posso tostare il pane?',
      'Posso torrar o pão?',
      'Могу я поджарить хлеб?',
      'Ekmeği kızartabilir miyim ben?',
      'Bolehkah saya memanggang roti?',
      '我 可以 烤 面包吗？',
      'パン を やいてもいい？',
      '제가 빵을 구워도 될까요?',
      { ur: 'Kya main double roti seenkoun?' }
    ),
    makeBundle(
      'Pour the cold juice.',
      'Sirve el jugo frío.',
      'ٹھنڈا جوس گلاس میں ڈالیں۔',
      'ठंडा जूस गिलास में डालिए।',
      'اسكب هذا العصير البارد.',
      'Verse le jus frais.',
      'Gieße den kalten Saft.',
      'Versa il succo freddo.',
      'Sirva o suco gelado.',
      'Налей этот холодный сок.',
      'Soğuk meyve suyunu koy.',
      'Tuangkan jus dingin itu.',
      '把 冷 果汁 倒出来。',
      'つめたい ジュース を そそごう。',
      '시원한 주스를 잔에 따라주세요.',
      { ur: 'Thanda juice glass mein dalein.' }
    ),
    makeBundle(
      'Help me set plates.',
      'Ayúdame a poner platos.',
      'پلیٹیں لگانے میں مدد کریں۔',
      'प्लेटें लगाने में मदद करें।',
      'ساعدني في ترتيب الأطباق.',
      'Aide-moi pour les assiettes.',
      'Hilf mir Teller aufzustellen.',
      'Aiutami a mettere piatti.',
      'Ajude a arrumar pratos.',
      'Помоги мне расставить тарелки.',
      'Tabakları dizmeme yardım et.',
      'Bantu saya menata piring.',
      '帮我 一起 摆 放盘子。',
      'おさら を ならべるの てつだって。',
      '접시 차리는 것을 도와주세요.',
      { ur: 'Platein lagane mein madad karein.' }
    ),
  ],
  '10-12__Intermediate': [
    makeBundle(
      'I will make morning toast.',
      'Prepararé pan tostado esta mañana.',
      'میں صبح کا ٹوسٹ بناؤں گا۔',
      'मैं सुबह का टोस्ट बनाऊंगा।',
      'سأقوم بإعداد الخبز المحمص الصباحي.',
      'Je préparerai le toast ce matin.',
      'Ich werde den Morgentoast zubereiten.',
      'Preparerò il pane tostato stamattina.',
      'Eu vou fazer torradas matinais.',
      'Я приготовлю утренний хрустящий тост.',
      'Sabah tostunu ben yapacağım bugün.',
      'Saya akan membuat roti panggang pagi.',
      '我 今早 会 烤 吐司。',
      'あさ の トースト を つくるね。',
      '제가 아침 토스트를 만들게요 오늘.',
      { ur: 'Main subah ka toast banaoun ga.' }
    ),
    makeBundle(
      'Could you slice the apples?',
      '¿Podrías rebanar las manzanas frescas?',
      'کیا آپ سیب کاٹ سکتے ہیں؟',
      'क्या आप सेब काट सकते हैं?',
      'هل يمكنك تقطيع التفاح الطازج؟',
      'Pourriez-vous couper les pommes fraîches?',
      'Könntest du bitte die Äpfel schneiden?',
      'Potresti affettare le mele fresche adesso?',
      'Você poderia fatiar as maçãs frescas?',
      'Не мог бы ты нарезать яблоки?',
      'Elmaları dilimleyebilir misiniz lütfen şimdi?',
      'Bisakah Anda memotong apel-apel segar itu?',
      '你可以 切 一下 苹果吗？',
      'りんご を きって もらえますか？',
      '사과를 먹기 좋게 썰어주시겠어요?',
      { ur: 'Kya aap saib kaat sakte hain?' }
    ),
    makeBundle(
      'Let us drink fresh juice.',
      'Bebamos jugo recién exprimido juntos.',
      'آئیں تازہ جوس مل کر پئیں۔',
      'आएं ताजा जूस मिलकर पिएं।',
      'دعنا نشرب العصير الطازج معاً.',
      'Buvons du jus frais ensemble.',
      'Trinken wir gemeinsam frischen Saft.',
      'Beviamo insieme della spremuta fresca.',
      'Vamos beber suco fresco juntos.',
      'Давай выпьем свежего сока вместе.',
      'Birlikte taze sıkılmış meyve suyu içelim.',
      'Ayo kita minum jus segar bersama.',
      '让我们 一起 喝 新鲜果汁。',
      'しんせん な ジュース を のもう。',
      '신선한 주스를 함께 마셔요 지금.',
      { ur: 'Aayein taaza juice mil kar peeyein.' }
    ),
  ],
  '10-12__Advanced': [
    makeBundle(
      'Would you prefer wheat or sourdough?',
      '¿Prefieres pan integral o masa madre?',
      'کیا آپ گندم یا کھٹا ٹوسٹ پسند کریں گے؟',
      'क्या आप गेहूं या खट्टा टोस्ट पसंद करेंगे?',
      'هل تفضل خبز القمح أم المخمر؟',
      'Préfères-tu le pain complet ou levain?',
      'Bevorzugst du Weizenbrot oder feines Sauerteigbrot?',
      'Preferisci pane integrale o a lievitazione?',
      'Você prefere pão integral ou fermentado?',
      'Ты предпочитаешь пшеничный хлеб или закваску?',
      'Tam buğday mı ekşi mayalı mı istersin?',
      'Apakah Anda lebih suka roti gandum utuh?',
      '你 更 喜欢 全麦 还是 酸酵面包？',
      'ぜんまい パン と ライぎ パン どっち？',
      '통밀빵과 사워도우 중 어떤 걸 원하세요?',
      { ur: 'Kya aap gandum ya khatta toast pasand karein ge?' }
    ),
    makeBundle(
      'I prepared a healthy breakfast bowl.',
      'Preparé un tazón de desayuno saludable.',
      'میں نے ایک صحت بخش ناشتہ تیار کیا۔',
      'मैंने एक सेहतमंद नाश्ता तैयार किया।',
      'لقد أعددت وعاء إفطار صحياً متوازناً.',
      'J\'ai préparé un bol déjeuner équilibré.',
      'Ich habe eine gesunde Frühstücksschüssel zubereitet.',
      'Ho preparato una ciotola sana stamattina.',
      'Eu preparei uma tigela matinal saudável.',
      'Я приготовил полезную тарелку питательного завтрака.',
      'Herkes için sağlıklı bir kahvaltı kasesi hazırladım.',
      'Saya menyiapkan semangkuk sarapan yang sangat sehat.',
      '我 准备了 一份 健康的 早餐碗。',
      'ヘルシー な あさごはん ボウル を つくったよ。',
      '건강하고 맛있는 아침 식사 볼을 준비했어요.',
      { ur: 'Main ne aik sehat bakhsh nashta tayyar kiya.' }
    ),
    makeBundle(
      'Could you pass me the jam?',
      '¿Podrías pasarme la mermelada de frutas?',
      'کیا آپ جام ادھر دے سکتے ہیں؟',
      'क्या आप जैम इधर दे सकते हैं?',
      'هل يمكنك تمرير مربى الفاكهة لي؟',
      'Pourriez-vous me passer la confiture fruit?',
      'Könntest du mir bitte die Marmelade reichen?',
      'Potresti passarmi la deliziosa marmellata dolce?',
      'Você poderia passar a geleia de frutas?',
      'Не мог бы ты передать мне варенье?',
      'Meyve reçelini bana uzatabilir misiniz lütfen?',
      'Bisakah Anda mengoperkan selai buah itu padaku?',
      '你可以 把 果酱 递给我 吗？',
      'ジャム を こちら に とって もらえますか？',
      '과일 잼을 저에게 건네주실 수 있나요?',
      { ur: 'Kya aap jam idhar de sakte hain?' }
    ),
  ],
  '13-16__Beginner': [
    makeBundle(
      'I need morning breakfast.',
      'Necesito un buen desayuno matutino.',
      'مجھے صبح کا ناشتہ چاہیے۔',
      'मुझे सुबह का नाश्ता चाहिए।',
      'أحتاج إلى وجبة إفطار صباحية.',
      'J\'ai besoin d\'un bon petit-déjeuner.',
      'Ich brauche ein ordentliches Frühstück.',
      'Ho bisogno di fare colazione stamattina.',
      'Preciso de um bom café matinal.',
      'Мне нужен хороший утренний завтрак.',
      'Benim sabah kahvaltısına ihtiyacım var.',
      'Saya butuh sarapan pagi yang baik.',
      '我 需要 吃 顿 早餐。',
      'しっかり あさごはん を たべたいな。',
      '저는 든든한 아침 식사가 필요해요.',
      { ur: 'Mujhe subah ka nashta chahiye.' }
    ),
    makeBundle(
      'Is breakfast ready now?',
      '¿Está listo el desayuno ahora?',
      'کیا اب ناشتہ تیار ہے؟',
      'क्या अब नाश्ता तैयार है?',
      'هل الفطور الصباحي جاهز الآن؟',
      'Le petit-déjeuner est-il prêt maintenant?',
      'Ist das Frühstück jetzt fertig zubereitet?',
      'La colazione è pronta adesso per noi?',
      'O café da manhã está pronto agora?',
      'Завтрак уже полностью готов для всех?',
      'Kahvaltı şu anda hazır mı acaba?',
      'Apakah sarapan sudah siap sekarang ini?',
      '早餐 现在 已经 准备好了 吗？',
      'あさごはん は もう できた の かな？',
      '아침 식사가 지금 다 준비되었나요?',
      { ur: 'Kya ab nashta tayyar hai?' }
    ),
    makeBundle(
      'Pass me the bread.',
      'Pásame el pan por favor.',
      'مجھے ڈبل روٹی پکڑا دیں۔',
      'मुझे डबल रोटी पकड़ा दीजिए।',
      'ناولني هذا الخبز من فضلك.',
      'Passe-moi le pain s\'il vous plaît.',
      'Reiche mir bitte das frische Brot.',
      'Passami il pane per favore subito.',
      'Passe o pão para mim porfavor.',
      'Передай мне хлеб пожалуйста сейчас.',
      'Ekmeği bana uzatır mısın lütfen?',
      'Tolong operkan roti itu kepada saya.',
      '把 面包 递给 我 一下。',
      'パン を こちら に ちょうだい。',
      '빵을 저에게 건네주시면 감사하겠습니다.',
      { ur: 'Mujhe double roti pakra dein.' }
    ),
  ],
  '13-16__Intermediate': [
    makeBundle(
      'I am making quick breakfast.',
      'Estoy preparando un desayuno rápido ahora.',
      'میں صبح کا جلدی ناشتہ بنا رہا ہوں۔',
      'मैं सुबह का जल्दी नाश्ता बना रहा हूँ।',
      'أقوم بإعداد وجبة إفطار سريعة الآن.',
      'Je prépare un petit déjeuner rapide.',
      'Ich mache ein schnelles leckeres Frühstück.',
      'Sto preparando una veloce colazione nutriente.',
      'Estou fazendo um café rápido agora.',
      'Я делаю быстрый и питательный завтрак.',
      'Hemen hızlı ve pratik kahvaltı hazırlıyorum.',
      'Saya sedang menyiapkan sarapan cepat sekarang.',
      '我 正在 准备 快速 早餐。',
      'てばやく あさごはん を つくって いるよ。',
      '간단하고 빠른 아침 식사를 만들고 있어요.',
      { ur: 'Main subah ka jaldi nashta bana raha hoon.' }
    ),
    makeBundle(
      'Could you pass the sourdough?',
      '¿Podrías pasarme el pan fermentado?',
      'کیا آپ خمیری ٹوسٹ ادھر دیں گے؟',
      'کیا آپ خمیری ٹوسٹ ادھر دیں گے؟',
      'هل يمكنك تمرير خبز العجين المخمر؟',
      'Pourriez-vous me passer le pain levain?',
      'Könntest du mir das Sauerteigbrot reichen?',
      'Potresti passarmi il pane a lievitazione?',
      'Você poderia passar o pão fermentado?',
      'Не мог бы ты передать закваску?',
      'Ekşi mayalı ekmeği uzatabilir misiniz lütfen?',
      'Bisakah Anda mengoperkan roti sourdough itu?',
      '你可以 递给 我 酸酵 面包吗？',
      'サワードウ ブレッド を とって もらえますか？',
      '사워도우 빵을 저에게 건네주시겠어요?',
      { ur: 'Kya aap khameeri toast idhar dein ge?' }
    ),
    makeBundle(
      'I will blend fresh smoothies.',
      'Prepararé batidos frescos para todos nosotros.',
      'میں سب کے لیے سمودھی بناؤں گا۔',
      'मैं सबके लिए स्मूदी बनाऊंगा।',
      'سأقوم بخلط العصائر الطازجة للجميع.',
      'Je vais mixer des smoothies frais.',
      'Ich werde frische Smoothies für uns mixen.',
      'Frullerò dei deliziosi frullati per tutti.',
      'Vou bater vitaminas frescas para todos.',
      'Я взобью свежие смузи для всех.',
      'Herkes için taze meyveli smoothie yapacağım.',
      'Saya akan memblender smoothie segar untuk kita.',
      '我 会 为 大家 调制 冰沙。',
      'みんな に フレッシュ スムージー を つくるね。',
      '모두를 위해 신선한 스무디를 만들어 줄게요.',
      { ur: 'Main sab ke liye smoothie banaoun ga.' }
    ),
  ],
  '13-16__Advanced': [
    makeBundle(
      'A balanced breakfast sharpens cognitive focus.',
      'Un desayuno equilibrado agudiza el enfoque.',
      'متوازن ناشتہ ذہنی توجہ کو تیز کرتا ہے۔',
      'संतुलित नाश्ता मानसिक एकाग्रता को तेज करता है।',
      'الإفطار المتوازن يعزز التركيز الذهني واليقظة.',
      'Un petit-déjeuner équilibré aiguise la concentration.',
      'Ein ausgewogenes Frühstück schärft die Konzentration.',
      'Una colazione equilibrata affina la concentrazione.',
      'Um café equilibrado aguça o foco mental.',
      'Сбалансированный завтрак значительно обостряет умственную концентрацию.',
      'Dengeli bir kahvaltı zihinsel odaklanmayı keskinleştirir.',
      'Sarapan seimbang mempertajam konsentrasi dan fokus mental.',
      '均衡的 早餐 能 提高 大脑 专注力。',
      'バランス の よい あさごはん は しゅうちゅうりょく を たかめます。',
      '균형 잡힌 아침 식사는 두뇌 집중력을 높여줍니다.',
      { ur: 'Mutawazin nashta zehni tawajjuh ko taiz karta hai.' }
    ),
    makeBundle(
      'Would you mind slicing the bread?',
      '¿Te importaría rebanar el pan tostado?',
      'کیا آپ ڈبل روٹی کاٹنے کی زحمت کریں گے؟',
      'क्या आप रोटी काटने की ज़हमत करेंगे?',
      'هل تمانع في تقطيع هذا الخبز الطازج؟',
      'Pourriez-vous trancher ce pain artisanal?',
      'Würde es dir etwas ausmachen das Brot zu schneiden?',
      'Ti dispiacerebbe affettare il pane fresco adesso?',
      'Você se importaria de fatiar o pão?',
      'Не мог бы ты аккуратно нарезать этот хлеб?',
      'Ekmeği dilimlemeyi rica etsem sakıncası olur mu?',
      'Apakah Anda tidak keberatan untuk memotong roti ini?',
      '你 介意 帮忙 切 一下 面包吗？',
      'パン を スライス して もらっても いいですか？',
      '빵을 썰어주시는 것을 부탁드려도 될까요?',
      { ur: 'Kya aap double roti kaatne ki zehmat karein ge?' }
    ),
    makeBundle(
      'I am preparing poached breakfast eggs.',
      'Estoy preparando huevos escalfados para el desayuno.',
      'میں ناشتے کے لیے پوچڈ انڈے بنا رہا ہوں۔',
      'मैं नाश्ते के लिए पोच्ड अंडे बना रहा हूँ।',
      'أنا أقوم بإعداد بيض مسلوق لوجبة الإفطار.',
      'Je prépare des œufs pochés pour le petit-déjeuner.',
      'Ich bereite pochierte Eier für das Frühstück zu.',
      'Sto preparando uova in camicia per la colazione.',
      'Estou preparando ovos pochê para o café da manhã.',
      'Я готовлю яйца пашот для нашего общего завтрака.',
      'Kahvaltı için poşe yumurta hazırlıyorum şu anda.',
      'Saya sedang menyiapkan telur rebus tanpa kulit untuk sarapan.',
      '我 正在 为 早餐 准备 水波蛋。',
      'あさごはん に ポーチド エッグ を つくって います。',
      '아침 식사를 위해 수란을 정성껏 만들고 있어요.',
      { ur: 'Main nashte ke liye poached anday bana raha hoon.' }
    ),
  ],
};

// Generates fallback progressive sentence bundle targeting the exact target word count and reactive keys
function generateSynthesizedBundle(
  topicId: string,
  ageGroup: AgeGroup,
  level: LearnerLevel,
  targetWordCount: number,
  day: number,
  sentenceIdx: number,
  variant: 'A' | 'B'
): PhraseBundle {
  const objKeys = Object.keys(THEMATIC_OBJECT_DICTIONARY);
  const hash = topicId.split('').reduce((acc, c) => acc + c.charCodeAt(0), 0);
  const ageOffset = ageGroup === '4-6' ? 0 : ageGroup === '7-9' ? 5 : ageGroup === '10-12' ? 10 : 15;
  const levelOffset = level === 'Beginner' ? 0 : level === 'Intermediate' ? 2 : 4;
  const selectedKey = objKeys[(hash + ageOffset + levelOffset + day * 3 + sentenceIdx * 5 + (variant === 'B' ? 7 : 0)) % objKeys.length];
  const obj = THEMATIC_OBJECT_DICTIONARY[selectedKey] || THEMATIC_OBJECT_DICTIONARY['warm-tea'];

  if (targetWordCount === 1) {
    const singleList = TOPIC_SINGLE_WORD_ITEMS[topicId];
    if (singleList && singleList.length > 0) {
      const it = singleList[(day * 3 + sentenceIdx - 1) % singleList.length];
      return resolveSingleWordBundle(it, 'en');
    }
    return makeBundle(
      'Morning',
      'Mañana',
      'صبح',
      'सुबह',
      'صباح',
      'Matin',
      'Morgen',
      'Mattina',
      'Manhã',
      'Утро',
      'Sabah',
      'Pagi',
      '早晨',
      'あさ',
      '아침'
    );
  }

  if (targetWordCount === 2) {
    return variant === 'A'
      ? makeBundle(
          `See ${obj.en}.`,
          `Mira ${obj.es}.`,
          `${obj.ur} دیکھیں۔`,
          `${obj.hi} देखें।`,
          `انظر ${obj.ar}.`,
          `Regarde ${obj.fr}.`,
          `Sieh ${obj.de}.`,
          `Guarda ${obj.it}.`,
          `Veja ${obj.pt}.`,
          `Посмотри на ${obj.ru}.`,
          `${obj.tr} bak.`,
          `Lihat ${obj.id}.`,
          `看 ${obj.zh}。`,
          `${obj.ja} をみて。`,
          `${obj.ko} 보세요.`
        )
      : makeBundle(
          `Hold ${obj.en}.`,
          `Toma ${obj.es}.`,
          `${obj.ur} پکڑیں۔`,
          `${obj.hi} पकड़ें।`,
          `امسك ${obj.ar}.`,
          `Tiens ${obj.fr}.`,
          `Halte ${obj.de}.`,
          `Tieni ${obj.it}.`,
          `Segure ${obj.pt}.`,
          `Держи ${obj.ru}.`,
          `${obj.tr} tut.`,
          `Pegang ${obj.id}.`,
          `拿着 ${obj.zh}。`,
          `${obj.ja} をもって。`,
          `${obj.ko} 잡아요.`
        );
  }

  if (targetWordCount === 3) {
    return variant === 'A'
      ? makeBundle(
          `I like ${obj.en}.`,
          `Me gusta ${obj.es}.`,
          `مجھے ${obj.ur} پسند ہے۔`,
          `मुझे ${obj.hi} पसंद है।`,
          `أحب ${obj.ar} كثيراً.`,
          `J\'aime ${obj.fr} bien.`,
          `Ich mag ${obj.de}.`,
          `Mi piace ${obj.it}.`,
          `Gosto de ${obj.pt}.`,
          `Мне нравится ${obj.ru}.`,
          `Ben ${obj.tr} severim.`,
          `Saya suka ${obj.id}.`,
          `我 喜欢 ${obj.zh}。`,
          `${obj.ja} が すき。`,
          `저는 ${obj.ko} 좋아해요.`
        )
      : makeBundle(
          `Pass the ${obj.en}.`,
          `Pásame ${obj.es} porfavor.`,
          `${obj.ur} ادھر دیں۔`,
          `${obj.hi} इधर दीजिए।`,
          `ناولني ${obj.ar} فضلاً.`,
          `Passe ${obj.fr} s\'il-te-plaît.`,
          `Reiche ${obj.de} herüber.`,
          `Passami ${obj.it} subito.`,
          `Passe ${obj.pt} rápido.`,
          `Передай ${obj.ru} пожалуйста.`,
          `${obj.tr} uzat lütfen.`,
          `Operkan ${obj.id} itu.`,
          `请 把 ${obj.zh} 递给我。`,
          `${obj.ja} を ちょうだい。`,
          `${obj.ko} 건네주세요.`
        );
  }

  if (targetWordCount === 4) {
    if (ageGroup === '10-12') {
      return makeBundle(
        `Help me set ${obj.en}.`,
        `Ayúdame con ${obj.es}.`,
        `${obj.ur} لگانے میں مدد کریں۔`,
        `${obj.hi} लगाने में मदद करें।`,
        `ساعدني بـ ${obj.ar}.`,
        `Aide-moi avec ${obj.fr}.`,
        `Hilf mir mit ${obj.de}.`,
        `Aiutami con ${obj.it}.`,
        `Ajude com ${obj.pt}.`,
        `Помоги мне с ${obj.ru}.`,
        `${obj.tr} yardım et.`,
        `Bantu dengan ${obj.id}.`,
        `帮我 整理 ${obj.zh}。`,
        `${obj.ja} を てつだって。`,
        `${obj.ko} 차리는것 도와줘.`
      );
    }
    if (ageGroup === '13-16') {
      return makeBundle(
        `Need morning ${obj.en} now.`,
        `Necesito ${obj.es} ahora.`,
        `ابھی ${obj.ur} چاہیے۔`,
        `अभी ${obj.hi} चाहिए।`,
        `أحتاج ${obj.ar} الآن.`,
        `J\'ai besoin de ${obj.fr}.`,
        `Ich brauche ${obj.de}.`,
        `Ho bisogno di ${obj.it}.`,
        `Preciso de ${obj.pt}.`,
        `Мне нужен ${obj.ru}.`,
        `${obj.tr} lazım şimdi.`,
        `Butuh ${obj.id} sekarang.`,
        `现在 需要 ${obj.zh}。`,
        `いま ${obj.ja} がひつよう。`,
        `지금 ${obj.ko} 필요해요.`
      );
    }
    return variant === 'A'
      ? makeBundle(
          `Please show me ${obj.en}.`,
          `Por favor muéstrame ${obj.es}.`,
          `براہ کرم مجھے ${obj.ur} دکھائیں۔`,
          `कृपया मुझे ${obj.hi} दिखाइए।`,
          `أرني من فضلك ${obj.ar}.`,
          `Montre-moi ${obj.fr} s\'il-te-plaît.`,
          `Zeige mir bitte ${obj.de}.`,
          `Mostrami per favore ${obj.it}.`,
          `Por favor mostre ${obj.pt}.`,
          `Покажи мне пожалуйста ${obj.ru}.`,
          `Lütfen bana ${obj.tr} göster.`,
          `Tolong tunjukkan ${obj.id} padaku.`,
          `请 给我 看看 ${obj.zh}。`,
          `${obj.ja} を みせて ください。`,
          `${obj.ko} 저에게 보여주세요.`
        )
      : makeBundle(
          `We always share ${obj.en}.`,
          `Siempre compartimos este ${obj.es}.`,
          `ہم ہمیشہ مل کر ${obj.ur} بانٹتے ہیں۔`,
          `हम हमेशा मिलकर ${obj.hi} बांटते हैं।`,
          `نحن دائماً نتشارك ${obj.ar} بمحبة.`,
          `Nous partageons toujours ${obj.fr} ensemble.`,
          `Wir teilen immer ${obj.de} miteinander.`,
          `Condividiamo sempre ${obj.it} insieme felicemente.`,
          `Nós sempre compartilhamos ${obj.pt} juntos.`,
          `Мы всегда делимся ${obj.ru} дружно.`,
          `Biz her zaman ${obj.tr} paylaşırız.`,
          `Kami selalu berbagi ${obj.id} bersama.`,
          `我们 总是 分享 ${obj.zh}。`,
          `いつも いっしょに ${obj.ja} をわけあおう。`,
          `우리는 항상 ${obj.ko} 함께 나눠요.`
        );
  }

  if (targetWordCount === 5) {
    if (ageGroup === '10-12') {
      return makeBundle(
        `I will organize the ${obj.en}.`,
        `Organizaré con cuidado este ${obj.es}.`,
        `میں احتیاط سے ${obj.ur} ترتیب دوں گا۔`,
        `मैं ध्यान से ${obj.hi} व्यवस्थित करूंगा।`,
        `سأنظم هذا ${obj.ar} بعناية.`,
        `J\'organiserai ce ${obj.fr} soigneusement.`,
        `Ich werde ${obj.de} sorgfältig ordnen.`,
        `Organizzerò questo ${obj.it} con cura.`,
        `Vou organizar este ${obj.pt} bem.`,
        `Я аккуратно разложу ${obj.ru} сейчас.`,
        `${obj.tr} dikkatlice düzenleyeceğim bugün.`,
        `Saya akan menata ${obj.id} itu.`,
        `我 会 整理 好 这个 ${obj.zh}。`,
        `わたし が ${obj.ja} を かたづけるね。`,
        `제가 ${obj.ko} 잘 정리해 둘게요.`
      );
    }
    if (ageGroup === '13-16') {
      return makeBundle(
        `Could you pass that ${obj.en}?`,
        `¿Podrías pasarme ese buen ${obj.es}?`,
        `کیا آپ وہ ${obj.ur} ادھر دیں گے؟`,
        `क्या आप वह ${obj.hi} इधर देंगे?`,
        `هل يمكنك تمرير هذا ${obj.ar}؟`,
        `Pourriez-vous me passer ce ${obj.fr}?`,
        `Könntest du mir ${obj.de} reichen?`,
        `Potresti passarmi quel ${obj.it} adesso?`,
        `Você poderia passar aquele ${obj.pt}?`,
        `Не мог бы ты передать ${obj.ru}?`,
        `Bana o ${obj.tr} uzatabilir misiniz?`,
        `Bisakah Anda operkan ${obj.id} itu?`,
        `你可以 把 ${obj.zh} 递给我吗？`,
        `その ${obj.ja} を とって もらえますか？`,
        `그 ${obj.ko} 저에게 건네주시겠어요?`
      );
    }
    return variant === 'A'
      ? makeBundle(
          `Could you pass that ${obj.en}?`,
          `¿Podrías pasarme ese lindo ${obj.es}?`,
          `کیا آپ مجھے وہ ${obj.ur} پکڑائیں گے؟`,
          `क्या आप मुझे वह ${obj.hi} पकड़ाएंगे?`,
          `هل يمكنك أن تمرر لي ${obj.ar}؟`,
          `Pourriez-vous me passer ce ${obj.fr} ?`,
          `Könntest du mir bitte ${obj.de} herüberreichen?`,
          `Potresti passarmi quel bel ${obj.it} adesso?`,
          `Você poderia passar aquele ${obj.pt} agora?`,
          `Не мог бы ты передать мне ${obj.ru}?`,
          `Bana o güzel ${obj.tr} uzatabilir misiniz?`,
          `Bisakah Anda mengoperkan ${obj.id} itu padaku?`,
          `你可以 把 那个 ${obj.zh} 递给我吗？`,
          `その ${obj.ja} を とって もらえますか？`,
          `그 ${obj.ko} 저에게 건네주실 수 있나요?`
        )
      : makeBundle(
          `I am looking for ${obj.en}.`,
          `Estoy buscando mi querido ${obj.es}.`,
          `میں اپنا پسندیدہ ${obj.ur} تلاش کر رہا ہوں۔`,
          `मैं अपना पसंदीदा ${obj.hi} खोज रहा हूँ।`,
          `أنا أبحث عن ${obj.ar} في كل مكان.`,
          `Je suis à la recherche de ${obj.fr}.`,
          `Ich suche gerade nach meinem ${obj.de}.`,
          `Sto cercando il mio amato ${obj.it} qui.`,
          `Estou procurando pelo meu ${obj.pt} favorito.`,
          `Я ищу свой любимый ${obj.ru} везде.`,
          `Her yerde benim ${obj.tr} arıyorum şu an.`,
          `Saya sedang mencari ${obj.id} kesayangan saya.`,
          `我 正在 寻找 我的 ${obj.zh}。`,
          `わたし の ${obj.ja} を さがして います。`,
          `저는 소중한 ${obj.ko} 찾고 있어요 지금.`
        );
  }

  if (targetWordCount === 6) {
    if (ageGroup === '13-16') {
      return makeBundle(
        `I prefer having fresh ${obj.en} mornings.`,
        `Prefiero disfrutar de ${obj.es} temprano.`,
        `میں صبح کے وقت ${obj.ur} ترجیح دیتا ہوں۔`,
        `मैं सुबह के समय ${obj.hi} पसंद करता हूँ।`,
        `أفضل الاستمتاع بـ ${obj.ar} صباحاً دائماً.`,
        `Je préfère avoir ${obj.fr} chaque matin.`,
        `Ich bevorzuge morgens frisches gutes ${obj.de}.`,
        `Preferisco godermi ${obj.it} ogni bella mattina.`,
        `Prefiro aproveitar ${obj.pt} todas as manhãs.`,
        `Я предпочитаю свежий ${obj.ru} каждое утро.`,
        `Sabahları taze ${obj.tr} almayı tercih ederim.`,
        `Saya lebih suka menikmati ${obj.id} pagi.`,
        `我 更 喜欢 早上 享用 ${obj.zh}。`,
        `あさ は ${obj.ja} を たのしむ のが すき。`,
        `아침에는 신선한 ${obj.ko} 즐기는 것을 선호해요.`
      );
    }
    return variant === 'A'
      ? makeBundle(
          `Please help me take care of ${obj.en}.`,
          `Por favor ayúdame a cuidar ${obj.es}.`,
          `براہ کرم ${obj.ur} کا خیال رکھنے میں میری مدد کریں۔`,
          `कृपया ${obj.hi} का ध्यान रखने में मदद कीजिए।`,
          `ساعدني رجاءً في الاعتناء بـ ${obj.ar} جيداً.`,
          `Aide-moi s\'il-te-plaît à prendre soin de ${obj.fr}.`,
          `Hilf mir bitte gut auf ${obj.de} aufzupassen.`,
          `Aiutami per favore a prendermi cura di ${obj.it}.`,
          `Por favor ajude a cuidar bem de ${obj.pt}.`,
          `Помоги мне пожалуйста заботиться о ${obj.ru} аккуратно.`,
          `Lütfen ${obj.tr} dikkatlice korumama yardım etsene.`,
          `Tolong bantu saya merawat ${obj.id} ini dengan baik.`,
          `请 帮我 一起 细心 照料 这个 ${obj.zh}。`,
          `${obj.ja} を たいせつに するのを てつだって ください。`,
          `${obj.ko} 정성껏 돌보는 것을 도와주시겠어요?`
        )
      : makeBundle(
          `We should always protect our beloved ${obj.en}.`,
          `Siempre debemos cuidar mucho a nuestro ${obj.es}.`,
          `ہمیں ہمیشہ اپنے پیارے ${obj.ur} کی حفاظت کرنی چاہیے۔`,
          `हमें हमेशा अपने प्यारे ${obj.hi} की रक्षा करनी चाहिए।`,
          `يجب علينا دوماً حماية هذا ${obj.ar} بحرص.`,
          `Nous devons toujours protéger notre cher ${obj.fr} ensemble.`,
          `Wir sollten immer gut auf unser ${obj.de} achten.`,
          `Dovremmo sempre proteggere con cura il nostro ${obj.it}.`,
          `Devemos sempre proteger nosso querido ${obj.pt} com carinho.`,
          `Мы должны бережно хранить наш любимый ${obj.ru} всегда.`,
          `Her zaman sevgili ${obj.tr} korumamız ve kollamamız gerekir.`,
          `Kita harus selalu menjaga dan menyayangi ${obj.id} kita.`,
          `我们 应当 始终 爱护 我们 珍贵的 ${obj.zh}。`,
          `いつも わたしたち の ${obj.ja} を まもりましょう。`,
          `우리는 소중한 ${obj.ko} 항상 아끼고 지켜주어야 해요.`
        );
  }

  // 7+ Words (Tiers 2 & 3, older brackets)
  return variant === 'A'
    ? makeBundle(
        `Communicating clearly about ${obj.en} builds confidence and lasting friendship.`,
        `Hablar con claridad sobre ${obj.es} fortalece la amistad.`,
        `${obj.ur} کے بارے میں بات چیت اعتماد اور گہری دوستی بڑھاتی ہے۔`,
        `${obj.hi} کے بارے میں बातचीत आत्मविश्वास और मित्रता बढ़ाती है।`,
        `التواصل الواضح بشأن ${obj.ar} ينمي الثقة بالنفس والصداقة الدائمة.`,
        `Parler clairement de ${obj.fr} renforce la confiance et l\'amitié.`,
        `Klares Sprechen über ${obj.de} stärkt das Selbstvertrauen und Freundschaften.`,
        `Parlare con chiarezza di ${obj.it} accresce la fiducia e l\'amicizia.`,
        `Falar com clareza sobre ${obj.pt} constrói confiança e amizade duradoura.`,
        `Чёткое и вежливое обсуждение ${obj.ru} укрепляет дружбу и уверенность.`,
        `${obj.tr} hakkında açıkça konuşmak özgüveni ve dostluğu pekiştirir her zaman.`,
        `Berkomunikasi dengan jelas tentang ${obj.id} membangun rasa percaya diri kuat.`,
        `清晰 自信地 谈论 ${obj.zh} 能 增进 彼此 友谊。`,
        `${obj.ja} について はなす ことで じしん と ゆうじょう が ふかまります。`,
        `${obj.ko} 대해 명확하게 대화하는 것은 자신감과 깊은 우정을 키워줍니다.`
      )
    : makeBundle(
        `Learning everyday expressions about ${obj.en} allows us to connect with others.`,
        `Aprender frases cotidianas sobre ${obj.es} nos une con los demás.`,
        `${obj.ur} کے متعلق روزمرہ جملے سیکھنا ہمیں دوسروں سے جوڑتا ہے۔`,
        `${obj.hi} से जुड़े रोजमर्रा के वाक्य हमें दूसरों से जोड़ते हैं।`,
        `تعلم التعبيرات اليومية حول ${obj.ar} يساعدنا على التواصل الودي مع الجميع.`,
        `Apprendre des expressions sur ${obj.fr} nous aide à communiquer avec tous.`,
        `Tägliche Redewendungen über ${obj.de} verbinden uns wunderbar mit anderen Menschen.`,
        `Imparare espressioni quotidiane su ${obj.it} ci connette profondamente con gli altri.`,
        `Aprender frases do cotidiano sobre ${obj.pt} nos conecta com outras pessoas.`,
        `Изучение повседневных фраз о ${obj.ru} помогает находить общий язык со всеми.`,
        `${obj.tr} ile ilgili günlük ifadeleri öğrenmek insanlarla bağ kurmamızı kolaylaştırır.`,
        `Mempelajari ungkapan sehari-hari tentang ${obj.id} menghubungkan kita dengan orang lain.`,
        `学习 关于 ${obj.zh} 的 日常 表达 能 让 我们 与人 亲近。`,
        `${obj.ja} の ことば を まなぶ ことで みんな と なかよく なれます。`,
        `${obj.ko} 관한 일상 표현을 배우면 다른 사람들과 따뜻하게 소통할 수 있어요.`
      );
}

// ============================================================================
// MAIN DATA RESOLUTION SERVICE: getCardPracticeData & getConversationalCurriculum
// ============================================================================

export interface GetConversationalCurriculumOptions {
  day?: number; // 1 to 90
  currentDay?: number;
  ageGroup: AgeGroup;
  level: LearnerLevel;
  category?: string;
  topicId?: string;
  targetLanguage: LanguageCode;
  motherTongue: LanguageCode;
  remediationVariant?: 'A' | 'B';
  weekSeed?: number;
}

/**
 * Universal data resolver explicitly keyed on [ageGroup, level, currentDay, topicId, targetLanguage].
 * Supplies 3 unique, progressive sentences for any combination of parameters.
 */
export function getCardPracticeData(
  optionsOrAgeGroup: GetConversationalCurriculumOptions | AgeGroup,
  levelArg?: LearnerLevel,
  dayArg?: number,
  topicIdArg?: string,
  targetLangArg?: LanguageCode,
  motherTongueArg?: LanguageCode,
  categoryArg?: string,
  variantArg?: 'A' | 'B',
  weekSeedArg?: number
): CardPracticeData & ConversationalCurriculumResult {
  let day: number;
  let ageGroup: AgeGroup;
  let level: LearnerLevel;
  let category: string;
  let topicId: string;
  let targetLanguage: LanguageCode;
  let motherTongue: LanguageCode;
  let remediationVariant: 'A' | 'B';
  let weekSeed: number;

  if (typeof optionsOrAgeGroup === 'object') {
    day = optionsOrAgeGroup.currentDay ?? optionsOrAgeGroup.day ?? 1;
    ageGroup = optionsOrAgeGroup.ageGroup;
    level = optionsOrAgeGroup.level;
    category = optionsOrAgeGroup.category || 'Home & Daily Life';
    topicId = optionsOrAgeGroup.topicId || 'breakfast-chat';
    targetLanguage = optionsOrAgeGroup.targetLanguage;
    motherTongue = optionsOrAgeGroup.motherTongue || 'en';
    remediationVariant = optionsOrAgeGroup.remediationVariant || 'A';
    weekSeed = optionsOrAgeGroup.weekSeed || 0;
  } else {
    ageGroup = optionsOrAgeGroup;
    level = levelArg || 'Beginner';
    day = dayArg || 1;
    topicId = topicIdArg || 'breakfast-chat';
    targetLanguage = targetLangArg || 'es';
    motherTongue = motherTongueArg || 'en';
    category = categoryArg || 'Home & Daily Life';
    remediationVariant = variantArg || 'A';
    weekSeed = weekSeedArg || 0;
  }

  const weekNumber = Math.ceil(day / 7);
  const tier = getTierForDay(day);
  const isRemediationVariantB = remediationVariant === 'B' || weekSeed > 0;
  const activeVariant: 'A' | 'B' = isRemediationVariantB ? 'B' : 'A';

  const canonicalTopic = CANONICAL_TOPIC_DATA[topicId];
  const items: ConversationalSentenceItem[] = [];

  const trackKey = `${ageGroup}__${level}`;
  const dedicatedBreakfastDay11 = (topicId === 'breakfast-chat' && day === 11)
    ? BREAKFAST_DEDICATED_DAY11[trackKey]
    : null;

  for (let sIdx = 1; sIdx <= 3; sIdx++) {
    const targetWordCount = getTargetWordCount(ageGroup, level, day, sIdx);
    let chosenBundle: PhraseBundle | null = null;

    // A. AGE GROUP 4–6 EXACT PROGRESSION SPECIFICATION:
    if (ageGroup === '4-6') {
      if (level === 'Beginner') {
        if (day <= 7) {
          // WEEK 1 (Days 1 to 7) -> STRICTLY 1 SINGLE WORD PER ITEM
          const singleList = TOPIC_SINGLE_WORD_ITEMS[topicId];
          if (singleList && singleList[sIdx - 1]) {
            chosenBundle = resolveSingleWordBundle(singleList[sIdx - 1], targetLanguage);
          }
        } else if (day <= 14) {
          // WEEK 2 (Days 8 to 14) -> STRICTLY 2 WORDS: "MODIFIER + NOUN"
          const w1List = TOPIC_TWO_WORD_ITEMS_W1[topicId];
          if (w1List && w1List[sIdx - 1]) {
            chosenBundle = resolveTwoWordBundle(w1List[sIdx - 1], targetLanguage);
          }
        } else if (day <= 21) {
          // WEEK 3 (Days 15 to 21) -> STRICTLY 2 WORDS: "ACTION VERB + NOUN"
          const w2List = TOPIC_TWO_WORD_ITEMS_W2[topicId];
          if (w2List && w2List[sIdx - 1]) {
            chosenBundle = resolveTwoWordBundle(w2List[sIdx - 1], targetLanguage);
          }
        } else if (day <= 30) {
          // WEEK 4 (Days 22 to 30) -> STRICTLY 3 WORDS PER ITEM
          const w4List = TOPIC_AGE4TO6_W4[topicId];
          if (w4List && w4List[sIdx - 1]) {
            chosenBundle = resolveAge4to6Bundle(w4List[sIdx - 1], 3);
          }
        } else if (day <= 60) {
          // TIER 2 (Days 31 to 60) -> STRICTLY 4 TO 5 WORDS PER ITEM
          const t2List = TOPIC_AGE4TO6_TIER2[topicId];
          if (t2List && t2List[sIdx - 1]) {
            chosenBundle = resolveAge4to6Bundle(t2List[sIdx - 1], targetWordCount);
          }
        } else {
          // TIER 3 (Days 61 to 90) -> STRICTLY 5 TO 6 WORDS PER ITEM
          const t3List = TOPIC_AGE4TO6_TIER3[topicId];
          if (t3List && t3List[sIdx - 1]) {
            chosenBundle = resolveAge4to6Bundle(t3List[sIdx - 1], targetWordCount);
          }
        }
      } else if (level === 'Intermediate') {
        if (day <= 7) {
          // Week 1 (Days 1 to 7): Exactly 2 words per item.
          const w1List = TOPIC_TWO_WORD_ITEMS_W1[topicId];
          if (w1List && w1List[sIdx - 1]) {
            chosenBundle = resolveTwoWordBundle(w1List[sIdx - 1], targetLanguage);
          }
        } else if (day <= 14) {
          // Week 2 (Days 8 to 14): Exactly 3 words per item.
          const w4List = TOPIC_AGE4TO6_W4[topicId];
          if (w4List && w4List[sIdx - 1]) {
            chosenBundle = resolveAge4to6Bundle(w4List[sIdx - 1], 3);
          }
        } else if (day <= 21) {
          // Week 3 (Days 15 to 21): Exactly 4 words per item.
          const t2List = TOPIC_AGE4TO6_TIER2[topicId];
          if (t2List && t2List[sIdx - 1]) {
            chosenBundle = resolveAge4to6Bundle(t2List[sIdx - 1], 4);
          }
        } else if (day <= 30) {
          // Week 4 (Days 22 to 30): Exactly 5 words per item.
          const t2List = TOPIC_AGE4TO6_TIER2[topicId];
          if (t2List && t2List[sIdx - 1]) {
            chosenBundle = resolveAge4to6Bundle(t2List[sIdx - 1], 5);
          }
        } else if (day <= 60) {
          // Tier 2 (Days 31 to 60): Exactly 5 to 6 words per item.
          const t3List = TOPIC_AGE4TO6_TIER3[topicId];
          if (t3List && t3List[sIdx - 1]) {
            chosenBundle = resolveAge4to6Bundle(t3List[sIdx - 1], targetWordCount);
          }
        } else {
          // Tier 3 (Days 61 to 90): Exactly 6 to 7 words per item.
          const t3List = TOPIC_AGE4TO6_TIER3[topicId];
          if (t3List && t3List[sIdx - 1]) {
            chosenBundle = resolveAge4to6Bundle(t3List[sIdx - 1], targetWordCount);
          }
        }
      } else {
        // Advanced
        if (day <= 7) {
          // Week 1 (Days 1 to 7): Exactly 3 words per item.
          const w4List = TOPIC_AGE4TO6_W4[topicId];
          if (w4List && w4List[sIdx - 1]) {
            chosenBundle = resolveAge4to6Bundle(w4List[sIdx - 1], 3);
          }
        } else if (day <= 14) {
          // Week 2 (Days 8 to 14): Exactly 4 words per item.
          const t2List = TOPIC_AGE4TO6_TIER2[topicId];
          if (t2List && t2List[sIdx - 1]) {
            chosenBundle = resolveAge4to6Bundle(t2List[sIdx - 1], 4);
          }
        } else if (day <= 21) {
          // Week 3 (Days 15 to 21): Exactly 5 words per item.
          const t2List = TOPIC_AGE4TO6_TIER2[topicId];
          if (t2List && t2List[sIdx - 1]) {
            chosenBundle = resolveAge4to6Bundle(t2List[sIdx - 1], 5);
          }
        } else if (day <= 30) {
          // Week 4 (Days 22 to 30): Exactly 6 words per item.
          const t3List = TOPIC_AGE4TO6_TIER3[topicId];
          if (t3List && t3List[sIdx - 1]) {
            chosenBundle = resolveAge4to6Bundle(t3List[sIdx - 1], 6);
          }
        } else if (day <= 60) {
          // Tier 2 (Days 31 to 60): Exactly 6 to 7 words per item.
          const t3List = TOPIC_AGE4TO6_TIER3[topicId];
          if (t3List && t3List[sIdx - 1]) {
            chosenBundle = resolveAge4to6Bundle(t3List[sIdx - 1], targetWordCount);
          }
        } else {
          // Tier 3 (Days 61 to 90): Exactly 7 to 8 words per item.
          const t3List = TOPIC_AGE4TO6_TIER3[topicId];
          if (t3List && t3List[sIdx - 1]) {
            chosenBundle = resolveAge4to6Bundle(t3List[sIdx - 1], targetWordCount);
          }
        }
      }
    }
    // 0. Age 7-9 Beginner:
    // Week 1 (Days 1 to 7) -> STRICT "MODIFIER + NOUN" PATTERN (100% Adjective + Noun, strictly 2 words, no action verbs)
    // Week 2 (Days 8 to 14) -> STRICT "ACTION VERB + NOUN" PATTERN (100% Action Verb + Noun, strictly 2 words)
    // Enforced across all 15 categories and all 77 topics
    else if (ageGroup === '7-9' && level === 'Beginner' && day <= 14) {
      const topicTwoWordList = day <= 7
        ? (TOPIC_TWO_WORD_ITEMS_W1[topicId] || TOPIC_TWO_WORD_ITEMS[topicId])
        : (TOPIC_TWO_WORD_ITEMS_W2[topicId] || TOPIC_TWO_WORD_ITEMS[topicId]);
      if (topicTwoWordList && topicTwoWordList[sIdx - 1]) {
        chosenBundle = resolveTwoWordBundle(topicTwoWordList[sIdx - 1], targetLanguage);
      }
    }
    // 1. Day 11 "Breakfast Chat" dedicated track check
    else if (dedicatedBreakfastDay11 && dedicatedBreakfastDay11[sIdx - 1]) {
      chosenBundle = dedicatedBreakfastDay11[sIdx - 1];
    }
    // 2. Strictly 1-word single items across all 77 topics
    else if (targetWordCount === 1) {
      const singleList = TOPIC_SINGLE_WORD_ITEMS[topicId];
      if (singleList && singleList.length > 0) {
        const wordIdx = (day * 3 + sIdx - 1) % singleList.length;
        chosenBundle = resolveSingleWordBundle(singleList[wordIdx], targetLanguage);
      }
    }
    // 3. Fallback to canonical topic pool if ageGroup matches baseline
    else if (canonicalTopic && ageGroup === '7-9' && level === 'Beginner') {
      const poolMap = activeVariant === 'B'
        ? canonicalTopic.variantsByCountB
        : canonicalTopic.variantsByCountA;
      const candidatePool = poolMap?.[targetWordCount];

      if (candidatePool && candidatePool.length > 0) {
        const pIdx = ((day - 11) * 3 + (sIdx - 1) + weekSeed + 300) % candidatePool.length;
        chosenBundle = candidatePool[pIdx];
      }
    }

    // 4. Synthesize age-and-level dedicated sentence bundle
    if (!chosenBundle) {
      chosenBundle = generateSynthesizedBundle(topicId, ageGroup, level, targetWordCount, day, sIdx, activeVariant);
    }

    const rawTarget = chosenBundle.target[targetLanguage] || chosenBundle.target.en || 'Hello.';
    const rawEnglish = chosenBundle.target.en || chosenBundle.target[motherTongue] || rawTarget;
    const rawRomanized = chosenBundle.romanized[targetLanguage] || rawTarget;

    const tokens = tokenizeSentence(rawTarget, targetLanguage);

    items.push({
      id: `${topicId}_d${day}_s${sIdx}`,
      day,
      sentenceIndex: sIdx,
      speaker: sIdx === 1 ? 'Learner' : sIdx === 2 ? 'Companion' : 'Native Guide',
      english: `"${rawEnglish.replace(/^"|"$/g, '')}"`, // Enforce English in quotation marks
      targetText: rawTarget,
      romanized: rawRomanized,
      tokens,
      wordCount: targetWordCount,
      tip: undefined,
    });
  }

  const primaryItem = items[0];
  const item1: CardPracticeItem = {
    ...items[0],
    motherTongueText: items[0].english,
    soundsLike: items[0].romanized,
    trayTiles: items[0].tokens.slice().reverse(),
  };
  const item2: CardPracticeItem = {
    ...items[1],
    motherTongueText: items[1].english,
    soundsLike: items[1].romanized,
    trayTiles: items[1].tokens.slice().reverse(),
  };
  const item3: CardPracticeItem = {
    ...items[2],
    motherTongueText: items[2].english,
    soundsLike: items[2].romanized,
    trayTiles: items[2].tokens.slice().reverse(),
  };

  return {
    id: `${topicId}_d${day}`,
    topicId,
    categoryId: category,
    day,
    currentDay: day,
    weekNumber,
    tier,
    ageGroup,
    level,
    targetLanguage,
    motherTongue,
    targetWordCount: primaryItem.wordCount,
    isRemediationVariantB,
    // Slot convenience bindings matching card slots:
    motherTongueText: primaryItem.english,
    targetText: primaryItem.targetText,
    soundsLike: primaryItem.romanized,
    romanized: primaryItem.romanized,
    trayTiles: primaryItem.tokens.slice().reverse(),
    tokens: primaryItem.tokens,
    practiceItems: [items[0].targetText, items[1].targetText, items[2].targetText],
    items: [item1, item2, item3],
    phoneticHint: primaryItem.romanized,
  };
}

/**
 * Convenience alias for getCardPracticeData
 */
export function getConversationalCurriculum(
  options: GetConversationalCurriculumOptions
): ConversationalCurriculumResult & CardPracticeData {
  return getCardPracticeData(options);
}
