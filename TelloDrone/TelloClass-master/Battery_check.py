from tello import Tello

local_ip = '192.168.10.2'
local_port = 8889
imperial = False
tello = Tello(local_ip, local_port, imperial)
Current_battery = tello.get_battery()
print(Current_battery)