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
            Incoming(name="incoming"),
            Nar1(name="nar1"),
            Result(name="result"),

        ]
        for screens in screens:
            self.wm.add_widget(screens)
        return self.wm

if __name__ == "__main__":
    LabelBase.register(name="MPoppins", fn_regular="assets/font/Poppins-Medium.otf")
    LabelBase.register(name="SBPoppins", fn_regular="assets/font/Poppins-SemiBold.otf")
    Test().run()
