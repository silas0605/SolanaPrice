
# SolanaPrice Telegram Bot

Telegram bot that notifies you about the Solana (SOL) price in real-time.

## Overview

This project is a simple Telegram bot built with Python that fetches the current price of Solana (SOL) and sends notifications or updates to a Telegram chat. It can be used to keep track of SOL price movements conveniently via Telegram messages.

## Features

- Fetches Solana price from a public API
- Sends price notifications to Telegram users or groups
- Easy to configure and run
- Lightweight and minimal dependencies

## Requirements

- Python 3.7 or higher
- `python-telegram-bot` library
- `requests` library

## Installation

1. Clone the repository:

```
git clone https://github.com/silas0605/SolanaPrice.git
cd SolanaPrice
```

2. Install dependencies:

```
pip install -r requirements.txt
```

*If `requirements.txt` is not available, install manually:*

```
pip install python-telegram-bot requests
```

## Setup

1. Create a Telegram bot via [BotFather](https://t.me/BotFather) and get your bot token.
2. Obtain your Telegram chat ID (can be your user ID or group ID).
3. Configure the bot token and chat ID in the script or environment variables.

## Usage

Run the bot script:

```
python bot.py
```

The bot will start and send Solana price updates to the configured Telegram chat.

## Customization

- You can customize the frequency of price checks and notifications.
- Modify the API endpoint if you want to use a different price source.
- Extend the bot to send alerts based on price thresholds or changes.

## License

