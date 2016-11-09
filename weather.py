#Author: Dustin Grady
#Function: Access weather data from Open Weather Maps API_KEY
#Status: Working/ Tested

import pyowm

API_KEY = 'f758480110064748fcea0d1f2063bbb3'
owm = pyowm.OWM(API_KEY)

observation = owm.weather_at_place('San Francisco, CA, US')
#observation = owm.weather_at_coords(36.6002, 121.8947)


class WeatherClass():
    def __init__(self):
        '''Get Today's forecast'''
        weather = observation.get_weather()
        self.todaysForecast = str(weather).split("status=", 1)[1].replace(">", "")#Search for status and remove ">" from the end

        '''Get Current Weather Conditions'''
        currentConditions = weather.get_detailed_status()

        '''Get Current Temperature in Fahrenheit'''
        self.currentTemperature = weather.get_temperature(unit = 'fahrenheit')
        self.currentTemperature = str(self.currentTemperature).split("'temp':", 1)[1]#Get temperature, removing everything before it
        self.currentTemperature = self.currentTemperature[:3]#Remove everything except for the 2 digits we need

        self.todaysForecast = str(self.todaysForecast)
        self.currentWeather = str(currentConditions)
        self.currentTemperature = str(self.currentTemperature)



#-----------------------_Testing_----------------------------
        #print(self.currentWeather)
        print('Todays Forecast: ' + self.todaysForecast)
        print('Current Weather: ' + self.currentWeather)
        print('Current Temperature: ' + self.currentTemperature + ' degrees fahrenheit')
    #currentWeather = getWeather()
#Weather.getWeather()
#-----------------------_Testing_----------------------------
