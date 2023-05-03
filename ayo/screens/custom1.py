from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

class Custom1(MDScreen):
    def __init__(self, *args, **kwargs):
        Builder.load_file("ayo/kv/custom1.kv")
        super().__init__(*args, **kwargs)

    def calculate1(self, cs_h2oad9, cw_h2oad9, heat_h2oad9, h2oad9):
        if cs_h2oad9.text != "" and cw_h2oad9.text != "" and heat_h2oad9.text != "":
            a = float(cs_h2oad9.text)
            b = float(cw_h2oad9.text)
            c = float(heat_h2oad9.text)
            if a == b:
                d = 0
            else:
                d = float(((a-c)/(a-b))*100)
            self.ids.h2oad9.text = f"{d:.2f}"
            
    def calculate2(self, cs_ash9, cw_ash9, heat_ash9, ash9):
        if cs_ash9.text != "" and cw_ash9.text != "" and heat_ash9.text != "":
            g = float(cs_ash9.text)
            h = float(cw_ash9.text)
            i = float(heat_ash9.text)
            if g == h:
                j = 0
            else:
                j = float(((i-h)/(g-h))*100)
            self.ids.ash9.text = f"{j:.2f}"

    def calculate3(self, cs_vm9, cw_vm9, heat_vm9, vm9, h2oad9):
        if cs_vm9.text != "" and cw_vm9.text != "" and heat_vm9.text != "" and h2oad9 != "":
            k = float(cs_vm9.text)
            l = float(cw_vm9.text)
            m = float(heat_vm9.text)
            d = float(h2oad9.text)
            if k == l:
                n = 0
            else:
                n = float((((k-m)/(k-l))*100)-d)
            self.ids.vm9.text = f"{n:.2f}"    

    def calculate4(self, fc9, h2oad9, ash9, vm9):
        if h2oad9.text != "" and ash9.text != "" and vm9.text != "":
            d = float(h2oad9.text)
            j = float(ash9.text)
            n = float(vm9.text)
            if d == j:
                p = 0
            else:
                p = float(100-(d+j+n))
            self.ids.fc9.text = f"{p:.2f}"