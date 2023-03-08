# get user's location
# get that location's weather data
# get that locations's golden hour time
# display golden hour expected in XX:XX mins (if less than 24 hours)
# else display the next possible golden hour expected
# the logic for golden hour is this: if it is sunny. 



import requests
import json
API_KEY = "2b0aa93a8746baccdb80c423dc53b631"


class Weather:
    
    def __init__(self, degrees, wind_speed, weather_type):
        self._degrees = degrees
        self._wind_speed = wind_speed
        self._weather_type = weather_type
       
    # @classmethod 
    # def get(cls):
    #     degrees = 
        
    def __str__(self):
        return f"Weather type: {self._weather_type}, Degrees: {self._degrees}, Wind speed: {self._wind_speed}"
    



def main():    
    coordinates = get_coordinates("tokyo")
    print(get_weather(coordinates))
    

def get_coordinates(city_name):
    # should return coordinates from a city name
    headers = {'Accept': 'application/json'}
    response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={API_KEY}", headers=headers)
    response_json = response.json()
    lat = response_json[0]["lat"]
    long = response_json[0]["lon"]
    return {"lat": lat, "long": long}
    
def get_weather(coordinates):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={coordinates['lat']}&lon={coordinates['long']}&appid={API_KEY}&units=metric")
    response_json = response.json()
    degrees = response_json["main"]["temp"]
    wind_speed = response_json["wind"]["speed"]
    weather_type = response_json["weather"][0]["main"]
    weather = Weather(degrees=degrees, wind_speed=wind_speed, weather_type=weather_type)
    return weather
    




if __name__ == "__main__":
    main()