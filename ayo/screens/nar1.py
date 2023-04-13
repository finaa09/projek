from kivymd.uix.screen import MDScreen
from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivymd.uix.scrollview import ScrollView

class Nar1(MDScreen):
    def __init__(self, **kwargs):
        Builder.load_file("ayo/kv/nar1.kv")
        super().__init__(**kwargs)

    def calculate1(self, cs_h2oad, cw_h2oad, heat_h2oad, h2oad):
        if cs_h2oad.text != "" and cw_h2oad.text != "" and heat_h2oad.text != "":
            a = float(cs_h2oad.text)
            b = float(cw_h2oad.text)
            c = float(heat_h2oad.text)
            if a == b:
                d = 0
            else:
                d = float(((a-c)/(a-b))*100)
            self.ids.h2oad.text = f"{d:.2f}"
            
    def calculate2(self, cs_ash, cw_ash, heat_ash, ash):
        if cs_ash.text != "" and cw_ash.text != "" and heat_ash.text != "":
            g = float(cs_ash.text)
            h = float(cw_ash.text)
            i = float(heat_ash.text)
            if g == h:
                j = 0
            else:
                j = float(((i-h)/(g-h))*100)
            self.ids.ash.text = f"{j:.2f}"

    def calculate3(self, cs_vm, cw_vm, heat_vm, vm, h2oad):
        if cs_vm.text != "" and cw_vm.text != "" and heat_vm.text != "" and h2oad != "":
            k = float(cs_vm.text)
            l = float(cw_vm.text)
            m = float(heat_vm.text)
            d = float(h2oad.text)
            if k == l:
                n = 0
            else:
                n = float((((k-m)/(k-l))*100)-d)
            self.ids.vm.text = f"{n:.2f}"    

    def calculate4(self, fc, h2oad, ash, vm):
        if h2oad.text != "" and ash.text != "" and vm.text != "":
            d = float(h2oad.text)
            j = float(ash.text)
            n = float(vm.text)
            if d == j:
                p = 0
            else:
                p = float(100-(d+j+n))
            self.ids.fc.text = f"{p:.2f}"