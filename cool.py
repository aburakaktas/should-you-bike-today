# get user's location
# get that location's weather data
# get that locations's golden hour time
# display golden hour expected in XX:XX mins (if less than 24 hours)
# else display the next possible golden hour expected
# the logic for golden hour is this: if it is sunny. 



import requests
import json


API_KEY = "2b0aa93a8746baccdb80c423dc53b631"

def main():    
    

    print(get_coordinates("Munich"))

def get_coordinates(city_name):
    # should return coordinates from a city name
    headers = {'Accept': 'application/json'}
    response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid=2b0aa93a8746baccdb80c423dc53b631", headers=headers)
    lat = response.json()[0]["lat"]
    long = response.json()[0]["lon"]
    
    return {"lat": lat, "long": long}
    
    




if __name__ == "__main__":
    main()