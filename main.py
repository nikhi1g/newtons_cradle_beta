import os
import time
import sys



# sys.path.insert(0, "/home/pi/packages/RaspberryPiCommon")

os.environ['DISPLAY'] = ":0.0" #makes touchscreen work :D INFO: The key you just pressed is not recognized by SDL. To help get this fixed, please report this to the SDL forums/mailing list <https://discourse.libsdl.org/> EVDEV KeyCode 330

# os.environ['KIVY_WINDOW'] = 'egl_rpi'
import subprocess
import kivy
# from kivy.properties import ObjectProperty # put this for rpi
# from kivy import *
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.slider import Slider
from pidev.MixPanel import MixPanel
from pidev.kivy.PassCodeScreen import PassCodeScreen
from pidev.kivy.PauseScreen import PauseScreen
from pidev.kivy import DPEAButton
from pidev.kivy import ImageButton
from pidev.kivy.selfupdatinglabel import SelfUpdatingLabel
import keyboard
# from datetime import datetime
from time import sleep
from threading import Thread

kivy.require("1.9.1")
# time = datetime
SCREEN_MANAGER = ScreenManager()
MAIN_SCREEN_NAME = 'main'

mouse_pos = [0, 0]


class NewtonGUI(App):


    def __init__(self, **kwargs):
        super(NewtonGUI, self).__init__(**kwargs)
        Window.bind(mouse_pos=self.mouse_pos_fn)

    def mouse_pos_fn(self, window, pos):
        global mouse_pos
        mouse_pos = pos

    def build(self):
        return SCREEN_MANAGER


Window.clearcolor = (1, 1, 1, 1)  # White


class MainScreen(Screen):
    global mouse_pos
    init_x = None
    fin_x = None
    bar_button = ObjectProperty(None)

    left_ball = ObjectProperty(None)
    middle_left_ball = ObjectProperty(None)
    middle_ball = ObjectProperty(None)
    middle_right_ball = ObjectProperty(None)
    right_ball = ObjectProperty(None)

    left_ball_string = ObjectProperty(None)
    middle_left_ball_string = ObjectProperty(None)
    middle_ball_string = ObjectProperty(None)
    middle_right_ball_string = ObjectProperty(None)
    right_ball_string = ObjectProperty(None)

    def __init__(self, **kw):
        super().__init__(**kw)

    def func(self):
        print('pressed test function')
        print("mouse pos", mouse_pos)

    def on_down(self):
        self.init_x = mouse_pos[0]

    def on_up(self):
        self.fin_x = mouse_pos[0]
        if self.init_x < self.fin_x:
            print("swing left")
        elif self.init_x > self.fin_x:
            print("swing right")

    def get_click(self):
#acces the mouse event on click
        print(mouse_pos)
        if 871 < mouse_pos[0] < 1000:
            print('right ball')
        elif 711 < mouse_pos[0] < 871:
            print('right middle ball')



Builder.load_file('main.kv')
SCREEN_MANAGER.add_widget(MainScreen(name=MAIN_SCREEN_NAME))

if __name__ == "__main__":
    NewtonGUI().run()
