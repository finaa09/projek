from kivymd.uix.screen import MDScreen
from kivymd.uix.pickers import MDDatePicker, MDTimePicker
from kivy.lang import Builder


class Coal(MDScreen):
    def __init__(self, *args, **kwargs):
        Builder.load_file('ayo/kv/coal.kv')
        super().__init__(*args, **kwargs)

    def open_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_date_save, on_cancel=self.on_date_cancel)
        date_dialog.open()

    def on_date_save(self, instance, value, *args, **kwargs):
        self.ids.set_date.text = str(value)

    def on_date_cancel(self, instance, value):
        self.ids.set_date.text = ""


