from tello import Tello
import time

wait_time = 5  # Wait time after each command
local_ip = ['192.168.10.2']
local_port = 8889
imperial = False  # MPH to KMH further info in tello.py

tello = Tello(local_ip, local_port, imperial, wait_time+1)
tello.takeoff()
time.sleep(wait_time)
tello.land()
