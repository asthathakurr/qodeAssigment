import time
import random
from datetime import datetime

def random_delay(min_s=1, max_s=3):
    time.sleep(random.uniform(min_s, max_s))

def clean_text(t):
    return t.replace('\n', ' ').strip()

def ts():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
