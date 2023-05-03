from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

class Result1(MDScreen):
    def __init__(self, *args, **kwargs):
        Builder.load_file("ayo/kv/result1.kv")
        super().__init__(*args, **kwargs)
