# Dedicated script to generate high-fidelity, natural child speech curriculum for all 77 topics for Age 4-6
import json
import re
import os
import sys

sys.path.append(os.path.dirname(__file__))
from helper import item

# Load clean single word items
with open('src/data/multilingual/topicSingleWordItems.ts', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'TOPIC_SINGLE_WORD_ITEMS[^{]+=\s*(\{[\s\S]*?\n\};)', text)
single_words = json.loads(m.group(1).rstrip(';'))

with open('src/data/topics.ts', 'r', encoding='utf-8') as f:
    topics_text = f.read()

topic_matches = re.findall(r'id:\s*[\'\"]([^\'\"]+)[\'\"]', topics_text)
all_topic_ids = list(dict.fromkeys(topic_matches))
print(f"Loaded {len(all_topic_ids)} topics.")
