# get user's location
# get that location's weather data
# get that locations's golden hour time
# display golden hour expected in XX:XX mins (if less than 24 hours)
# else display the next possible golden hour expected
# the logic for golden hour is this: if it is sunny.


from weather import Weather


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
        

def decide_result(degrees, weather_type, wind_speed, location, result: Result):
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
        

def main():
    weather = Weather("munich")
    result = Result()
    print(decide_result(weather.degrees, weather.weather_type, weather.wind_speed, weather.location, result))
    

if __name__ == "__main__":
    main()
