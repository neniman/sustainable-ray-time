import serial
from datetime import datetime, timedelta
from urllib.request import urlopen

URI = 'http://127.0.0.1:5000/api/uid/1/'

with serial.Serial('/dev/ttyUSB0', 115200) as ser:
    uid = 0
    time = datetime.now()
    while 1:
        line = ser.readline()
        if line.startswith(b'UID:'):
            bline = line.strip()
            data = bline.split(b' ')[1:]
            i = 0
            for d in data:
                i = i * 256 + int(d, 16)
            if uid != i or datetime.now() - time > timedelta(seconds=5):
                uid = i
                time = datetime.now()
                urlopen(URI+hex(i))
                print(hex(i))
