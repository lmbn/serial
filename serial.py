
import serial
import time
import os

os.getcwd()
ser = serial.Serial('/dev/ttyACM0', 115200, timeout = 5)

file = open('commands.csv')
while 1:
 command = file.readline()
 if not command:
        break
 ser.write(command)

 response = ser.readline()
 print response
 time.sleep(5)
 file.close

