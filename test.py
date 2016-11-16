import time
import calendar
import threading
from weather import WeatherClass

try:
    #python3
    from tkinter import *
except:
    #python2
    from Tkinter import *

time1 = time.localtime(time.time())

class Application(Frame):

    def createTime(self):
        self.Time = Label(self.top_right, text=time.asctime(self.localtime), background='black', fg = 'white')
        self.Time.pack(side='right')

    def createCal(self):
        self.Cal = Text(self.bottom_right,height=8,width=0,background='black', fg = 'white')
        self.Cal.insert(INSERT, calendar.month(self.localtime[0], self.localtime[1]))
        self.Cal.pack(side='left',fill='both',expand=True)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.localtime = time.localtime(time.time())

        self.main_container = Frame(master, background='black')
        self.main_container.pack(side='top',fill='both',expand=True)
        master.minsize(width=1000,height=300)

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

        self.bottom_left_label = Label(self.bottom_left,text='Bottom Left')
        self.bottom_left_label.pack(side='left')

root = Tk()
root.title('Smart Mirror')
app = Application(root)

#Display live time
def tick():
    global time1
    time2 = time.localtime(time.time())
    if time2 != time1:
        time1 = time2
        app.Time.config(text=time.asctime(time1))
    app.Time.after(200, tick)


'''Draw weather results'''
weatherClassObject = WeatherClass()#Create object of our WeatherClass()
#initialize the weather widgets
imageWidget = Label(root)
labelfont = ('Courier', 20, 'bold')

imageWidget.pack(side="right")
textWidget = Label(root)
textWidget.config(bg='black', fg='white')
textWidget.config(font=labelfont)
textWidget.config(height=3, width=16)
textWidget.pack(expand=NO, fill=BOTH, side='right')

def draw_Weather():
    weatherImage = weatherClassObject.weatherImage
    weatherInfo = str(weatherClassObject.currentWeather) + '\n' + str(weatherClassObject.currentTemperature + 'F')#Get description of weather/ temperature
    imageWidget.config(image=weatherImage) #update image

    textWidget.config(text = weatherInfo) #update text

    print('Updating..')#Testing
    threading.Timer(5, draw_Weather).start()#Updates every x seconds

tick()
draw_Weather()

app.mainloop()
