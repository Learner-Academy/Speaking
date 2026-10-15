import { TopicCategory } from '../types';

export interface CategoryRewardDef {
  category: TopicCategory;
  name: string;
  badgeEmoji: string;
  description: string;
}

export const CATEGORY_REWARDS: Record<TopicCategory, CategoryRewardDef> = {
  'Home & Daily Life': {
    category: 'Home & Daily Life',
    name: 'Home Master',
    badgeEmoji: '🏡',
    description: 'Mastered everyday morning, dining, and home conversations.',
  },
  'Family & Relatives': {
    category: 'Family & Relatives',
    name: 'Family Champion',
    badgeEmoji: '❤️',
    description: 'Expressed emotions and connected warmly with loved ones.',
  },
  'Travel & Transport': {
    category: 'Travel & Transport',
    name: 'Globe Trotter',
    badgeEmoji: '✈️',
    description: 'Confident navigation of train platforms, flights, and bus stations.',
  },
  'Shopping & Food': {
    category: 'Shopping & Food',
    name: 'Market Maestro',
    badgeEmoji: '🛒',
    description: 'Handled transactions, ordering foods, and courteous checkout.',
  },
  'Health & Doctor': {
    category: 'Health & Doctor',
    name: 'Health Guardian',
    badgeEmoji: '🩺',
    description: 'Accurately described symptoms and medical instructions.',
  },
  'School & Study': {
    category: 'School & Study',
    name: 'Scholar Hero',
    badgeEmoji: '🎓',
    description: 'Excelled in classroom collaboration and polite academic queries.',
  },
  'Friends & Play': {
    category: 'Friends & Play',
    name: 'Playmate Ace',
    badgeEmoji: '⚽',
    description: 'Formed friendships, shared games, and demonstrated sportsmanship.',
  },
  'Nature & Outdoors': {
    category: 'Nature & Outdoors',
    name: 'Nature Scout',
    badgeEmoji: '🌲',
    description: 'Explored outdoor adventures, weather elements, and nature.',
  },
  'Manners & Help': {
    category: 'Manners & Help',
    name: 'Manners Ambassador',
    badgeEmoji: '🤝',
    description: 'Speaks with gratitude, empathy, and exceptional politeness.',
  },
  'Fun & Tech': {
    category: 'Fun & Tech',
    name: 'Digital Prodigy',
    badgeEmoji: '🎮',
    description: 'Discussed games, creative tools, and digital communications.',
  },
  'Time & Weather': {
    category: 'Time & Weather',
    name: 'Chrono Navigator',
    badgeEmoji: '⛅',
    description: 'Understands daily routines, schedules, seasons, and forecasts.',
  },
  'Holidays & Events': {
    category: 'Holidays & Events',
    name: 'Festival Star',
    badgeEmoji: '🎉',
    description: 'Exchanged cultural wishes, celebrations, and gift greetings.',
  },
  'Sports & Games': {
    category: 'Sports & Games',
    name: 'Athletic Champion',
    badgeEmoji: '🏆',
    description: 'Mastered athletic teamwork, match commentary, and sports play.',
  },
  'Clothes & Style': {
    category: 'Clothes & Style',
    name: 'Style Icon',
    badgeEmoji: '👕',
    description: 'Chose outfits, described colors, and dressed with independence.',
  },
  'Chores & Helping': {
    category: 'Chores & Helping',
    name: 'Helping Hand Ace',
    badgeEmoji: '🧹',
    description: 'Maintains personal space, cares for pets, and assists the home.',
  },
};

// 4 Specific Card-Level Rewards based on completed steps:
export const CARD_STEP_REWARDS = {
  listening: {
    id: 'listening',
    name: 'Sharp Ears',
    badgeEmoji: '🎧',
    desc: 'Completed 3 listening repetitions of native accents.',
    quota: 3,
  },
  watching: {
    id: 'watching',
    name: 'Visual Scholar',
    badgeEmoji: '🎬',
    desc: 'Completed 5 contextual video learning sessions.',
    quota: 5,
  },
  practice: {
    id: 'practice',
    name: 'Master Builder',
    badgeEmoji: '🧩',
    desc: 'Completed 10 active interactive phrase rehearsals.',
    quota: 10,
  },
  speaking: {
    id: 'speaking',
    name: 'Native Voice',
    badgeEmoji: '🎙️',
    desc: 'Recorded 3 verified high-accuracy pronunciations.',
    quota: 3,
  },
};
