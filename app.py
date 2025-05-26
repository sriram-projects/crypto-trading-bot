# app.py
from flask import Flask, render_template, request
from bot import place_market_order  # 👈 link to bot.py

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    message = None
    result = {}
    
    if request.method == 'POST':
        side = request.form['side']
        quantity = request.form['quantity']
        
        order = place_market_order('BTCUSDT', side.upper(), float(quantity))

        
        if 'error' in order:
            message = "❌ Error placing order:"
            result = order['error']
        else:
            message = "✅ Order placed successfully!"
            result = order

    return render_template('index.html', message=message, result=result)

if __name__ == '__main__':
    app.run(debug=True)
