import requests
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Access environment variables
api_key = os.getenv('API_KEY')

def APICall(city):
    url = f"https://api.weatherstack.com/current?access_key={api_key}"
    querystring = {"query": city, "units": "f"}  

    response = requests.get(url, params=querystring)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None


def CompareRequest():
    while True:
        # Gets cities, use default if user does not enter anything
        city1 = input("\nEnter the first city (New York City, New York): ").strip()
        if not city1:
            city1 = "New York City, New York"

        city2 = input("Enter the second city (Santa Monica, California): ").strip()
        if not city2:
            city2 = "Santa Monica, California"

        data1 = APICall(city1)
        data2 = APICall(city2)
        
        if data1 is None or data2 is None:
            print("Error fetching data for one or both cities. Please try again.")
            continue  # Re-prompt if there was an error

        
        temp1 = data1['current']['temperature']
        temp2 = data2['current']['temperature']
    
        # Calculate temperature difference
        temp_difference = abs(temp1 - temp2)

        
        print(f"\nTemperature in {data1['location']['name']}: {temp1} F")
        print(f"Temperature in {data2['location']['name']}: {temp2} F")
        print(f"\nTemperature difference: {temp_difference} F")

        # Ask the user if they want to search again
        redo = input("\nWould you like to compare another pair of cities? (Y/N): ").strip().lower()

        if redo != 'y':
            os.system('cls' if os.name == 'nt' else 'clear')
            break
