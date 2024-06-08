# FaceCheck Bot Project

## Overview

This project implements a Telegram bot that interfaces with the FaceCheck ID API to search for image occurrences. The project also includes a RESTful API and database integration.

The project is structured as follows:

- `bot/`: Contains functionality related to the bot.
- `api/`: Contains functionality related to the API.
- `database/`: Contains database-related functionality.
- `tests/`: Contains test cases for the project.
- `config.py`: Configuration file.
- `requirements.txt`: File listing project dependencies.
- `README.md`: This file.
- `.gitignore`: Git ignore file.

## Detailed Structure

### bot/

- `bot.py`: Main bot functionality.
- `handlers.py`: Handlers for bot commands.
- `messages.py`: Bot messages.
- `utils.py`: Utility functions for the bot.

### api/

- `app.py`: Main API functionality.
- `database.py`: Database handling for the API.
- `models.py`: API models.
- `utils.py`: Utility functions for the API.

### database/

- `models.py`: Database models.
- `operations.py`: Database operations.

### tests/

- `test_bot.py`: Tests for bot functionality.
- `test_api.py`: Tests for API functionality.
- `test_database.py`: Tests for database functionality.
- `test_utils.py`: Tests for utility functions.

## Configuration

- `config.py`: Configuration settings for the project.

## Dependencies

To install project dependencies, run:

## Setup

1. Clone the repository.
2. Install the dependencies:
   ```sh
   pip install -r requirements.txt

3. Set up environment variables for TELEGRAM_TOKEN and DATABASE_URI

## Usage
## Running the Telegram Bot

python -m bot.bot



