# Basic Chatbot

A lightweight deterministic web chatbot built with Flask, HTML, CSS, and vanilla JavaScript. It uses simple pattern matching and no external API, database, or machine-learning framework.

## Setup

```text
python -m venv .chatbot
.chatbot\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000 in a browser.

## API

`POST /chat` accepts `{"message":"hello"}` and returns `{"response":"Hi!"}`. Missing, non-string, and whitespace-only messages receive HTTP 400. Supported rules include greetings, asking how the bot is, goodbye, thanks, help, and the bot's name; other messages receive a deterministic fallback.