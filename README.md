# FaceCheck Bot Project

## Overview

This project implements a Telegram bot that interfaces with the FaceCheck ID API to search for image occurrences. The project also includes a RESTful API and database integration.

## Project Structure

facecheck_bot_project/
│
├── bot/
│   ├── __init__.py
│   ├── bot.py
│   ├── handlers.py
│   ├── messages.py
│   └── utils.py
│
├── api/
│   ├── __init__.py
│   ├── app.py
│   ├── database.py
│   ├── models.py
│   └── utils.py
│
├── database/
│   ├── __init__.py
│   ├── models.py
│   └── operations.py
│
├── tests/
│   ├── __init__.py
│   ├── test_bot.py
│   ├── test_api.py
│   ├── test_database.py
│   └── test_utils.py
│
├── config.py
├── requirements.txt
├── README.md
└── .gitignore



## Setup

1. Clone the repository.
2. Install the dependencies:
   ```sh
   pip install -r requirements.txt

3. Set up environment variables for TELEGRAM_TOKEN and DATABASE_URI

## Usage
## Running the Telegram Bot

python -m bot.bot



