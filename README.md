# Trading Bot

Simple Python CLI trading bot using Binance Futures Testnet.

## Setup
pip3 install -r requirements.txt

Create .env:
API_KEY=your_key
API_SECRET=your_secret

## Run

Market:
python3 cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

Limit:
python3 cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 75000

## Features
- MARKET & LIMIT orders
- BUY / SELL
- CLI input
- Logging