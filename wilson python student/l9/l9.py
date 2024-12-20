
from pycat.core import Window, Scheduler, Sprite, Label, KeyCode
import random
window = Window()
class Hero (Sprite):
    def on_create(self):
        self.add_tag('hero')
        self.image = '0.png'
        self.position = (500,500)
        self.scale= 0.5
        
    def on_update(self, dt):
        self.move_forward(6)
        if window.is_key_down(KeyCode.W):
            self.rotation = 90
            
        if window.is_key_down(KeyCode.S):
            self.rotation = 270
            
        if window.is_key_down(KeyCode.A):
            self.rotation = 180
            self.image = '180.png'
        if window.is_key_down(KeyCode.D):
            self.rotation = 0
            
class monster (Sprite):
    def on_create(self):
        self.image = 'monster.gif'
        self.position = (640,150)
        self.scale= 0.3
        Scheduler.update(self.throw, 2)
    def throw (self):
        window.create_sprite(ball ,position = self.position ,rotation =random.randint(45,135))

class ball (Sprite):
    def on_create(self):
       self.image = 'bad.png'
       self.scale = 0.1
    def on_update(self, dt):
        self.move_forward(5)
        if self.y >= 630:
            self.delete()
        if self.is_touching_any_sprite_with_tag('hero'):
            window.close()
class make_coin (Sprite):
    def on_create (self):
       self.image = 'coin.png'
       self.scale= 0.05
       
    def on_update(self, dt):
        self.goto_random_position()
        if self.is_touching_any_sprite_with_tag('hero'):
            point.Score += 1
 
def coin():
    window.create_sprite(make_coin)

Scheduler.update(coin, 2) 

class point (Label):
    def on_create(self):
        self.position = (100,500)
        point.Score = 0
        
    def on_update(self, dt):
        self.text = str(point.Score)
 

 

window.create_label(point)
window.create_sprite(monster)
hero = window.create_sprite(Hero)
window.run()