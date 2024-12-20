from pycat.core import Window,Sprite, KeyCode
window = Window()

class monkey (Sprite):
    def on_create(self):
        self.image = 'img/monkey.jpg'
        self.y = 600
        self.scale = 0.1
            
    def on_update(self, dt):
        self.x +=600
        if self.is_touching_window_edge():
             self.x -= 1000


class cokoala (Sprite):
    def on_create(self):
        self.image = 'img/ANIMALS.jpg'
        self.y = 450
        self.scale = 0.2
        self.x = 0

    def on_update(self, dt):
        self.x += 700
        if self.is_touching_window_edge():
             self.x -= 1000


class dog (Sprite):
    def on_create(self):
        self.image = 'img/dog.jpg'
        self.y = 200
        self.scale = 0.4

    def on_update(self, dt):
        self.x += 800
        if self.is_touching_window_edge():
             self.x -= 940

class pig (Sprite):
    def on_create(self):
        self.image = 'img/pig.jpg'
        self.y = 100
        self.scale = 0.2
        self.x = 50
    def on_update(self, dt):
        if self.window.is_key_down(KeyCode.W):
            self.y += 10
        if self.window.is_key_down(KeyCode.S):
            self.y -= 10

window.create_sprite(cokoala)
window.create_sprite(monkey)
window.create_sprite(dog)
window.create_sprite(pig)
window.run()