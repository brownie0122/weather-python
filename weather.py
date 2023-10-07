import requests
import json

# Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
api_key = '385adecfef41e09d4641e51e129df2af'

# Function to get weather data
def get_weather(city_name):
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
    response = requests.get(base_url)

    if response.status_code == 200:
        data = response.json()
        main_data = data['main']
        weather_info = data['weather'][0]
        temperature = main_data['temp']
        humidity = main_data['humidity']
        description = weather_info['description']

        print(f'Weather in {city_name}:')
        print(f'Temperature: {temperature}°C')
        print(f'Humidity: {humidity}%')
        print(f'Description: {description}')
    else:
        print('Failed to retrieve weather data.')

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
