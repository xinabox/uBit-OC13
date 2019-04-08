from microbit import *
from OC13 import OC13

OC13 = OC13()

OC13.init()

while True:
    for i in range(0, 5):
        OC13.write(i, True)
        sleep(500)
        
    for i in range(4, -1, -1):
        OC13.write(i, False)
        sleep(500)
