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
    
    def __init__(self, weather):
        self.weather = weather
        self._decide()
    
    
    def _decide(self):
        if self.weather.degrees >= 20:
            self.main_result = True
        elif self.weather.degrees > 15 and self.weather.degrees < 20:
            if self.weather.weather_type == "Rain":
                self.main_result = False
            else:
                self.main_result = True
        elif self.weather.degrees > 0:
            if self.weather.weather_type != "Clear":
                self.main_result = False
            else:
                self.main_result = True
        if self.weather.wind_speed > 10:
            self.wind_warning = True
        else:
            self.wind_warning = False
        
        print(f"Is it cycling weather in {self.weather.location}?\n- {'Yes!' if self.main_result else 'No.'} It is {self.weather.degrees} degrees and weather type is: {self.weather.weather_type}.\nShould i care about wind?\n- {'Yes.' if self.wind_warning else 'No!'} Wind speed is {self.weather.wind_speed} km/h.")
        
    
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
        

def main():
    weather = Weather("scotland")
    result = Result(weather)
    # print(weather.get_full_json())

    # if weather.degrees >= 20:
    #     result.main_result= True
    # elif weather.degrees > 15 and weather.degrees < 20:
    #     if weather.weather_type == "Rain":
    #         result.main_result = False
    #     else:
    #         result.main_result = True
    # elif weather.degrees > 0:
    #     if weather.weather_type != "Clear":
    #         result.main_result = False
    #     else:
    #         result.main_result = True
    
    # if weather.wind_speed > 10:
    #     result.wind_warning = True
    # else:
    #     result.wind_warning = False
        
    # print(f"Is it cycling weather in {weather.location}?\n- {'Yes!' if result.main_result else 'No.'} It is {weather.degrees} degrees and weather type is: {weather.weather_type}.\nShould i care about wind?\n- {'Yes.' if result.wind_warning else 'No!'} Wind speed is {weather.wind_speed} km/h.")
        

if __name__ == "__main__":
    main()
