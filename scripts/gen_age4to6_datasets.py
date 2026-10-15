# scripts/gen_age4to6_datasets.py
# Generates authentic, natural spoken child speech datasets for Age 4-6
# Across all 15 languages and all 77 topics.
# Strictly zero literal translation.

import os
import sys
import json
import re

sys.path.append(os.path.dirname(__file__))
from helper import item

# Load all 77 topics
with open('src/data/topics.ts', 'r', encoding='utf-8') as f:
    topics_text = f.read()

topic_matches = re.findall(r'id:\s*[\'\"]([^\'\"]+)[\'\"]', topics_text)
all_topic_ids = list(dict.fromkeys(topic_matches))
print(f"Total topics to process: {len(all_topic_ids)}")
