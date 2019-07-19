# declared inside the class bt outside the methods.


class Weather:
    day = 'Thursday'

    def __init__(self, humidity, precipitation, wind):
        self.humidity = humidity
        self.precipitation = precipitation
        self.wind = wind

    def weather_data(self):
        return f"""Today is {self.day} with humidity {self.humidity}, precipitation of {self.precipitation} and wind with {self.wind}"""


w1 = Weather(80, 80, 11)
# to access the class variable
# use,
w1.day
# or
Weather.day

# can access class variables inside the methods defined in class.
# and it is invoked with self.


