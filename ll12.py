
from turtle import up
from pycat.core import Window, Scheduler, Sprite, KeyCode, Label
import random
window = Window()
class Player (Sprite):
    def on_create(self):
        self.image = ('player-bl.png')
        self.position = (600,300)
        self.scale = 0.2
        self.add_tag('player')
        self.gun = False
        self.slash = False
    def on_update(self, dt):    
        if window.is_key_pressed(KeyCode.W) and not self.gun:
            self.image = ('player-bl.png')
            self.y += 5
        if window.is_key_pressed(KeyCode.A) and not self.gun:
            self.x -= 5
            self.scale = 0.2
            self.image = ('player-bl.png')
        if window.is_key_pressed(KeyCode.S) and not self.gun:
            self.image = ('player-br.png')
            self.y -= 5
        if window.is_key_pressed(KeyCode.D) and not self.gun:
            self.x += 5
            self.image = ('player-br.png')
            self.scale = 0.2
        if window.is_key_down(KeyCode.X):
            self.gun = True
        if window.is_key_down(KeyCode.Z):
            self.gun = False
        if window.is_key_pressed(KeyCode.D) and  self.gun:
            self.x += 5
            self.image = ('player-gr.png')
            self.scale = 0.2
        if window.is_key_pressed(KeyCode.W) and  self.gun:
            self.y += 5
            self.image = ('player-gr.png')
            self.scale = 0.2
        if window.is_key_pressed(KeyCode.S) and  self.gun:
            self.y -= 5
            self.image = ('player-gl.png')
            self.scale = 0.2
        if window.is_key_pressed(KeyCode.A) and  self.gun:
            self.x -= 5
            self.image = ('player-gl.png')
            self.scale = 0.2
        if window.is_key_down(KeyCode.SPACE) and  not self.gun:
            self.slash = True
            window.create_sprite(Slash)
    def on_left_click_anywhere(self):
        if player.gun == True:
            window.create_sprite(Player_bullet)

player = window.create_sprite(Player)

class Player_bullet (Sprite):
    def on_create(self):
        self.scale = 0.15
        self.position = player.position
        self.image = ('bullet.gif')
        self.add_tag('player_bullet')
        self.point_toward_mouse_cursor()
    def on_update(self, dt):
        self.move_forward(7)
        if self.is_touching_window_edge():
            self.enabled = False
            self.is_visible = False
            self.delete()
            return


class Slash (Sprite):
    def on_create(self):
        self.scale = 0.4
        self.position = player.position
        self.image = ('slash.png')
        self.add_tag('Slash')
        self.timer = 0
    def on_update(self, dt):
        if player.slash == True:
            self.rotation += 25
            self.timer += 1
        if self.timer ==  20:
            self.delete()

class make_dog (Sprite):
    def on_create(self):
        self.image = ('dog.png')
        self.goto_random_position()
       
        self.scale = 0.4
    def on_update(self, dt):
        self.point_toward_sprite(player)
        self.move_forward(3)
        if self.is_touching_window_edge():
            self.enabled = False
            self.is_visible = False
            self.delete()
            return
        if self.is_touching_any_sprite_with_tag('Slash'):
            self.enabled = False
            self.is_visible = False
            self.delete()
            return
        if self.is_touching_any_sprite_with_tag('player_bullet'):
            self.enabled = False
            self.is_visible = False
            self.delete()
            return
            
def dog():
    window.create_sprite(make_dog)
Scheduler.update(dog, 1.5) 

class make_enemy (Sprite):
    def on_create(self):
        self.image = ('monster.gif')
        self.goto_random_position()
        self.rotation = random.randint(0, 360)
        self.scale =0.1
        self.add_tag('enemy')
        self.time = 0
        self.bullet_time = 1
        self.point = 0 
    def on_update(self, dt):
        self.move_forward(0.5)
        self.time += dt
        if self.time > self.bullet_time:
            enemy_bullet = window.create_sprite(enemybullet)
            enemy_bullet.position = self.position
            enemy_bullet.point_toward_sprite(player)
            self.time = 0
        if self.is_touching_window_edge():
            self.enabled = False
            self.is_visible = False
            self.delete()
            return
        if self.is_touching_any_sprite_with_tag('Slash'):
            self.enabled = False
            self.is_visible = False
            self.point +=1
            self.delete()
            return
        if self.is_touching_any_sprite_with_tag('player_bullet'):
            self.enabled = False
            self.is_visible = False
            self.delete()
            return
            
def enemy():
    enemy = window.create_sprite(make_enemy)
Scheduler.update(enemy, 3)  

class kills (Label):
    def on_create (self):
        self.text = '0'
        self.position = 1035, 80
    def on_update(self, dt):
        self.text  = str(enemy.point)
window.create_label(kills)
class enemybullet (Sprite):
    def on_create(self):
        self.image = 'blue.png'
        self.scale = 0.1
        self.add_tag('enemy_bullet')
    def on_update(self, dt):
        self.move_forward (3)
        if self.is_touching_window_edge():
            self.delete()
        if self.is_touching_any_sprite_with_tag('Player'):
            self.delete()

window.create_sprite(image = 'gun-image.png', x = 60, y = 40, scale = 0.1)      
window.create_sprite(image = 'baseball-bat-image.png', x = 170, y = 40, scale = 0.123)  

window.run()