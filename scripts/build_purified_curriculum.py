import json
import re
import os
import sys

sys.path.append(os.path.dirname(__file__))
from helper import item

# Load cleaned single word items
with open('src/data/multilingual/topicSingleWordItems.ts', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('export const TOPIC_SINGLE_WORD_ITEMS')
start = text.find('{', idx)
end = text.find('};', start) + 1
single_words = json.loads(text[start:end])

# Load W1 and W2 items
w1_all = {}
w2_all = {}
for cat_name in ['cat1_home_family_travel', 'cat2_shopping_health_school', 'cat3_friends_nature_manners', 'cat4_tech_weather_holidays', 'cat5_sports_clothes_chores']:
    path = f'src/data/multilingual/{cat_name}.ts'
    with open(path, 'r', encoding='utf-8') as f:
        c_text = f.read()
    
    m1 = re.search(r'export const CAT\d_W1[^{]+=\s*(\{[\s\S]*?\n\};)', c_text)
    if m1:
        w1_all.update(json.loads(m1.group(1).rstrip(';')))
    
    m2 = re.search(r'export const CAT\d_W2[^{]+=\s*(\{[\s\S]*?\n\};)', c_text)
    if m2:
        w2_all.update(json.loads(m2.group(1).rstrip(';')))

with open('src/data/topics.ts', 'r', encoding='utf-8') as f:
    topics_text = f.read()

topic_matches = re.findall(r'id:\s*[\'\"]([^\'\"]+)[\'\"]', topics_text)
all_topic_ids = list(dict.fromkeys(topic_matches))

w4_data = {}
tier2_data = {}
tier3_data = {}

print(f"Loaded {len(all_topic_ids)} topics, {len(single_words)} single word topics, {len(w1_all)} W1 topics.")
