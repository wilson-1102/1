from turtle import position
from pycat.core import Window, Scheduler, Sprite, KeyCode, Label
window = Window()
class Player (Sprite):
    def on_create(self):
        self.image = ('player.png')
        self.position = (0,0)
        self.scale = 0.4
        self.add_tag('player')
    def on_update(self, dt):    
        if window.is_key_pressed(KeyCode.W):
            self.y += 5
        if window.is_key_pressed(KeyCode.A):
            self.x -= 5
            self.scale = 0.2
            self.image = ('player2.png')
        if window.is_key_pressed(KeyCode.S):
            self.y -= 5
        if window.is_key_pressed(KeyCode.D):
            self.x += 5
            self.scale = 0.4
            self.image = ('player.png')
    def on_left_click_anywhere(self):
        if self.is_touching_any_sprite_with_tag('Gun'):
            window.create_sprite(Player_bullet)

player = window.create_sprite(Player)

class Player_bullet (Sprite):
    def on_create(self):
        self.scale = 0.2
        self.position = player.position
        self.image = ('bullet.gif')
        self.add_tag('player_bullet')
        self.point_toward_mouse_cursor()
    def on_update(self, dt):
        self.move_forward(4)
        if self.is_touching_window_edge():
            self.delete()

class Baseball_bat (Sprite):
    def on_create(self):
        self.scale = 0.3
        self.position = (600, 600)
        self.image = ('baseball_bat.png')
        self.add_tag('baseball_bat')
    def on_update(self, dt):
        if self.is_touching_any_sprite_with_tag('player'):
            self.position = player.position
            self.scale = 0.3
        if self.is_touching_any_sprite_with_tag('Gun'):
            self.delete
window.create_sprite(Baseball_bat)

class Gun (Sprite):
    def on_create(self):
        self.scale = 0.1
        self.position =(200, 500)
        self.image = ('gun.png')
        self.add_tag('Gun')
    def on_update(self, dt):
        if self.is_touching_any_sprite_with_tag('player'):
            self.position = player.position
            self.rotation = player.rotation
            self.scale = 0.1
        if self.is_touching_any_sprite_with_tag('baseball_bat'):
            self.delete
window.create_sprite(Gun)
window.run()