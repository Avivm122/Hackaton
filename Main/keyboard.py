from tello import Tello
from tkinter import *
root=Tk()
x = 1
local_ip = '192.168.10.2'
local_port = 8889
imperial = False
tello = Tello(local_ip, local_port, imperial)
tello.takeoff()
tello.set_speed(5)
def stop(event):
    tello.land()
def left(event):
    tello.move_left(x)
def right(event):
    tello.move_right(x)
def forward(event):
    tello.move_forward(x)
def backward(event):
    tello.move_backward(x)
def up(event):
    tello.rotate_cw(30)
def down(event):
    tello.rotate_ccw(30)

frame=Frame(root,width=300,height=250)
frame.bind('<Down>',backward)
frame.bind('<Left>',left)
frame.bind('<Right>',right)
frame.bind('<Up>',forward)
frame.bind('<1>',up)
frame.bind('<2>',down)
frame.bind('<Tab>',stop)

frame.pack()
frame.focus_set()
frame.mainloop()


