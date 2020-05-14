import serial
#sudo python /opt/anaconda3/lib/python3.7/site-packages/serial/serialposix.py

def read():
    ser = serial.Serial('/dev/ttyUSB1') #Update with your arduino port
    ser.baudrate = '9600' #set baudRate
    
    while True: # looping. 
        try:
            h1=ser.readline() #reading serial data.
            ss=h1.decode().strip() #转码问题
        #         print(ss)

        except:
            print('error')  # Maybe don't do this, or mess around with the interval
            continue

        if 'UID' in ss:
            s1 = ss.split(':')
            uid1 = s1[1].strip()
            print(uid1)
            break
    return uid1



