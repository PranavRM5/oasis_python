import requests
import json

def weather_App(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}  # You can change units to imperial for Fahrenheit

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            print(f"Weather in {city}:")
            print(f"Temperature: {data['main']['temp']}°C")
            print(f"Humidity: {data['main']['humidity']}%")
            print(f"Conditions: {data['weather'][0]['description']}")
        else:
            print(f"Error: {data['message']}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    api_key = "179a85928546c2d7edd22f8253ef9fab"
    city = input("Enter the city name: ")

    weather_App(api_key, city)

