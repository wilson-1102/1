from pycat.core import Window,Sprite, KeyCode

window = Window(background_image='img/street.jpg')

class berd (Sprite):
    def on_create(self):
        self.image = 'img/berd.png'
        self.x = 200
        self.y = 200
    def on_update(self,dt):
        self.move_forward(5)
        if window.is_key_down(KeyCode.W):
            self.rotation = 90
        if window.is_key_down(KeyCode.S):
            self.rotation = 270
        if window.is_key_down(KeyCode.A):
            self.rotation = 180
        if window.is_key_down(KeyCode.D):
            self.rotation = 0
class eagle(Sprite):
    def on_create(self):
        self.image =  'img/eagle.png'
        self.x = 500
        self.y = 500
        self.scale = 0.5
    def on_update(self, dt):
        self.rotation = 0
        self.move_forward(10)
        if self.is_touching_window_edge():
            self.rotation += 180

window.create_sprite(eagle)
window.create_sprite(berd)
window.run()