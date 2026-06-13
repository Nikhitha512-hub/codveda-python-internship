import requests

print("=== Weather Application ===")

city = input("Enter city name: ")

url = f"https://wttr.in/{city}?format=j1"

try:
    response = requests.get(url)

    # Check if request was successful
    if response.status_code == 200:

        data = response.json()

        temperature = data["current_condition"][0]["temp_C"]
        humidity = data["current_condition"][0]["humidity"]
        condition = data["current_condition"][0]["weatherDesc"][0]["value"]

        print("\nWeather Details")
        print("---------------------")
        print("City:", city)
        print("Temperature:", temperature, "°C")
        print("Humidity:", humidity, "%")
        print("Condition:", condition)

    else:
        print("Failed to fetch weather data.")

except Exception as e:
    print("An error occurred:", e)