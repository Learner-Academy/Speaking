import sys
import os
import json
import re

sys.path.append(os.path.dirname(__file__))
from helper import item
from data_cat1 import w4 as cat1_w4, tier2 as cat1_t2, tier3 as cat1_t3
from dedicated_topics import w4_special, tier2_special, tier3_special

print(f"Cat1 topics: {len(cat1_w4)}")
print(f"Dedicated topics: {len(w4_special)}")
