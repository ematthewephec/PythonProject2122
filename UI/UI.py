from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from appellechat import *


Builder.load_file('UI.kv')


class UI(Widget):
    pass


class UIApp(App):
    test3 = ObjectProperty(None)

    def build(self):
        return UI()

    def process(self):
        text = self.root.ids.input.text
        print(text)


    def outputtext(self):
        text = self.root.ids.output.text

        self.ids['result_label'].text = str("test")




    def abc(self):
        print('Test')
        command = self.root.ids.input.text
        inputcommand(command) #hier !!!!!!!!!!!!!!!

if __name__ == "__main__":
    UIApp().run()