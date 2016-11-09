import time
import calendar
#import threading
from weather import WeatherClass

try:
    #python3
    from tkinter import *
except:
    #python2
    from Tkinter import *

class Application(Frame):

    def createTime(self):
        self.Time = Label(self.top_right, text=time.asctime(self.localtime))
        self.Time.pack(side='right')

    def createCal(self):
        self.Cal = Text(self.bottom_right,height=8,width=0,background='gray')
        self.Cal.insert(INSERT, calendar.month(self.localtime[0], self.localtime[1]))
        self.Cal.pack(side='right',fill='both',expand=True)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.localtime = time.localtime(time.time())

        self.main_container = Frame(master, background='bisque')
        self.main_container.pack(side='top',fill='both',expand=True)
        master.minsize(width=800,height=800)

        self.top_frame = Frame(self.main_container,background='green')
        self.top_frame.pack(side='top',fill='x',expand=False)

        self.bottom_frame = Frame(self.main_container,background='yellow')
        self.bottom_frame.pack(side='bottom',fill='x',expand=False)

        self.top_left = Frame(self.top_frame, background="pink")
        self.top_left.pack(side="left", fill="x", expand=True)

        self.top_right = Frame(self.top_frame, background="blue")
        self.top_right.pack(side="right", fill="x", expand=True)

        self.bottom_right = Frame(self.bottom_frame,background='red')
        self.bottom_right.pack(side='right',fill='x',expand=True)

        self.bottom_left = Frame(self.bottom_frame,background='orange')
        self.bottom_left.pack(side='left',fill='x',expand=True)

        self.createTime()
        self.createCal()

        self.top_left_label = Label(self.top_left, text="Top Left")
        self.top_left_label.pack(side="left")

        #self.top_right_label = Label(self.top_right, text="Top Right")
        #self.top_right_label.pack(side="right")

        #self.bottom_right_label = Label(self.bottom_right,text='Bottom Right')
        #self.bottom_right_label.pack(side='right')

        self.bottom_left_label = Label(self.bottom_left,text='Bottom Left')
        self.bottom_left_label.pack(side='left')

root = Tk()
root.title('Smart Mirror')
app = Application(root)

#Display live time
def tick(app):
    time2 = time.localtime(time.time())
    if time2 != app.localtime:
        app.localtime = time2
        app.Time.config(text=time.asctime(app.localtime))
    app.Time.after(200,tick(app))

#Display current weather from weather.py
def getWeatherIcon(app):
    weatherClassObject = WeatherClass()#Create object of our WeatherClass()
    currentWeatherStatus = weatherClassObject.currentWeather#Reference current weather from our object

    if "clouds" in currentWeatherStatus:
        weatherImage = PhotoImage(file="Cloudy.png")
    if "clear" in currentWeatherStatus:
        weatherImage = PhotoImage(file="ClearSkyDay.png")#Need to get time to change between clearnight/ clearday
    if "sunny" in currentWeatherStatus:
        weatherImage = PhotoImage(file="ClearSkyDay.png")
    if "rain" in currentWeatherStatus:
        weatherImage = PhotoImage(file="Rain.png")
    if "thunder" in currentWeatherStatus:
        weatherImage = PhotoImage(file="Thunder.png")
    if "snow" in currentWeatherStatus:
        weatherImage = PhotoImage(file="Snow.png")
    if "haze" in currentWeatherStatus:
        weatherImage = PhotoImage(file="Foggy.png")
    if "fog" in currentWeatherStatus:
        weatherImage = PhotoImage(file="Foggy.png")
    if "mist" in currentWeatherStatus:
        weatherImage = PhotoImage(file="Foggy.png")
    #print('Doing stuff..')#Testing
    return weatherImage

weatherImage = getWeatherIcon(app)#Get appropriate weather image from our displayWeather function
weatherInfo = str(WeatherClass().currentWeather) + '\n' + str(WeatherClass().currentTemperature + 'F')#Get description of weather/ temperature

#Draw the results
labelfont = ('times', 20, 'bold')
imageWidget = Label(root, image=weatherImage).pack(side="right")

#textWidget = Label(root,
#justify=LEFT,
#padx = 10,
#text=weatherInfo).pack(side="right")

textWidget = Label(root, text = weatherInfo)
textWidget.config(bg='black', fg='white')
textWidget.config(font=labelfont)
textWidget.config(height=3, width=20)
textWidget.pack(expand=NO, fill=BOTH, side='right')

#tick(app)#Currently broken
#threading.Timer(5, test).start()

app.mainloop()
