import time
from datatime import datetime
from pynput.keyboard import Controller_key
for date import lst
import webbrowser

b=Controller()

a=False

for i in lst:
    while True:
        if a==False:
            if datetime.now().hour == int(i[1].split(':')[0]) and datetime,now().minute == int(i[1].split(':')[1]):
                webbrowser.open(i[0])
                a=True
            elif a==True:
                if datetime.now().hour == int(i[1].split(':')[0]) and datetime.now().minute == int(i[1].split(':')[1]):
                    keyboard.press('w')
                    time.sleep(1)
                    keyboard.press(Key.enter)
                    a=False
                    break
                    
                
