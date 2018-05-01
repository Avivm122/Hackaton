from tello import Tello


local_ip = '192.168.10.2'
local_port = 8889
imperial = False
tello = Tello(local_ip, local_port, imperial)
tello.land()