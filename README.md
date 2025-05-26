# 💼 Crypto Trading Bot – Internship Assignment

This is a simple Binance Futures trading bot built using **Python** and **Flask**.  
It allows users to place **BUY** or **SELL** market orders through a web interface using the Binance **Testnet API**.


## 🚀 Features

- Web interface built with Flask
- Market order execution (Buy/Sell)
- Binance Futures Testnet integration
- Input quantity and order type
- Error handling and success message display

## 📁 Folder Structure

crypto-trading-bot/
├── app.py # Flask app
├── bot.py # Binance API logic
├── templates/
│ └── index.html # Frontend UI
├── requirements.txt # Python libraries
├── README.md # Project documentation
└── log.txt # Sample logs


---

## 🛠️ How to Run the Project

1. **Clone or Download**
    ```
    git clone https://github.com/sriram-projects/crypto-trading-bot.git
    cd crypto-trading-bot
    ```

2. **Install Dependencies**
    ```
    pip install -r requirements.txt
    ```

3. **Configure Binance Testnet API Keys**
    - Register at [Binance Futures Testnet](https://testnet.binancefuture.com)
    - Replace `API_KEY` and `API_SECRET` in `bot.py` with your keys

4. **Run the Application**
    ```
    python app.py
    ```
    - Open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser


## 🧑‍💻 For Freshers

This project is ideal for beginners to demonstrate:

- **Python programming**
- **Flask web development**
- **REST API usage (Binance)**
- **Basic error handling and UI integration**


## 📜 License

MIT


