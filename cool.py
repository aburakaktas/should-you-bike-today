# get user's location
# get that location's weather data
# get that locations's golden hour time
# display golden hour expected in XX:XX mins (if less than 24 hours)
# else display the next possible golden hour expected
# the logic for golden hour is this: if it is sunny.


from weather import Weather

def main():
    weather = Weather("Munich")
    print(weather)


if __name__ == "__main__":
    main()
