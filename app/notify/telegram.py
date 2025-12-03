import requests

def send_backup(bot_token: str, chat_id: int | str, link: str, time: str):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    data = {
        "chat_id": chat_id,
        "text": f"♿️ Бекап за {time}\n\n{link}",
    }

    response = requests.post(url, data=data)
    response.raise_for_status()
    return response.json()