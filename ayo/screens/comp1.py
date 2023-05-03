from kivymd.uix.screen import MDScreen
from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivymd.uix.scrollview import ScrollView

class Comp1(MDScreen):
    def __init__(self, **kwargs):
        Builder.load_file("ayo/kv/comp1.kv")
        super().__init__(**kwargs)

    def calculate1(self, cs_h2oad1, cw_h2oad1, heat_h2oad1, h2oad1):
        if cs_h2oad1.text != "" and cw_h2oad1.text != "" and heat_h2oad1.text != "":
            a = float(cs_h2oad1.text)
            b = float(cw_h2oad1.text)
            c = float(heat_h2oad1.text)
            if a == b:
                d = 0
            else:
                d = float(((a-c)/(a-b))*100)
            self.ids.h2oad1.text = f"{d:.2f}"
            
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

    def calculate3(self, cs_vm1, cw_vm1, heat_vm1, vm1, h2oad1):
        if cs_vm1.text != "" and cw_vm1.text != "" and heat_vm1.text != "" and h2oad1.text != "":
            k = float(cs_vm1.text)
            l = float(cw_vm1.text)
            m = float(heat_vm1.text)
            d = float(h2oad1.text)
            if k == l:
                n = 0
            else:
                n = float((((k-m)/(k-l))*100)-d)
            self.ids.vm1.text = f"{n:.2f}"    

    def calculate4(self, fc1, h2oad1, ash1, vm1):
        if h2oad1.text != "" and ash1.text != "" and vm1.text != "":
            d = float(h2oad1.text)
            j = float(ash1.text)
            n = float(vm1.text)
            if d == j:
                p = 0
            else:
                p = float(100-(d+j+n))
            self.ids.fc1.text = f"{p:.2f}"