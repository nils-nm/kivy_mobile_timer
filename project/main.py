

from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivy.uix.togglebutton import ToggleButton
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivy.factory import Factory

from kivy.lang import Builder
from kivy.clock import Clock
import time
kv = Builder.load_file('main.kv')


class TimeWindow(MDScreen):
    def time(self, *args):
        MDRaisedButton.text = str(time.strftime('%H:%M', time.localtime()))


# class SettingsWindow(Screen):
#    def color(self, col):
#        if col == 'r':
#            sm.get_screen('time').ids.time_in.color = (1, 0, 0, 1)
#        elif col == 'g':
#            sm.get_screen('time').ids.time_in.color = (0, 1, 0, 1)
#        elif col == 'b':
#            sm.get_screen('time').ids.time_in.color = (0, 0, 1, 1)


class MyApp(MDApp):
    custom_sheet = None

    def build(self):

        Clock.schedule_interval(TimeWindow.time, 1)

        return kv

    def secbs(self):
        self.custom_sheet = MDCustomBottomSheet(screen=Factory.ContentCustomSheet())
        self.custom_sheet.open()


if __name__ == '__main__':
    MyApp().run()
