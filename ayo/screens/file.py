from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

class File(MDScreen):
    def __init__(self, *args, **kwargs):
        Builder.load_file("ayo/kv/file.kv")
        super().__init__(*args, **kwargs)