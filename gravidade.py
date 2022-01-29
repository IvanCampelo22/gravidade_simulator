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
from kivy.clock import Clock 
from random import randint
from kivy.core.image import Image



class Objeto(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class Principal(Widget):
    obj = ObjectProperty(None)

    def serve_obj(self, vel=(100,100)):
        self.obj.top = self.top
        self.obj.velocity = Vector(0,-4)

    
    def update(self, dt):
        self.obj.move()

        if (self.obj.y < 5.0) or (self.obj.top > self.height):
            self.obj.velocity_y = 0

        #if (self.obj.x < 0) or (self.obj.right > self.width):
            #self.obj.velocity_x *= -1
        


class Gravidade(App):

    def build(self):
        caindo = Principal()
        caindo.serve_obj(vel=5000)
        Clock.schedule_interval(caindo.update, 0/60.0)
        return caindo

if __name__ == '__main__':
    Gravidade().run()