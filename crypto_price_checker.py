import requests

print("=== Cryptocurrency Price Checker ===")

crypto = input("Enter cryptocurrency name (bitcoin/ethereum/dogecoin): ").lower()

url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd"

try:
    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        if crypto in data:
            price = data[crypto]["usd"]

            print("\nCryptocurrency:", crypto.capitalize())
            print("Current Price: $", price)

        else:
            print("Cryptocurrency not found.")

    else:
        print("Failed to fetch data.")

except Exception as e:
    print("An error occurred:", e)