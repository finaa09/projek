from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

class Login(MDScreen):
    def __init__(self, *args, **kwargs):
        Builder.load_file("ayo/kv/login.kv")
        super().__init__(*args, **kwargs)