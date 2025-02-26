## Telegram Currency & Crypto Bot

This Telegram Bot uses Python, and pyTelegramBotAPI library.  

## Installation

If you want to run it locally, you need to follow these steps.

```js

pip install pyTelegramBotAPI
pip install requests
python main.py

``` 

 - After that, you need a Telegram Bot Secret key. Find @BotFather on
   Telegram, and create a bot and get the secret key.
   Then, fill the **"telegramkey"** string in **"keys.py"**.

 - If you want to get Gas Price on Ethereum Chain, you need to get a
   Etherscan API key from etherscan.io.
   Then, fill the **"etherscankey"** string in **"keys.py"**.

## Lists

In **"lists.py",** you can see the lists of coins or keywords. They can be adjustable, if you want to follow other coins & currencies' prices, you can change it, or you can change the structure completely. If you want, you can add other exchanges' APIs and lists to use it in bot. 

## Usage 

Usage is typing the symbol of the currency in chat without slash. Examples: BTC, ETH, USD, BNB, USDT, EUR, GAS

## Extra Commands

If you want to check Top 5 gainers or losers on Binance, you can type **gainers** or **losers**.