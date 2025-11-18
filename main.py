import requests

api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
base_url = "http://api.openweathermap.org/data/2.5/weather?"

somali_cities = ["Mogadishu", "Hargeisa", "Garowe", "Kismayo", "Baidoa", "Barawe", "Galkayo", "Bossaso", "Berbera", "Merca"]

print("Somali Cities:", ", ".join(somali_cities))

# Loop until user enters a valid city
while True:
    city = input("Enter a Somali city from the list above: ").title()
    if city in somali_cities:
        break
    print("City not recognized. Make sure to choose from the list!")

complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"

try:
    response = requests.get(complete_url)
    data = response.json()

    if str(data.get("cod")) != "200":
        print(f"Error: {data.get('message', 'Unable to fetch weather data')}")
    else:
        main = data["main"]
        weather = data["weather"][0]
        print(f"\nCity: {data['name']}, {data['sys']['country']}")
        print(f"Temperature: {main['temp']} °C")
        print(f"Weather: {weather['description']}")
        print(f"Humidity: {main['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")

except requests.exceptions.RequestException as e:
    print("Network error:", e)
