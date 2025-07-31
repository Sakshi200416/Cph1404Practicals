"""
Dynamic Labels App - Generates labels from a list.
"""

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class DynamicLabelsApp(App):
    def build(self):
        names = ["Alice", "Bob", "Charlie", "Daisy", "Ethan"]
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        for name in names:
            label = Label(text=name, font_size=24)
            main_layout.add_widget(label)
        return main_layout


if __name__ == '__main__':
    DynamicLabelsApp().run()
