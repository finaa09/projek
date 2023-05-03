from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

class Result3(MDScreen):
    def __init__(self, *args, **kwargs):
        Builder.load_file("ayo/kv/result3.kv")
        super().__init__(*args, **kwargs)
