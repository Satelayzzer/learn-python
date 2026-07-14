import requests

url = "https://cropio.com/api/v3/sign_in"

payload = {
    "user_login": {
        "email": "ny@sasagro.com",
        "password": "123456",
    }
}

headers = {
    "Content-Type": "application/json",
}

try:
    response = requests.post(
        url,
        json=payload,
        headers=headers,
        timeout=30,
        allow_redirects=True,
    )

    response.raise_for_status()

    print("Status code:", response.status_code)

    try:
        print("Response:", response.json())
    except ValueError:
        print("Response:", response.text)

except requests.RequestException as error:
    print("Помилка запиту:", error)