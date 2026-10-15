import os
import json
import re

# We will generate comprehensive Age 4-6 authentic sentences for all 77 topics.
# Each topic will have:
# - w4: exactly 3 words per item (Item 1, 2, 3)
# - tier2: exactly 4 to 5 words per item (Item 1, 2, 3)
# - tier3: exactly 5 to 6 words per item (Item 1, 2, 3)
# All across 15 languages: en, ur, hi, ar, es, fr, de, it, pt, ru, tr, id, zh, ja, ko.

from helper import item

# Load topics from topics.ts
with open('src/data/topics.ts', 'r', encoding='utf-8') as f:
    topics_text = f.read()

topic_matches = re.findall(r'id:\s*[\'\"]([^\'\"]+)[\'\"]', topics_text)
all_topic_ids = list(dict.fromkeys(topic_matches))

print(f"Loaded {len(all_topic_ids)} topics.")
