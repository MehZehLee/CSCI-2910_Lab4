import requests
import os
from dotenv import load_dotenv


# Load environment variables from the .env file
load_dotenv()
# Access environment variables
api_key = os.getenv('API_KEY')

def APICall():
    url = f"https://api.weatherstack.com/current?access_key={api_key}" 
    city = input("\nEnter Location in this format (Johnson City, Tennessee): ").strip()

    # Use default city if no input is provided
    if not city:
        city = "Johnson City, Tennessee"

    querystring = {"query": city, "units": "f"} 

    response = requests.get(url, params=querystring)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

def WeatherInfo():
    while True:
        data = APICall()
        
        if data is None:
            print("Error fetching data. Please try again.")
            continue 

        output = {
            '\nLocation': f"{data['location']['name']}, {data['location']['region']}",
            'Local Time': data['location']['localtime'].split(" ")[1],
            'Temperature': f"{data['current']['temperature']} F",
            'Feels Like': f"{data['current']['feelslike']} F",
            'Weather Description': data['current']['weather_descriptions'][0],
            'Visibility': f"{data['current']['visibility']}/10",
            'Wind Speed': f"{data['current']['wind_speed']} mph", 
            'Wind Direction': data['current']['wind_dir'],
            'Pressure': data['current']['pressure'],
            'Precip': data['current']['precip'],
            'Humidity': f"{data['current']['humidity']}%",
            'Cloud Cover': f"{data['current']['cloudcover']}%",
            'UV Index': f"{data['current']['uv_index']}/10"
        }

        # Formatting output
        formatted_output = "\n".join([f"{key}: {value}" for key, value in output.items()])
        print(formatted_output)

        # Ask the user if they want to search again
        redo = input("\nWould you like to search again? (Y/N): ").strip().lower()

        if redo != 'y':
            os.system('cls' if os.name == 'nt' else 'clear')
            break
