import requests, json
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

my_API_key = os.getenv('API_KEY')


def get_weather(city):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={my_API_key}')
    return response.json()

def weather_info(city):
    details = get_weather(city)

    # Check for errors in the API response
    if details.get('cod') != 200:
        print("Error:", details.get('message', 'Could not retrieve weather data.'))
        return None

    # Prepare the weather information
    weather_info = {
        "City": details['name'],
        "Country": details['sys']['country'],
        "Temperature": f"{details['main']['temp'] - 273.15:.2f} °C",
        "Feels Like": f"{details['main']['feels_like'] - 273.15:.2f} °C",
        "Humidity": f"{details['main']['humidity']}%",
        "Description": details['weather'][0]['description'],
        "Wind Speed": f"{details['wind']['speed']} m/s",
        "Cloudiness": f"{details['clouds']['all']}%",
        "Sunrise": datetime.fromtimestamp(details['sys']['sunrise']).strftime('%Y-%m-%d %H:%M:%S'),
        "Sunset": datetime.fromtimestamp(details['sys']['sunset']).strftime('%Y-%m-%d %H:%M:%S')
    }

    # Print the weather details
    print("Weather Details:")
    print("-----------------")
    for key, value in weather_info.items():
        print(f"{key}: {value}")
    print("-----------------")

    return weather_info

if __name__ == "__main__":
    city = input("Enter the city name: ")
    weather_info(city)

    
    