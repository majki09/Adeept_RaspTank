#!/usr/bin/env/python
# File name   : LED_test.py
# Author      : majki
# Date        : 2020/11/01

#import web_pdb; web_pdb.set_trace()
import move
import robotLight
import ultra
import os
#import info
import RPIservo
from time import sleep

def arm_park():
    sc.certSpeed([12,13,14], [50,50,0], [70,70,40])

def arm_reach_front():
    sc.certSpeed([12,13], [-80,-80], [70,70])

def arm_reach_back():
    sc.certSpeed([12,13],  [-80,70], [70,70])

def move_forward(speed: int, steps: int):
    for step in range(0, steps):
        move.move(speed, "forward", "no")
        sleep(0.1)
    move.motorStop()

def move_backward(speed: int, steps: int):
    for step in range(0, steps):
        move.move(speed, "backward", "no")
        sleep(0.1)
    move.motorStop()

if __name__ == '__main__':
    try:
        RL=robotLight.RobotLight()
        RL.start()
        #RL.breath(70,70,255)
        RL.hazard()
    except:
        print('Use "sudo pip3 install rpi_ws281x" to install WS_281x package')
        pass

    try:
        sc = RPIservo.ServoCtrl()
        sc.start()
    except:
        pass

    try:
        move.setup()
    except:
        pass

