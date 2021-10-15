

from kivy.app import App

from kivy.uix.screenmanager import Screen, ScreenManager

from kivy.lang import Builder
from kivy.clock import Clock
import time
Builder.load_file('main.kv')


class TimeWindow(Screen):
    def time(self, *args):
        sm.get_screen('time').ids.but_clock.text = str(time.strftime('%H:%M', time.localtime()))


class SettingsWindow(Screen):
    def color(self, r_col, g_col, b_col):
        col_list = [r_col, g_col, b_col]
        sm.get_screen('time').ids.but_clock.color = (col_list[0], col_list[1], col_list[2], 1)

    def background(self, r_bak, g_bak, b_bak):
        bak_list = [r_bak, g_bak, b_bak]
        sm.get_screen('time').ids.but_clock.background_color = (bak_list[0], bak_list[1], bak_list[2], 1)


sm = ScreenManager()
sm.add_widget(TimeWindow(name='time'))
sm.add_widget(SettingsWindow(name='settings'))


class MyApp(App):

    def build(self):
        Clock.schedule_interval(TimeWindow.time, 1)

        return sm


if __name__ == '__main__':
    MyApp().run()
