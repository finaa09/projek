from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

class Day1(MDScreen):
    def __init__(self, *args, **kwargs):
        Builder.load_file("ayo/kv/day1.kv")
        super().__init__(*args, **kwargs)
          
    def calculate2(self, cs_ash3, cw_ash3, heat_ash3, ash3):
        if cs_ash3.text != "" and cw_ash3.text != "" and heat_ash3.text != "":
            g = float(cs_ash3.text)
            h = float(cw_ash3.text)
            i = float(heat_ash3.text)
            if g == h:
                j = 0
            else:
                j = float(((i-h)/(g-h))*100)
            self.ids.ash3.text = f"{j:.2f}"
