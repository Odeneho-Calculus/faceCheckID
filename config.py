# config.py

import os

class Config:
    TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN', 'your-telegram-bot-token')
    DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///facecheck_bot.db')
