# Should you bike today?

*This is my final project submission for [CS50p](https://cs50.harvard.edu/python).*

**Video demo:** 

[![a](https://img.youtube.com/vi/cZ1yHnH4olc/maxresdefault.jpg)](https://www.youtube.com/watch?v=cZ1yHnH4olc)

https://www.youtube.com/watch?v=ak5ia7yuUo8

---

<br>


I really like touring with my bike, but it is somewhat confusing to decide if that day is good for a bike ride. In the past, I had days I regretted going out for a bike ride because the weather conditions got deteriorated over time, or simply because it was just not as enjoyable without experiencing the golden hour and the sunset. Therefore I wrote this program to help me (or hopefully you) determine quickly if today is a good day for a bike tour. The program checks the most critical weather conditions like weather type, temperature, and wind speed. Moreover, it tells you what time is golden hour and sunset, because those times are the best to bike.


Here is how I structured this project:

### 1. Getting weather forecast information.
To get the weather forecast, I needed a publicly available weather API. I chose the [Open Weather API](https://openweathermap.org/api). I wrote a class called [Weather](/weather.py), which handles all weather-related information. It gets the coordinates of a given city, then uses those coordinates to get the current weather information.

### 2. Deciding if today is a good day to bike.
Based on the weather information I got, I use a bit of funky logic (that is tailored to my specific biking pleasure) to determine if today is a good day to bike. Here are some example criteria I've set:
- If the temperature forecast is more than 20°C, it is a good day to bike, regardless of weather type (for example rain or fog.)

- If the temperature is a little colder, but the sky is clear, it is still a good day. If, however, it is raining, it is not worth it.

- If the weather type is clear, it is always a good day to bike if the temperature is above 0.

- On top of all these, I also check for wind speed and display a warning if the wind speed is larger than 10km/h because I learned the hard way that it is really not fun to bike against the wind.

### 3. Displaying the sunset and golden hour times
Finally, I used a package called [Astral](https://astral.readthedocs.io/en/latest/) to calculate the golden hour and sunset time at our location. This actually took way more time than I expected to figure out. I had to use another package called [timezonefinder](https://pypi.org/project/timezonefinder/) to figure out the local time zone, then input that information along with the coordinates from the Weather information to Astral to figure out the exact sunset and golden hour time window. I also used regex to clean up the information I got from Astral to display to the user in a simple format.

### 4. Checking other locations
Right now the program defaults to "Munich" (where I currently live) to calculate all these things. However, I thought it would also be helpful to add functionality for users to input another city name as a command line argument to check if today is a good day to bike there. Could be handy when I (or you) travel. To do this, I used the [argparse](https://docs.python.org/3/library/argparse.html) module.


## Challenges:
At first, I also wanted this app to suggest what I should wear. I was thinking of defining a cloth library with specific properties. However, that became a really complicated problem for me to solve, risking never finishing this project. Therefore I changed the scope.

I did a lot of refactoring along the way (for example creating the Weather class) and at one point I made a refactoring that actually made everything super hard to read and way more complicated than it should be. Then I reverted it the next day. I guess sometimes having things "less proper" but "more readable" is also possible.

## Next steps:
- Handling more weather conditions like fog, snow, storm, etc. Apparently, there are tens of [different weather conditions](https://openweathermap.org/weather-conditions).
- Making a friendly UI instead of just text output.

## Thanks:
- CS50 team for the amazing course
- The unpredictable Munich weather for the inspiration