from tello import Tello
import time


local_ip = '192.168.10.3'
local_port = 8889
imperial = False
drone = Tello(local_ip, local_port, imperial)
drone.takeoff()
time.sleep(7)
drone.set_speed(2)
time.sleep(1)
drone.move_down(3)
time.sleep(5)
drone.move_forward(10)
time.sleep(10)
drone.rotate_cw(180)
time.sleep(5)
drone.move_forward(10)
time.sleep(10)
drone.land()
print("Hokey Pokey complete! :)")

print('Flight time: %s' % drone.get_flight_time())