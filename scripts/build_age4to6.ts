import * as fs from 'fs';
import * as path from 'path';
import { TOPIC_SINGLE_WORD_ITEMS } from '../src/data/multilingual/topicSingleWordItems';
import { TOPIC_TWO_WORD_ITEMS_W1, TOPIC_TWO_WORD_ITEMS_W2 } from '../src/data/topicTwoWordItems';
import { TOPIC_SCENARIOS } from '../src/data/topics';
import { LanguageCode } from '../src/types';

interface ItemBundle {
  en: string;
  ur: string;
  ur_rom: string;
  es: string;
  es_rom: string;
  target: Record<LanguageCode, string>;
  romanized: Record<LanguageCode, string>;
}

console.log('Testing script loading...');
