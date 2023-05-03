from kivymd.uix.screen import MDScreen
from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivymd.uix.scrollview import ScrollView

class Comp2(MDScreen):
    def __init__(self, **kwargs):
        Builder.load_file("ayo/kv/comp2.kv")
        super().__init__(**kwargs)

    def calculate1(self, cs_h2oad5, cw_h2oad5, heat_h2oad5, h2oad5):
        if cs_h2oad5.text != "" and cw_h2oad5.text != "" and heat_h2oad5.text != "":
            a = float(cs_h2oad5.text)
            b = float(cw_h2oad5.text)
            c = float(heat_h2oad5.text)
            if a == b:
                d = 0
            else:
                d = float(((a-c)/(a-b))*100)
            self.ids.h2oad5.text = f"{d:.2f}"
            
    #def calculate2(self, ash1, ash2, ash3, ash4):
        #if ash1.text != "" and ash2.text != "" and ash3.text != "" and ash4.text != "":
            #g = float(ash1.text)
            #h = float(ash2.text)
            #i = float(ash3.text)
            #if g == h:
                #j = 0
            #else:
                #j = float((g+h+i)/3)
            #self.ids.ash1.text = f"{j:.2f}"

    def calculate3(self, cs_vm5, cw_vm5, heat_vm5, vm5, h2oad5):
        if cs_vm5.text != "" and cw_vm5.text != "" and heat_vm5.text != "" and h2oad5.text != "":
            k = float(cs_vm5.text)
            l = float(cw_vm5.text)
            m = float(heat_vm5.text)
            d = float(h2oad5.text)
            if k == l:
                n = 0
            else:
                n = float((((k-m)/(k-l))*100)-d)
            self.ids.vm5.text = f"{n:.2f}"    

    def calculate4(self, fc5, h2oad5, ash5, vm5):
        if h2oad5.text != "" and ash5.text != "" and vm5.text != "":
            d = float(h2oad5.text)
            j = float(ash5.text)
            n = float(vm5.text)
            if d == j:
                p = 0
            else:
                p = float(100-(d+j+n))
            self.ids.fc5.text = f"{p:.2f}"