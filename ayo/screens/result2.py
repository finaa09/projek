from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

class Result2(MDScreen):
    def __init__(self, *args, **kwargs):
        Builder.load_file("ayo/kv/result2.kv")
        super().__init__(*args, **kwargs)
