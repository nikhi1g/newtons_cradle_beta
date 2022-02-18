import spidev
import sys
import os
from time import sleep
import RPi.GPIO as GPIO

sys.path.insert(0, '/home/pi/packages/RaspberryPiCommon')
sys.path.insert(0, '/home/pi/packages/slushengine')
sys.path.insert(0, 'Kivy/')
import Slush
from Slush.Devices import L6470Registers as LReg
from pidev.stepper import stepper
from Slush.Devices import L6470Registers
from threading import Thread
import keyboard

spi = spidev.SpiDev()

'''
Globals
'''
# Init a 200 steps per revolution stepper on Ports
left_vertical = stepper(port=3, micro_steps=32, hold_current=20, run_current=20, accel_current=20, deaccel_current=20,
                        steps_per_unit=200, speed=5)

left_horizontal = stepper(port=2, micro_steps=32, hold_current=20, run_current=20, accel_current=20, deaccel_current=20,
                          steps_per_unit=200, speed=3)

right_vertical = stepper(port=1, micro_steps=32, hold_current=20, run_current=20, accel_current=20, deaccel_current=20,
                         steps_per_unit=200, speed=5)

right_horizontal = stepper(port=0, micro_steps=32, hold_current=20, run_current=20, accel_current=20,
                           deaccel_current=20,
                           steps_per_unit=200, speed=3)

lscooper = [left_vertical, left_horizontal]
rscooper = [right_vertical, right_horizontal]
motors = [left_vertical, right_vertical, left_horizontal, right_horizontal]
switches = [left_vertical.read_switch(), right_vertical.read_switch(), left_horizontal.read_switch(),
            right_horizontal.read_switch()]

positions = [8.75, 8.75 + 4.5, 8.75 + 4.5 * 2, 8.75 + 4.5 * 3]

# motorpositions

right_vertical_up = 3.1
left_vertical_up = 3.5

left_horizontal_stop = 5
right_horizontal_stop = 5.2

user_input = []

'''
End Globals
'''


def set_verticals(m: stepper):
    m.setCurrent(8, 10, 10, 10)
    m.setAccel(0x50)
    m.setDecel(0x10)
    m.setMaxSpeed(525)
    m.setMinSpeed(0)
    m.setMicroSteps(32)
    m.setThresholdSpeed(1000)
    m.setOverCurrent(2000)
    m.setStallCurrent(2187.5)
    m.setLowSpeedOpt(False)
    m.setSlope(0x562, 0x010, 0x01F, 0x01F)
    m.setParam(LReg.CONFIG, 0x3688)


set_verticals(left_vertical)
set_verticals(right_vertical)


def is_busy(motor):
    while motor.is_busy():
        sleep(.1)


def complete_relative_move(motor: stepper, num):
    motor.start_relative_move(num)
    is_busy(motor)


def home():
    global motors
    lscooper[0].go_until_press(0, 2 * 6400)
    rscooper[0].go_until_press(0, 2 * 6400)
    is_busy(lscooper[0])
    is_busy(rscooper[0])
    sleep(0.2)
    lscooper[1].go_until_press(0, 3 * 6400)
    rscooper[1].go_until_press(0, 3 * 6400)
    is_busy(lscooper[1])
    is_busy(rscooper[1])
    for motor in motors:
        motor.free()


def home_verticals():
    lscooper[0].go_until_press(0, 5500)
    rscooper[0].go_until_press(0, 5000)




def get_switches():
    return switches


def get_user_input():
    global user_input
    user_input_left = int(input("Enter Left Number 0(none) 1, 2, 3, 4: "))

    user_input_right = int(input("Enter Right Number 0(none) 1, 2, 3, 4: "))

    user_input = [user_input_left, user_input_right]

    return user_input


def stop_balls():
    home()
    complete_relative_move(left_vertical, left_vertical_up)
    complete_relative_move(right_vertical, right_vertical_up)
    complete_relative_move(left_horizontal, left_horizontal_stop)
    complete_relative_move(right_horizontal, right_horizontal_stop)





def scoop():
    left = 1
    right = 1
    can_scoop = True
    if can_scoop:
        # Left
        complete_relative_move(left_horizontal, positions[left - 1])
        complete_relative_move(left_vertical, left_vertical_up)
        complete_relative_move(left_horizontal, -positions[left - 1])
        # Right
        complete_relative_move(right_horizontal, positions[right - 1])
        complete_relative_move(right_vertical, right_vertical_up)
        complete_relative_move(right_horizontal, -positions[right - 1])
        home_verticals()


def start():
    stop_balls()
    scoop()






# right vertical tends to move at a greater scale than the left
