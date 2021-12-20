from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from appellechat import *
from kivymd.app import MDApp


class UI(Widget):
    pass


class UIApp(MDApp):
    confirmbutton = ObjectProperty(None)

    def build(self):
        return UI()

    def process(self):
        text = self.root.ids.input.text
        print(text)

    def outputtext(self):
        self.root.ids.result_label.text = self.getcommandresult()

    def getcommandresult(self):
        command = self.root.ids.input.text
        return inputcommand(command)


if __name__ == "__main__":
    UIApp().run()
