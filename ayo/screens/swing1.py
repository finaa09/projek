from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

class Swing1(MDScreen):
    def __init__(self, *args, **kwargs):
        Builder.load_file("ayo/kv/swing1.kv")
        super().__init__(*args, **kwargs)
          
    def calculate2(self, cs_ash4, cw_ash4, heat_ash4, ash4):
        if cs_ash4.text != "" and cw_ash4.text != "" and heat_ash4.text != "":
            g = float(cs_ash4.text)
            h = float(cw_ash4.text)
            i = float(heat_ash4.text)
            if g == h:
                j = 0
            else:
                j = float(((i-h)/(g-h))*100)
            self.ids.ash4.text = f"{j:.2f}"
