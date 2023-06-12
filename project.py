from weather import Weather
from astral.sun import sun, golden_hour
from astral import LocationInfo, SunDirection
from timezonefinder import TimezoneFinder
import re
import argparse


class color:
        PURPLE = '\033[95m'
        CYAN = '\033[96m'
        DARKCYAN = '\033[36m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        END = '\033[0m'

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


def decide_result(degrees, weather_type, wind_speed, location, region):
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

    return f"\nIs it cycling weather in {location}, {region}?\n- {f'{color.GREEN}✅Yes!{color.END}' if result.main_result else f'{color.RED}❌No.{color.END}'} It is {color.CYAN}{degrees}{color.END} degrees and weather type is: {color.CYAN}{weather_type}{color.END}.\n\nIs the wind speed low enough?\n- {f'{color.RED}❌No.{color.END}' if result.wind_warning else f'{color.GREEN}✅Yes!{color.END}'} Wind speed is {color.CYAN}{wind_speed} km/h.{color.END}"


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
    gh_start = extract_time(str(gh[0]))
    gh_end = extract_time(str(gh[1]))
    sunset = extract_time(str(s["sunset"]))
    
    
    # print the results
    print(decide_result(weather.degrees, weather.weather_type, weather.wind_speed, weather.location, weather.region))
    print(f"\nGolden hour starts at {color.YELLOW}{gh_start}{color.END} and ends at {color.YELLOW}{gh_end}{color.END}. Also sunset is at {color.YELLOW}{sunset}{color.END}.\n")
        
if __name__ == "__main__":
    main()
