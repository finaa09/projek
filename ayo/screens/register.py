from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

class Register(MDScreen):
    def __init__(self, *args, **kwargs):
        Builder.load_file("ayo/kv/register.kv")
        super().__init__(*args, **kwargs)