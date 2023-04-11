from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

class Result(MDScreen):
    def __init__(self, *args, **kwargs):
        Builder.load_file("ayo/kv/result.kv")
        super().__init__(*args, **kwargs)
