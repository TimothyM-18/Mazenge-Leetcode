import requests

url = "https://api.coingecko.com/api/v3/simple/price"

params = {
    "ids": "bitcoin,ethereum",
    "vs_currencies": "usd"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    for coin, values in data.items():
        price = values.get("usd", "N/A")
        print(f"{coin.capitalize()} price: ${price}")
else:
    print("API request failed:", response.status_code)
