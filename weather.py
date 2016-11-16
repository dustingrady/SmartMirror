#Author: Dustin Grady
#Function: Access weather data from Open Weather Maps API_KEY
#Status: Working/ Tested

import pyowm
import time
import threading

try:
    #python3
    from tkinter import *
except:
    #python2
    from Tkinter import *

API_KEY = 'your_key_here'
owm = pyowm.OWM(API_KEY)

observation = owm.weather_at_place('Monterey, CA, US')
#observation = owm.weather_at_place('Tehran, Iran')#Example of another place (am vs pm)
#observation = owm.weather_at_coords(36.6002, 121.8947)#Example of coord system


class WeatherClass():
    def __init__(self):
        time1 = time.localtime(time.time())

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

        '''Determine current weather state'''
        if "clouds" in self.currentWeather:
            self.weatherImage = PhotoImage(file="Cloudy.png")
        if "clear" in self.currentWeather:
            if(time1.tm_hour > 6) and (time1.tm_hour <18):#Between 6am and 6pm will be day
                self.weatherImage = PhotoImage(file="ClearSkyDay.png")
            else:
                self.weatherImage = PhotoImage(file="ClearSkyNight.png")
        if "sunny" in self.currentWeather:
            self.weatherImage = PhotoImage(file="ClearSkyDay.png")
        if "rain" in self.currentWeather:
            self.weatherImage = PhotoImage(file="Rain.png")
        if "thunder" in self.currentWeather:
            self.weatherImage = PhotoImage(file="Thunder.png")
        if "snow" in self.currentWeather:
            self.weatherImage = PhotoImage(file="Snow.png")
        if "haze" in self.currentWeather:
            self.weatherImage = PhotoImage(file="Foggy.png")
        if "fog" in self.currentWeather:
            self.weatherImage = PhotoImage(file="Foggy.png")
        if "mist" in self.currentWeather:
            self.weatherImage = PhotoImage(file="Foggy.png")

#threading.Timer(5, __init__(self).start()
