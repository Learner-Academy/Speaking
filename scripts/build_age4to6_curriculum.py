import json
import re

# Load topicSingleWordItems
with open('src/data/multilingual/topicSingleWordItems.ts', 'r', encoding='utf-8') as f:
    s_text = f.read()

# Load cat1 to cat5 to have exact access to W1 and W2 items
cats = ['cat1_home_family_travel', 'cat2_shopping_health_school', 'cat3_friends_nature_manners', 'cat4_tech_weather_holidays', 'cat5_sports_clothes_chores']

print("Ready to parse and generate Age 4-6 datasets")
