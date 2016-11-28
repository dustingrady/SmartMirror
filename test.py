#Author: Scott Grether, Dustin Grady
#Function: Create GUI with TKinter and set up widgets. Clock and weather that updates
#Status: Working/ Tested

import time
import calendar
from weather import WeatherClass

try:
    #python3
    from tkinter import *
except:
    #python2
    from Tkinter import *

time1 = time.localtime(time.time())

class Application(Frame):

    def createTime(self):#Create Time widget
        self.Time = Label(self.top_right, fg='white', background='black', font=self.labelfont)
        self.Time.pack(side='right')
        self.Time.config(borderwidth=0)
        self.Time.config(highlightthickness=0)

    def createCal(self):#Create calendar widget
        self.Cal = Text(self.bottom_left,height=7,width=0,background='black', fg='white')
        self.Cal.insert(INSERT, calendar.month(time1[0], time1[1]))
        self.Cal.pack(side='left',fill='both',expand=True)
        self.Cal.config(borderwidth=0)
        self.Cal.config(highlightthickness=0)

    def createImage(self):#Create weather image widget
        self.imageWidget = Label(self.bottom_right, fg='white', background='black', font=self.labelfont)
        self.imageWidget.pack(side="right")
        self.imageWidget.config(borderwidth=0)
        self.imageWidget.config(highlightthickness=0)

    def createText(self):#Create weather text widget
        self.textWidget = Label(self.bottom_right, fg='white', background='black', font=self.labelfont)
        self.textWidget.config(bg='black', fg='white')
        self.textWidget.config(borderwidth=0)#Get rid of 1px border
        self.textWidget.config(highlightthickness=0)#Get rid of 1px border
        self.textWidget.config(height=3, width=20)
        self.textWidget.pack(expand=NO, fill=BOTH, side='right')

    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.labelfont = ('Courier', 20, 'bold')#Font for all the widgets

        self.main_container = Frame(master, background='black')
        self.main_container.pack(side='top',fill='both',expand=True)
        master.minsize(width=1000,height=500)#Set window size

        self.top_frame = Frame(self.main_container, background='black')
        self.top_frame.pack(side='top',fill='x',expand=False)

        self.bottom_frame = Frame(self.main_container, background='black')
        self.bottom_frame.pack(side='bottom',fill='x',expand=False)

        self.top_left = Frame(self.top_frame, background='black')
        self.top_left.pack(side="left", fill="x", expand=True)

        self.top_right = Frame(self.top_frame, background='black')
        self.top_right.pack(side="right", fill="x", expand=True)

        self.bottom_right = Frame(self.bottom_frame, background='black')
        self.bottom_right.pack(side='right',fill='x',expand=True)

        self.bottom_left = Frame(self.bottom_frame, background='black')
        self.bottom_left.pack(side='left',fill='x',expand=True)

        #Create all thew widgets
        self.createTime()
        self.createCal()
        self.createImage()
        self.createText()

        self.top_left_label = Label(self.top_left, text="Top Left", fg='white', background='black')
        self.top_left_label.pack(side="left")

        #self.top_right_label = Label(self.top_right, text="Top Right")
        #self.top_right_label.pack(side="right")

        #self.bottom_right_label = Label(self.bottom_right,text='Bottom Right', fg='white', background='black')
        #self.bottom_right_label.pack(side='right')

        #self.bottom_left_label = Label(self.bottom_left,text='Bottom Left')
        #self.bottom_left_label.pack(side='left')

#Display live time
def tick():
    global time1
    time2 = time.localtime(time.time())
    if time2 != time1:
        time1 = time2
        app.Time.config(text=time.asctime(time1))
    app.Time.after(1000, tick)

'''Draw weather status/icon'''
def draw_Weather():
    global weatherClassObject
    weatherClassObject = WeatherClass()

    weatherImage = weatherClassObject.weatherImage
    weatherInfo = weatherClassObject.location + '\n' + str(weatherClassObject.currentWeather) + '\n' + str(weatherClassObject.currentTemperature + 'F')#Get description of weather/ temperature

    app.imageWidget.config(image = weatherImage) #update image
    app.textWidget.config(text = weatherInfo) #update text

    #print('Updating..')#Testing
    #print(weatherClassObject.currentWeather)#Testing
    #print(weatherClassObject.currentTemperature)#Testing
    app.imageWidget.after(30000, draw_Weather)#update every x milliseconds
    #return weatherClassObject

root = Tk()
root.title('Smart Mirror')
app = Application(root)
tick()#Initial call for clock ticking
draw_Weather()#Initial call to get draw_Weather going
root.mainloop()
