from kivymd.app import MDApp
from kivymd.uix.screenmanager import ScreenManager
from kivy.core.text import LabelBase
from kivy.core.window import Window

Window.size = (320, 580)

from screens.screens import *

class WindowManager(ScreenManager):
    pass


class Test(MDApp):
    def build(self):
        self.wm = WindowManager()
        screens = [
            Welcome(name="welcome"),
            Login(name="login"),
            Standard(name="standard"),
            Coal(name="coal"),
            Register(name="register"),
            Daily(name="daily"),
            Nar1(name="nar1"),
            Comp1(name="comp1"),
            Grave1(name="grave1"),
            Day1(name="day1"),
            Swing1(name="swing1"),
            Comp2(name="comp2"),
            Result1(name="result1"),
            Result2(name="result2"),
            Result3(name="result3"),
            Result4(name="result4"),
            Result5(name="result5"), 
            Incoming(name="incoming"),
            Custom1(name="custom1"),
            Result9(name="result9"),
            File(name="file"),
        ]
        for screens in screens:
            self.wm.add_widget(screens)
        return self.wm

if __name__ == "__main__":
    LabelBase.register(name="MPoppins", fn_regular="assets/font/Poppins-Medium.otf")
    LabelBase.register(name="SBPoppins", fn_regular="assets/font/Poppins-SemiBold.otf")
    Test().run()
