\# Binance Futures Trading Bot (Testnet)



\## Setup



1\. Clone repo

2\. Install dependencies:

&#x20;  pip install -r requirements.txt



3\. Create .env file with API keys



\## Run Examples



\### Market Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001



\### Limit Order

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000



\## Features

\- Market \& Limit orders

\- BUY / SELL support

\- CLI input

\- Logging

\- Error handling



\## Assumptions

\- Using Binance Futures Testnet

\- Valid API keys required

