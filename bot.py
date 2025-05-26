from binance.client import Client
import datetime

API_KEY = 'iPB7hYKiXjZKe6zPwffaxXOA6Taneo3HAUiH28k3Ov1glkKRGByKnjyEVB6S9Tyh'
API_SECRET = 'your_ciktH5UADf9bHkppxDlXlqUrkDmbMs5dsObN7c7E6OtifR7ipggudwoaOF8EjWEo'

client = Client(API_KEY, API_SECRET, testnet=True)
client.FUTURES_URL = 'https://testnet.binancefuture.com'

# Log function
def log_event(message):
    with open("log.txt", "a") as f:
        f.write(f"[{datetime.datetime.now()}] {message}\n")

def place_market_order(symbol, side, quantity):
    try:
        log_event(f"Placing order: symbol={symbol}, side={side}, quantity={quantity}")
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type='MARKET',
            quantity=quantity
        )
        log_event(f"Order response: {order}")
        return order
    except Exception as e:
        log_event(f"ERROR: {str(e)}")
        return {"error": str(e)}
