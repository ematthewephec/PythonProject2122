from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget


def build(self):
    return Builder.load_file("UI.kv")
