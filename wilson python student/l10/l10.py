from turtle import position
from pycat.core import Window, Scheduler, Sprite, KeyCode
import random
window = Window(width=600, height=900, background_image= 'galaxy.png')

class rocket (Sprite):
    def on_create(self):
        self.position = 300, 200
        self.scale =0.15
        self.image = 'rocket.gif'
    def on_update(self, dt):
        if window.is_key_pressed(KeyCode.A):
            self.x -= 10
        if window.is_key_pressed(KeyCode.D):
            self.x += 10
        if window.is_key_down(KeyCode.SPACE):
            window.create_sprite(laser, position = self.position)
        if self.is_touching_window_edge():
            self.delete()
window.create_sprite(rocket)



class laser (Sprite):
    def on_create(self):
        self.rotation =90 
        self.scale =0.1
        self.image = 'laser.png'
        self.add_tag('laser')
    def on_update(self, dt):
        self.y +=15
        if self.is_touching_window_edge():
            self.delete()
        if self.is_touching_any_sprite_with_tag('ufo'):
            self.delete()
            
class make_ufo (Sprite):
    def on_create(self):
        self.goto_random_position()
        self.y =850 
        self.image = random.choice(['UFO1.png', 'UFO2.png', 'UFO3.png', 'UFO4.png'])
        self.scale =0.2
        self.add_tag('ufo')    
    def on_update(self, dt):
        self.y -=2
        if self.is_touching_any_sprite_with_tag('laser'):
            self.image = ('boom.gif')
            self.scale=0.5
            if self.scale < 0:
                self.scale -= 0.01
                self.delete()
        if self.is_touching_window_edge():
            self.delete()
def ufo():
    window.create_sprite(make_ufo)
Scheduler.update(ufo, 1)


class make_rock (Sprite):
    def on_create (self):
       self.image = 'rock1.png'
       self.scale= 0.35
       self.goto_random_position()
       self.y = 850
       self.rotation = 270
    def on_update(self, dt):
        self.move_forward(1.5)
        
def rock():
    window.create_sprite(make_rock)
        
Scheduler.update(rock, 2)

class make_rock2 (Sprite):
    def on_create (self):
       self.image = 'rock2.png'
       self.scale= 0.1
       self.goto_random_position()
       self.y = 850
       self.rotation = 270
    def on_update(self, dt):
        self.move_forward(1)
def rock2():
    window.create_sprite(make_rock2)
        
Scheduler.update(rock2, 3)

window.run()