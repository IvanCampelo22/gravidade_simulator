from unicodedata import numeric
import kivy
import time
from threading import Thread
kivy.require('1.0.5')
from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, ReferenceListProperty
from kivy.uix.widget import Widget
from kivy.vector import Vector


class Objeto(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class Principal(Widget):
    pass



class Gravidade(App):

    def build(self):
        return Principal()

if __name__ == '__main__':
    Gravidade().run()