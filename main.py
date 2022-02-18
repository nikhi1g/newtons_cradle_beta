import os
import time
import sys
sys.path.insert(0, "/home/pi/packages/RaspberryPiCommon")

os.environ['DISPLAY'] = ":0.0" #makes touchscreen work :D INFO: The key you just pressed is not recognized by SDL. To help get this fixed, please report this to the SDL forums/mailing list <https://discourse.libsdl.org/> EVDEV KeyCode 330

# os.environ['KIVY_WINDOW'] = 'egl_rpi'
import subprocess
import kivy
from kivy.properties import ObjectProperty
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
from datetime import datetime
from time import sleep
from threading import Thread

kivy.require("1.9.1")
# time = datetime
timer_is_on = True
seconds = None
SCREEN_MANAGER = ScreenManager()
MAIN_SCREEN_NAME = 'main'


class ProjectNameGUI(App):

    def build(self):
        return SCREEN_MANAGER


Window.clearcolor = (1, 1, 1, 1)  # White


class MainScreen(Screen):
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
        Thread(target=self.timer).start()

    def timer(self):
        global seconds, timer_is_on
        set_time = time.time()
        while timer_is_on:
            ctime = time.time()
            seconds = int(ctime - set_time)
            time.sleep(1)
            if seconds > 1:
                timer_is_on = False
                Thread(target=self.initialize_ui).start()

    def initialize_ui(self):
        x = 0.1 - 0.115/4
        x_add = 0.115
        balls = [self.left_ball, self.middle_left_ball, self.middle_ball, self.middle_right_ball, self.right_ball]
        for ball in balls:
            ball.center_y = self.width * 0.2
            ball.center_x = self.width * (x + 0.2)
            x += x_add
        ballstrings = [self.left_ball_string, self.middle_left_ball_string, self.middle_ball_string,
                       self.middle_right_ball_string, self.right_ball_string]
        print("x_add", x_add)
        print("x", x)
        for string in ballstrings:
            string.size = (9, 500)
            string.pos = (self.width * (x - 0.375), self.width * 0.2)
            pos = string.pos
            print(f"({pos[0]},{pos[1]})")
            # string.center_y = self.width * 0.2
            # string.center_x = self.width * (x - 0.3)
            x += x_add

    def func(self):
        print('pressed')
        self.initialize_ui()


Builder.load_file('main.kv')
SCREEN_MANAGER.add_widget(MainScreen(name=MAIN_SCREEN_NAME))

if __name__ == "__main__":
    ProjectNameGUI().run()
