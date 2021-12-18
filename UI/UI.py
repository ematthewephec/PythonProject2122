from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget



class MyTextInput(Widget):
    pass


class TextWindow(App):
    def build(self):
        text_input = TextInput(font_size = 30, multiline = False)

        return text_input


if __name__ == "__main__":
    window = TextWindow()
    window.run()