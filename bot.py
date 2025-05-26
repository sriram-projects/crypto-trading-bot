# bot.py
from binance.client import Client

API_KEY = 'iPB7hYKiXjZKe6zPwffaxXOA6Taneo3HAUiH28k3Ov1glkKRGByKnjyEVB6S9Tyh'
API_SECRET = 'your_ciktH5UADf9bHkppxDlXlqUrkDmbMs5dsObN7c7E6OtifR7ipggudwoaOF8EjWEo'

client = Client(API_KEY, API_SECRET,testnet = True)
client.FUTURES_URL = 'https://testnet.binancefuture.com'

def place_market_order(symbol, side, quantity):
    try:
        order = client.futures_create_order(
            symbol= "BTCUSDT",
            side=side,
            type='MARKET',
            quantity=quantity
        )
        return order
    except Exception as e:
        return {"error": str(e)}
