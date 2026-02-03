import requests
import json
import time
#This is for the PR testing procedure
# Replace 'your_actual_api_key_here' with your actual OpenWeatherMap API key
api_key = 'be01239f377a214b1fb7b6fa3dbd1841'

# Function to fetch weather data by coordinates (latitude and longitude)
def get_weather_by_coordinates(latitude, longitude):
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    
    # Create a dictionary with the parameters for the API request
    params = {
        'lat': latitude,
        'lon': longitude,
        'appid': api_key,
        'units': 'metric'  # You can change units to 'imperial' for Fahrenheit
    }
    
    try:
        # Send a GET request to the OpenWeatherMap API
        response = requests.get(base_url, params=params)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            weather_data = response.json()
            return weather_data
        else:
            print("Error fetching weather data. Status code:", response.status_code)
    except Exception as e:
        print("An error occurred:", str(e))

# Function to convert degrees to a cardinal direction (e.g., 45 degrees to 'NE')
def degrees_to_cardinal(degrees):
    directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    index = round(degrees / 45) % 8
    return directions[index]

# Function to continuously stream weather data
def stream_weather_data(latitude, longitude, interval):
    while True:
        weather_data = get_weather_by_coordinates(latitude, longitude)
        
        if weather_data:
            # Extract and display relevant weather information
            temperature = weather_data['main']['temp']
            description = weather_data['weather'][0]['description']
            humidity = weather_data['main']['humidity']
            wind_speed = weather_data['wind']['speed']
            wind_direction_degrees = weather_data['wind']['deg']
            wind_direction = degrees_to_cardinal(wind_direction_degrees)
            
            print("\nWeather at coordinates:")
            print(f"Latitude: {latitude}")
            print(f"Longitude: {longitude}")
            print(f"Temperature: {temperature}°C")
            print(f"Description: {description}")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} m/s")
            print(f"Wind Direction: {wind_direction}")
        
        # Wait for the specified interval before fetching the next data
        time.sleep(interval)

# Main program
if __name__ == '__main__':
    # Input latitude and longitude coordinates
    latitude = float(input("Enter latitude: "))
    longitude = float(input("Enter longitude: "))
    
    # Input the streaming interval (in seconds)
    interval = int(input("Enter streaming interval (in seconds): "))
    
    print("Live Weather Streaming:")
    stream_weather_data(latitude, longitude, interval)

