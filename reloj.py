from datetime import datetime
from time import sleep
from os import system

while True:
    sleep(1)
    dt=datetime.now()
    system("cls")
    print("{}:{}:{}".format(dt.hour,dt.minute,dt.second))
   

