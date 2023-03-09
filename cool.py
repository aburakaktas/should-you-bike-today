# get user's location
# get that location's weather data
# get that locations's golden hour time
# display golden hour expected in XX:XX mins (if less than 24 hours)
# else display the next possible golden hour expected
# the logic for golden hour is this: if it is sunny.


import requests


class Weather:
    _base_url = "https://api.openweathermap.org/"

    def __init__(self, location):
        self._location = location
        self._read_api_key()
        self._coordinates = self._get_coordinates()
        self._get_weather()

    # def __init__(self, lat, lon):
    #     self._coordinates = {"lat": lat, "lon": lon}
    #     self._read_api_key()
    #     self._get_weather()

    def _read_api_key(self):
        with open(".apikey") as file:
            self._apikey = file.read()

    def _get_coordinates(self):
        response = requests.get(
            f"{self._base_url}geo/1.0/direct?q={self._location}&appid={self._apikey}")
        response_json = response.json()
        lat = response_json[0]["lat"]
        lon = response_json[0]["lon"]
        return {"lat": lat, "lon": lon}

    def _get_weather(self):
        lat = self._coordinates['lat']
        lon = self._coordinates['lon']
        response = requests.get(
            f"{self._base_url}data/2.5/weather?lat={lat}&lon={lon}&appid={self._apikey}&units=metric")
        response_json = response.json()
        self._degrees = response_json["main"]["temp"]
        self._wind_speed = response_json["wind"]["speed"]
        self._weather_type = response_json["weather"][0]["main"]

    def __str__(self):
        return f"Weather type: {self.weather_type}, Degrees: {self.degrees}, Wind speed: {self.wind_speed}"

    @property
    def degrees(self):
        return self._degrees

    @property
    def wind_speed(self):
        return self._wind_speed

    @property
    def weather_type(self):
        return self._weather_type


def main():
    weather = Weather("Munich")
    print(weather)


if __name__ == "__main__":
    main()
