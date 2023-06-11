from weather import Weather
from astral.sun import sun, golden_hour
from astral import LocationInfo, SunDirection
from timezonefinder import TimezoneFinder
import re
import argparse



class Result:
    _main_result = None
    _wind_warning = None

    @property
    def main_result(self):
        return self._main_result

    @main_result.setter
    def main_result(self, value):
        self._main_result = value

    @property
    def wind_warning(self):
        return self._wind_warning

    @wind_warning.setter
    def wind_warning(self, value):
        self._wind_warning = value


def decide_result(degrees, weather_type, wind_speed, location):
    result = Result()
    if degrees >= 20:
        result.main_result = True
    elif degrees > 15 and degrees < 20:
        if weather_type == "Rain":
            result.main_result = False
        else:
            result.main_result = True
    elif degrees > 0:
        if weather_type != "Clear":
            result.main_result = False
        else:
            result.main_result = True

    if wind_speed > 10:
        result.wind_warning = True
    else:
        result.wind_warning = False

    return f"Is it cycling weather in {location}?\n- {'Yes!' if result.main_result else 'No.'} It is {degrees} degrees and weather type is: {weather_type}.\nShould I care about wind?\n- {'Yes.' if result.wind_warning else 'No!'} Wind speed is {wind_speed} km/h."


def find_time_zone(lat, lon):
    timeZoneFinder = TimezoneFinder()
    return timeZoneFinder.timezone_at(lng=lon, lat=lat)
    

def extract_time(s):
    pattern = r" (.*)\:..\."
    result = re.findall(pattern, s)
    return result[0]
    

def main():
    
    # create the optional command line argument to override location
    parser = argparse.ArgumentParser(description="Is it worth biking today?")
    parser.add_argument("-l", default="Munich", help="location", type=str)
    args = parser.parse_args()
    loc = args.l
    
    # ask user to enter 
    weather = Weather(loc)
    
    # get time zone based on coordinates
    timeZone = find_time_zone(weather.coordinates["lat"], weather.coordinates["lon"])
    
    # get city info based on time zone and coordinates
    city = LocationInfo(name=weather.location, region=weather.region, timezone=timeZone, latitude=weather.coordinates["lat"], longitude=weather.coordinates["lon"])
    
    # get sunset and golden hour times using the city info
    s = sun(city.observer, tzinfo=timeZone) 
    gh = golden_hour(city.observer, tzinfo=timeZone,direction=SunDirection.SETTING)
    print(str(gh[0]))
    gh_start = extract_time(str(gh[0]))
    gh_end = extract_time(str(gh[1]))
    sunset = extract_time(str(s["sunset"]))
    
    
    # print the results
    print(decide_result(weather.degrees, weather.weather_type, weather.wind_speed, weather.location))
    print(f"Golden hour starts at {gh_start} and ends at {gh_end}. Also sunset is at {sunset}.")
    
if __name__ == "__main__":
    main()
