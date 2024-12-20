
from pycat.core import Window, Scheduler, Sprite, KeyCode, Label
window = Window()
class Player (Sprite):
    def on_create(self):
        self.image = ('player-bl.png')
        self.position = (0,0)
        self.scale = 0.4
        self.add_tag('player')
        self.gun = False

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
        if window.is_key_down(KeyCode.Z):
            self.gun = True
        if window.is_key_down(KeyCode.X):
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
    def on_left_click_anywhere(self):
        if player.gun == True:
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
        if self.is_touching_any_sprite_with_tag('Gun'):
            self.delete
    def on_update(self, dt):
        if self.is_touching_any_sprite_with_tag('player'):
            self.position = player.position
            self.scale = 0.3
        if self.is_touching_any_sprite_with_tag('Gun'):
            self.delete
window.create_sprite(Baseball_bat)
class Slash (Sprite):
    def on_create(self):
        self.scale = 0.1
        self.position =(200, 500)
        self.image = ('slash.png')
        



#window.create_sprite(arms, )
window.run()