from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

class Grave1(MDScreen):
    def __init__(self, *args, **kwargs):
        Builder.load_file("ayo/kv/grave1.kv")
        super().__init__(*args, **kwargs)
          
    def calculate2(self, cs_ash2, cw_ash2, heat_ash2, ash2):
        if cs_ash2.text != "" and cw_ash2.text != "" and heat_ash2.text != "":
            g = float(cs_ash2.text)
            h = float(cw_ash2.text)
            i = float(heat_ash2.text)
            if g == h:
                j = 0
            else:
                j = float(((i-h)/(g-h))*100)
            self.ids.ash2.text = f"{j:.2f}"
