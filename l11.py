from turtle import position
from pycat.core import Window, Scheduler, Sprite, KeyCode
import random
window = Window()

class player (Sprite):
    def on_create(self):
        self.image = ('player.png')
        self.position = (600,300)
        self.scale = 0.1
        self.add_tag('player')
    def on_update(self, dt):    
        if window.is_key_pressed(KeyCode.W):
            self.y += 5
        if window.is_key_pressed(KeyCode.A):
            self.x -= 5
        if window.is_key_pressed(KeyCode.S):
            self.y -= 5
        if window.is_key_pressed(KeyCode.D):
            self.x += 5
def on_leftclick_anywhere(self):
    window.create_sprite(player_bullet)

class make_ememy (Sprite):
    def on_create(self):
        self.image = ('Mew.png')
        self.goto_random_position()
        self.rotation = random.randint(0, 360)
        self.scale =0.2
        self.add_tag('enemy')
    def on_update(self, dt):
        self.move_forward(3.5)
        if self.is_touching_window_edge():
            self.delete()
def enemy():
    window.create_sprite(make_ememy)
Scheduler.update(enemy, 0.8)       
class player_bullet (Sprite):
    def on_create(self):
        self.image = ('bullet.gif')
        self.add_tag('player_bullet')
    def on_update(self, dt):
        self.move_forward(5)
        if self.is_touching_window_edge():
            self.delete()
        if self.is_touching_any_sprite_with_tag('Mew'):
            self.delete()
window.create_sprite(player_bullet)   
window.run()



