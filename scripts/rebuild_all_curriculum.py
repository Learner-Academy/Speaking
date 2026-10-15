import re
import json
import os
import sys

sys.path.append(os.path.dirname(__file__))
from helper import item

# We will generate comprehensive, authentic, native child sentences for all 77 topics
# strictly adhering to:
# W4 (Days 22 to 30): exactly 3 words per item
# Tier 2 (Days 31 to 60): exactly 4 to 5 words per item
# Tier 3 (Days 61 to 90): exactly 5 to 6 words per item
# Across all 15 languages: en, ur, hi, ar, es, fr, de, it, pt, ru, tr, id, zh, ja, ko.

# Let's verify topicSingleWordItems.ts is our source of truth for single words
with open('src/data/multilingual/topicSingleWordItems.ts', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'TOPIC_SINGLE_WORD_ITEMS[^{]+=\s*(\{[\s\S]*?\n\};)', text)
single_words = json.loads(m.group(1).rstrip(';'))

with open('src/data/topics.ts', 'r', encoding='utf-8') as f:
    topics_text = f.read()

topic_matches = re.findall(r'id:\s*[\'\"]([^\'\"]+)[\'\"]', topics_text)
all_topic_ids = list(dict.fromkeys(topic_matches))
print(f"Total topics: {len(all_topic_ids)}")

w4_data = {}
tier2_data = {}
tier3_data = {}

# We define dedicated, pristine items for all topics.
# Let's import our dedicated dictionaries or generate clean structures.
