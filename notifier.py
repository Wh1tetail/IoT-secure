import requests

TELEGRAM_TOKEN = '7558201647:AAFqHyW459oltCuFFTgosh1iEvG6vpoVP4M'
TELEGRAM_CHAT_ID = '1223399167' 

def send_alert_to_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    try:
        response = requests.post(url, data=payload)
        if response.status_code != 200:
            print(f"[ERROR] Telegram error: {response.text}")
    except Exception as e:
        print(f"[ERROR] Exception sending to Telegram: {e}")