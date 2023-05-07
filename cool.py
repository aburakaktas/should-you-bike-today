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
    
    def __str__(self):
        return f"Is it cycling weather: {'Yes' if self.main_result else 'No'},\nShould i care about wind: {'Yes' if self.wind_warning else 'No'}"
        
    
        

def main():
    weather = Weather("munich")
    result = Result()
    print(weather.get_full_json())
    # print(f"Weather degrees:{weather.degrees} type:{type(weather.degrees)}")
    # print(f"Weather type:{weather.weather_type} type:{type(weather.weather_type)}")
    # print(f"Wind speed:{weather.wind_speed} type:{type(weather.wind_speed)}")


    if weather.degrees >= 20:
        result.main_result= True
    elif weather.degrees > 10 and weather.degrees < 20:
        if weather.weather_type == "Rain":
            result.main_result = False
        else:
            result.main_result = True
    elif weather.degrees > 0:
        if weather.weather_type != "Clear":
            result.main_result = False
        else:
            result.main_result = True
    
    if weather.wind_speed > 10:
        result.wind_warning = True
    else:
        result.wind_warning = False
        
    print(f"Is it cycling weather in {weather.location}?\n- {'Yes!' if result.main_result else 'No.'} It is {weather.degrees} degrees and weather type is: {weather.weather_type}.\nShould i care about wind?\n- {'Yes.' if result.wind_warning else 'No!'} Wind speed is {weather.wind_speed} km/h.")
        

if __name__ == "__main__":
    main()
