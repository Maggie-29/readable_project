import serial
import keyboard
import threading
import datetime as dt
#sudo python /opt/anaconda3/lib/python3.7/site-packages/serial/serialposix.py

def read():
    ser = serial.Serial('/dev/ttyUSB0') #Update with your arduino port
    ser.baudrate = '9600' #set baudRate
    
    start = dt.datetime.now()
    while True: 
        end = dt.datetime.now()
        delta = (end - start).seconds
        if delta > 10:
            uid1 = -1
            break
        try:
            if (ser.inWaiting()>0):
                h1=ser.readline() #reading serial data.
                ss=h1.decode().strip() #转码问题
            else:
                continue

        except:
            print('error')  # Maybe don't do this, or mess around with the interval
            continue

        if 'UID' in ss:
            print(ss)
            s1 = ss.split(':')
            print(s1)
            uid1 = s1[1].strip()
            print(uid1)
            break
    return uid1



