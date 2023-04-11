from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.pickers import MDDatePicker

Builder.load_file("ayo/kv/daily.kv")

class Daily(MDScreen):
    def open_date_picker(self):
        date_dialogue = MDDatePicker()
        date_dialogue.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialogue.open()

    def on_save(self, instance, value,*args ,**kwargs):
        self.ids.set_date.text = str(value)

    def on_cancel(self, instance, value):
        self.ids.set_date.text = ""
