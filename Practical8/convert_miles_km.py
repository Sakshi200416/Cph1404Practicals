"""
Convert miles to kilometres GUI program.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = "Sakshi Sharma"


class MilesConverterApp(App):
    def build(self):
        Window.size = (400, 200)
        self.title = "Miles to Kilometres Converter"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self):
        try:
            miles = float(self.root.ids.input_miles.text)
            km = miles * 1.60934
            self.root.ids.output_label.text = f"{km:.2f}"
        except ValueError:
            self.root.ids.output_label.text = "0.0"

    def handle_increment(self, value):
        try:
            miles = float(self.root.ids.input_miles.text)
        except ValueError:
            miles = 0
        miles += value
        self.root.ids.input_miles.text = str(miles)
        self.handle_convert()


MilesConverterApp().run()
