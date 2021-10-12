from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.lang import Builder
from kivy.clock import Clock
import time
Builder.load_file('main.kv')


class TimeWindow(Screen):
    def spin(self, win):
        pass

    def time(self, *args):
        self.ids.time_in.text = str(time.strftime('%H:%M', time.localtime()))


class SettingsWindow(Screen):
    def color(self, col):
        if col == 'r':
            sm.get_screen('time').ids.time_in.color = (1, 0, 0, 1)
        elif col == 'g':
            sm.get_screen('time').ids.time_in.color = (0, 1, 0, 1)
        elif col == 'b':
            sm.get_screen('time').ids.time_in.color = (0, 0, 1, 1)


class WODWindow(Screen):
    pass


sm = ScreenManager()
sm.add_widget(TimeWindow(name='time'))
sm.add_widget(SettingsWindow(name='set'))
sm.add_widget(WODWindow(name='wod'))


class MyApp(App):
    def build(self):

        Clock.schedule_interval(sm.get_screen('time').time, 1)
        return sm


if __name__ == '__main__':
    MyApp().run()
