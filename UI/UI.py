from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder


Builder.load_file('UI.kv')


class UI(Widget):
    pass


class UIApp(App):
    def build(self):
        return UI()

    def process(self):
        text = self.root.ids.input.text
        print(text)

    def outputtext(self):
        text = self.root.ids.input.text
        print(text)

if __name__ == "__main__":
    UIApp().run()