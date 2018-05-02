import cv2
import numpy as np

#BGR

def Red():
    red = np.uint8([[[0, 0, 255]]])
    HSV_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
    return HSV_red

def Green():
    green = np.uint8([[[0, 255, 0]]])
    HSV_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
    return HSV_green

def Blue():
    blue = np.uint8([[[255, 0, 0]]])
    HSV_blue = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
    return HSV_blue

def Black():
    black = np.uint8([[[0, 0, 0]]])
    HSV_black = cv2.cvtColor(black, cv2.COLOR_BGR2HSV)
    return HSV_black
