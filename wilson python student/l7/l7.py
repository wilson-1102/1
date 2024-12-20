from pycat.core import Window,Sprite,Scheduler, RotationMode, Player

window = Window(background_image='forest.png')

class bird (Sprite):
    def on_create(self):
        self.image = 'bird.png'
        self.scale = 0.1
        self.y = 500
        self.x  = 100
    def on_update (self,dt):
        self.move_forward(10)
        if self.is_touching_window_edge():
            self.rotation += 270


window.create_sprite(bird)
class make_tnt (Sprite):
    def on_create(self):
        self.image = 'tnt.png'
        self.scale = 0.4
        self.goto_random_position()    
        self.has_been_clicked = False
    def on_update (self,dt):
        if self.has_been_clicked == True:
            self.y += 10
        if self.is_touching_window_edge():
            self.delete()
        if self.is_touching_any_sprite():
            self.delete()       
    def on_left_click(self):
        self.has_been_clicked == True

def tnt():
    window.create_sprite(make_tnt)        

Scheduler.update(tnt, 1)
window.run()