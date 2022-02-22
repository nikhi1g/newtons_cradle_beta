from kivy.app import App
from kivy.uix.widget import Widget
import os
os.environ[
    'DISPLAY'] = ":0.0"
'''
Globals
'''
initial_touch = None
final_touch = None
'''
End Globals
'''

class TouchInput(Widget):
    global initial_touch, final_touch
    def on_touch_down(self, touch):
        initial_touch = touch.pos
        print(initial_touch, 'initial')

    # def on_touch_move(self, touch):
    #     print(touch.pos)

    def on_touch_up(self, touch):
        final_touch = touch.pos
        print(final_touch, 'final')

class SimpleKivy4(App):
    def build(self):
        return TouchInput()
    
if __name__ == "__main__":
    SimpleKivy4().run()


# from kivy.app import App
# from kivy.uix.widget import Widget
# from kivy.core.window import Window
#
# class TouchInput(Widget):
#     def on_touch_down(self, touch):
#         print(touch.pos)
#
#     def on_touch_move(self, touch):
#         # print(touch)
#         pass
#     def on_touch_up(self, touch):
#         print("RE",touch.pos)
#
#     Window.bind(on_touch_down=on_touch_down)
#     Window.bind(on_touch_down=on_touch_move)
#     Window.bind(on_touch_down=on_touch_up)
#
# class SimpleKivy4(App):
#
#     def build(self):
#
#         return TouchInput()
#
#
#
# if __name__ == "__main__":
#     SimpleKivy4().run()