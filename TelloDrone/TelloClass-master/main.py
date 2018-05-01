from tello import Tello
import time
import sys

wait_time = 5  # Wait time after each command
Lowest_battery = 5  # If the battery is equal to this or lower than the program will not run
local_ip = ['192.168.10.2', '192.168.10.3']
# local_ip = ['192.168.10.10', '192.168.10.19']  # Test ip's for debugging while the drone is charging
local_port = 8889
imperial = False  # MPH to KMH further info in tello.py
i = 0
while True:
    try:
        tello = Tello(local_ip[i], local_port, imperial, wait_time+1)
    except OSError:
        i = i+1
        if i == 2:
            break
        else:
            print(local_ip[i], "Is wrong ip")
try:
    Current_battery = tello.get_battery()
except NameError:
    sys.exit("No ip found")
if Current_battery >= Lowest_battery:
    print("Battery is fine")
    tello.takeoff()
    time.sleep(wait_time)  # delay for 1 seconds
    tello.flip('b')
    time.sleep(wait_time)  # delay for 1 seconds
    tello.rotate_cw(180)
    time.sleep(wait_time)
    tello.set_speed(2)
    time.sleep(1)
    tello.move_forward(0.1)
    time.sleep(wait_time)
    print('moved')
    time.sleep(wait_time)
    tello.land()
else:
    print("Battery need charging!")
