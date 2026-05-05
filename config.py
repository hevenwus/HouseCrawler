
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

REQUEST_DELAY = 1

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

OUTPUT_DIR = os.path.join(BASE_DIR, 'data')

os.makedirs(OUTPUT_DIR, exist_ok=True)

