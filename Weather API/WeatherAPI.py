import requests

def get_weather_by_city(city_name, state_code, units):
    api_key = "YOUR_API_KEY"  # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name},{state_code}&appid={api_key}&units={units}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad responses
        data = response.json()
        display_weather(data)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def get_weather_by_zip(zip_code, units):
    api_key = "YOUR_API_KEY"  # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?zip={zip_code}&appid={api_key}&units={units}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad responses
        data = response.json()
        display_weather(data)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def display_weather(data):
    location = f"{data['name']}, {data['sys']['country']}"
    temperature = data['main']['temp']
    feels_like = data['main']['feels_like']
    temp_min = data['main']['temp_min']
    temp_max = data['main']['temp_max']
    pressure = data['main']['pressure']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']

    print("Weather Forecast:")
    print(f"Location: {location}")
    print(f"Temperature: {temperature}°")
    print(f"Feels Like: {feels_like}°")
    print(f"Min Temperature: {temp_min}°")
    print(f"Max Temperature: {temp_max}°")
    print(f"Pressure: {pressure} hPa")
    print(f"Humidity: {humidity}%")
    print(f"Description: {description}")

def main():
    while True:
        choice = input("What do you want to perform?\n1. City lookup\n2. Zip code lookup\nEnter your choice (1/2): ")
        if choice == '1':
            city_name = input("Enter city name: ")
            state_code = input("Enter state code (optional, leave empty if not applicable): ")
            units = input("Choose temperature unit (Celsius, Fahrenheit, or Kelvin): ").lower()
            if units not in ['celsius', 'fahrenheit', 'kelvin']:
                print("Invalid temperature unit. Please choose from Celsius, Fahrenheit, or Kelvin.")
                continue
            units = 'metric' if units == 'celsius' else 'imperial'
            get_weather_by_city(city_name, state_code, units)
        elif choice == '2':
            zip_code = input("Enter zip code: ")
            units = input("Choose temperature unit (Celsius, Fahrenheit, or Kelvin): ").lower()
            if units not in ['celsius', 'fahrenheit', 'kelvin']:
                print("Invalid temperature unit. Please choose from Celsius, Fahrenheit, or Kelvin.")
                continue
            units = 'metric' if units == 'celsius' else 'imperial'
            get_weather_by_zip(zip_code, units)
        else:
            print("Invalid choice. Please enter either 1 or 2.")

        another_query = input("Do you want to perform another query? (yes/no): ")
        if another_query.lower() != 'yes':
            break

if __name__ == "__main__":
    main()