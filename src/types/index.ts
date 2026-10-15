export type AgeGroup = '4-6' | '7-9' | '10-12' | '13-16';

export type LearnerLevel = 'Beginner' | 'Intermediate' | 'Advanced';
export type Level = LearnerLevel;

export interface PracticeCardItem {
  id: string; // e.g., "cat-1_top-3_d-11"
  categoryId: string | number;
  topicId: string | number;
  day: number; // 1 to 90
  ageGroup: AgeGroup;
  level: Level;
  practiceItems: [string, string, string]; // Strictly 3 speaking items
  phoneticHint?: string; // Optional pronunciation cue
}

// 15 supported languages (en, es, fr, zh, tr, id, it, de, pt, ru, ja, ko, ur, hi, ar)
export type LanguageCode =
  | 'en'
  | 'es'
  | 'fr'
  | 'zh'
  | 'tr'
  | 'id'
  | 'it'
  | 'ur'
  | 'hi'
  | 'ar'
  | 'de'
  | 'pt'
  | 'ru'
  | 'ja'
  | 'ko';

export type LearningGoal = 'Speaking' | 'Reading' | 'Writing';

export interface LanguageInfo {
  code: LanguageCode;
  label: string;
  nativeName: string;
  flag: string;
  speechLocale: string;
  dir: 'ltr' | 'rtl';
}

export interface DialoguePhrase {
  id: string;
  speaker: string;
  targetPhrases: Partial<Record<LanguageCode, string>>;
  phonetics: Partial<Record<LanguageCode, string>>; // phonetic pronunciation guide
  translations: Partial<Record<LanguageCode, string>>; // translations in each language
  tip?: string;
  chunks?: any;
  scrambledWords?: Partial<Record<LanguageCode, string[]>>; // For writing goal
}

// 15 Comprehensive Conversation Categories (all strictly have at least 5 topics)
export type TopicCategory =
  | 'Home & Daily Life'
  | 'Family & Relatives'
  | 'Travel & Transport'
  | 'Shopping & Food'
  | 'Health & Doctor'
  | 'School & Study'
  | 'Friends & Play'
  | 'Nature & Outdoors'
  | 'Manners & Help'
  | 'Fun & Tech'
  | 'Time & Weather'
  | 'Holidays & Events'
  | 'Sports & Games'
  | 'Clothes & Style'
  | 'Chores & Helping';

export interface TopicScenario {
  id: string;
  title: string;
  category: TopicCategory;
  description: string;
  iconName: string;
  badgeEmoji: string;
  youtubeVideoId: string;
  videoTitle: string;
  rewardName: string;
  dialoguesByAge: Record<AgeGroup, DialoguePhrase[]>;
}

// Card step quotas for every single sentence:
// Listening (3), Watching (5), Practice (10), Speaking (3)
export interface CardStepQuotas {
  listening: number;
  watching: number;
  practice: number;
  speaking: number;
}

export interface RewardsState {
  dailyBadges: number[]; // Day numbers unlocked (e.g. [1, 2, 3])
  categoryBadges: string[]; // Unlocked category names
  topicBadges: string[]; // Unlocked topic IDs
  cardRewards: {
    listeningCount: number;
    watchingCount: number;
    practiceCount: number;
    speakingCount: number;
  };
}

export interface UserProfile {
  ageGroup: AgeGroup;
  level: LearnerLevel; // Beginner, Intermediate, Advanced
  motherTongue: LanguageCode;
  targetLanguage: LanguageCode;
  learningGoal: LearningGoal;
  completedTopics: string[]; // ids of completed topics
  phraseMastery: Record<string, number>; // phraseId -> score percentage (0-100)
  totalXp: number;
  totalStars: number;
  speechRate: number; // 0.75, 1.0, 1.25
  autoPlayTts: boolean;

  // 90-Day Progression Engine
  currentDay: number; // 1 to 90
  completedDays: number[]; // e.g. [1, 2, ...]
  weekSeeds: Record<number, number>; // weekNumber (1..13) -> seed for sentence shuffle on failed weekly exam

  // Card Step Quotas for sentences: key is `day_topic_phraseId`
  sentenceStepQuotas: Record<string, CardStepQuotas>;

  // Multi-tier Rewards
  rewards: RewardsState;

  // Exam Scores
  examScores: Record<number, number>; // dayNumber -> score (0-100)
  remediationWeeks?: Record<number, boolean>; // weekNumber -> true if in Remediation Variant B

  diplomaUnlocked?: boolean;
  digitalPassportStamps?: string[];
  dailyXp?: Record<string, number>;
}

export interface ConversationalSentenceItem {
  id: string; // e.g. "breakfast-chat_d11_s1"
  day: number;
  sentenceIndex: number; // 1, 2, 3
  speaker: string; // 'Learner' | 'Companion' | 'Native Guide'
  english: string; // English translation in quotation marks
  targetText: string; // Native script in target language
  romanized: string; // Romanized pronunciation guide ("Sounds like: ...")
  tokens: string[]; // Interactive word tiles for Step 3 Assembly Tray
  wordCount: number;
  tip?: string; // Optional authentic conversational tip
}

export interface ConversationalCurriculumResult {
  topicId: string;
  categoryId: string;
  day: number;
  weekNumber: number;
  tier: 1 | 2 | 3;
  targetWordCount: number;
  isRemediationVariantB: boolean;
  items: [ConversationalSentenceItem, ConversationalSentenceItem, ConversationalSentenceItem];
}

export type MasteryLevel = 'Beginner' | 'Intermediate' | 'Advanced' | 'Novice' | 'Conversational' | 'Fluent' | 'Master';

export interface DailyXpRecord {
  date?: string;
  day?: number | string;
  xp: number;
}

export interface ScenarioTrack {
  id: string;
  title: string;
  subtitle?: string;
  badge?: string;
  badgeEmoji?: string;
  youtubeId?: string;
  youtubeVideoId?: string;
  videoTitle?: string;
  targetObjective?: string;
}

export type CoreCategoryId = string;

export interface CoreCategory {
  id: CoreCategoryId;
  name?: string;
  title?: string;
  subtitle?: string;
  icon?: string;
  badgeEmoji?: string;
  description?: string;
  scenarios?: ScenarioTrack[];
  tracks?: ScenarioTrack[];
}

export interface ExamQuestion {
  id: string;
  question: string;
  targetPhrase: string;
  phonetic: string;
  correctAnswer: string;
  options: string[];
}

export interface PassportStamp {
  id: string;
  title: string;
  icon: string;
  unlockedAt: string;
}

export interface GeneratedSentence {
  id: string;
  target: string;
  speaker?: string;
  colloquialTarget?: string;
  phonetic?: string;
  phoneticTransliteration?: string;
  translation?: string;
  motherTongueTranslation?: string;
  contextTip?: string;
  tip?: string;
  openingChunk?: string;
}

export interface CardPracticeItem {
  id: string;
  day: number;
  sentenceIndex: number;
  wordCount: number;
  // Slot 1: Mother Tongue Slot (Natural conversational English sentence in quotes)
  motherTongueText: string;
  english: string; // alias
  // Slot 2: Target Language Slot (Spoken target language script)
  targetText: string;
  // Slot 3: Sounds Like Slot (Natural conversational Romanized pronunciation)
  soundsLike: string;
  romanized: string; // alias
  // Slot 4: Tray Tiles Slot (Scrambled array of tokens derived strictly from target language string)
  trayTiles: string[];
  tokens: string[];
  speaker: string;
  tip?: string;
}

export interface CardPracticeData {
  id: string;
  topicId: string;
  categoryId: string;
  day: number;
  currentDay: number;
  ageGroup: AgeGroup;
  level: LearnerLevel;
  targetLanguage: LanguageCode;
  motherTongue: LanguageCode;
  targetWordCount: number;
  isRemediationVariantB: boolean;
  items: [CardPracticeItem, CardPracticeItem, CardPracticeItem];
  practiceItems: [string, string, string];
  phoneticHint?: string;
  // Slot convenience bindings
  motherTongueText?: string;
  soundsLike?: string;
  romanized?: string;
  targetText?: string;
  trayTiles?: string[];
  tokens?: string[];
}

export interface UserProfilePro extends UserProfile {
  activeDay?: number;
  unlockedDays?: number[];
  passedExams?: Record<string, boolean>;
  completedScenarios?: string[];
  vocalRepetitionCounts?: Record<string, number>;
  dailyXpHistory?: DailyXpRecord[];
}
