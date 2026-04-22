from binance.client import Client
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="bot.env")

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

def get_client():
    if not API_KEY or not API_SECRET:
        raise ValueError("API keys not found in .env file")

    client = Client(API_KEY, API_SECRET)
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
    return client