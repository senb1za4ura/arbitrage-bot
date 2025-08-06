import os
import time
from datetime import datetime
from kucoin.client import Market as KucoinMarket
from pybit.unified_trading import HTTP as BybitClient
from gate_api import SpotApi, Configuration as GateConfiguration
from mexc_sdk import Spot as MEXCClient
from telegram import Bot
from dotenv import load_dotenv

# Загрузка переменных из .env файла
load_dotenv()

# Получение API-ключей из переменных окружения
KUCOIN_API_KEY = os.getenv("KUCOIN_API_KEY")
KUCOIN_API_SECRET = os.getenv("KUCOIN_API_SECRET")
KUCOIN_PASSPHRASE = os.getenv("KUCOIN_PASSPHRASE")

BYBIT_API_KEY = os.getenv("BYBIT_API_KEY")
BYBIT_API_SECRET = os.getenv("BYBIT_API_SECRET")

GATE_API_KEY = os.getenv("GATE_API_KEY")
GATE_API_SECRET = os.getenv("GATE_API_SECRET")

MEXC_API_KEY = os.getenv("MEXC_API_KEY")
MEXC_API_SECRET = os.getenv("MEXC_API_SECRET")

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Примеры инициализации клиентов
kucoin = KucoinMarket(key=KUCOIN_API_KEY, secret=KUCOIN_API_SECRET, passphrase=KUCOIN_PASSPHRASE)
bybit = BybitClient(api_key=BYBIT_API_KEY, api_secret=BYBIT_API_SECRET)

gate_conf = GateConfiguration()
gate_conf.key = GATE_API_KEY
gate_conf.secret = GATE_API_SECRET
gate = SpotApi(configuration=gate_conf)

mexc = MEXCClient(api_key=MEXC_API_KEY, api_secret=MEXC_API_SECRET)

bot = Bot(token=TELEGRAM_TOKEN)

# Пример функции отправки сообщения
def send_message(message):
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)

# Пример запуска
if __name__ == "__main__":
    send_message("✅ Бот успешно запущен!")

    while True:
        now = datetime.now().strftime("%H:%M:%S")
        print(f"[{now}] Бот работает...")
        time.sleep(30)
