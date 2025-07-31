"""
Square Number GUI program.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = "Sakshi Sharma"


class SquaringApp(App):
    def build(self):
        Window.size = (400, 150)
        self.title = "Square Number Calculator"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def calculate_square(self):
        try:
            value = float(self.root.ids.input_number.text)
            square = value ** 2
            self.root.ids.output_label.text = f"{square:.2f}"
        except ValueError:
            self.root.ids.output_label.text = "0.0"
