import requests

# Заголовки запроса
headers = {
    'Content-Type': 'application/json',
    'X-CSRFToken': 'HR1IMOHGzBrq57rvEpXdcZknFeyZNFWM',
}

cookies = {
    'csrftoken': 'HR1IMOHGzBrq57rvEpXdcZknFeyZNFWM',
    'sessionid': '2zp5zpq7dzyxle42mu6s8et7hyq9kfik',
}

# Тело запроса
payload = {
    "player": 1,
    "money": 1200,
    "total_clicks": 706,
    "click_power": 3,
    "passive_power": 0
}

try:
    response = requests.patch(
        'http://127.0.0.1:8000/api/v0/stats/',
        cookies=cookies,
        headers=headers,
        json=payload,  # Используем json= для отправки данных как JSON
    )
    print(response.status_code)
    print(response.text)
except Exception as e:
    print(f'Ошибка запроса: {e}')