import serial
import time
import requests

r = requests.get('https://api.github.com', auth=('user', 'pass'))


URI = 'http://127.0.0.1:5000/api/uid/2'

with serial.Serial('/dev/ttyACM0', 115200) as ser:
    while True:
        time.sleep(1)
        data = requests.get(URI)
        j = data.json()
        if 'uid' in j and j['uid'] is not '':
            print(j['uid'])
            d = j['uid'].encode()
            ser.write(d)

