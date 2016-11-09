import threading
from test import getWeatherIcon

#testObject = test()

def update():
    threading.Timer(5, update).start()
    print('Updating..')
    getWeatherIcon()

update()
