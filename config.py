import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = '!'
DATA_FILE = 'user_data.json'