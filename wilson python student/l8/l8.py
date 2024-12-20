

from pycat.core import Window,Sprite,Color, Point, Label


window = Window()


class startbutton (Sprite):
    def on_create(self):
        self.scale = 0.1
        self.image = 'button.png'
        self.position =(200,200) 
        
    def on_left_click(self):
        if stopwatch.is_running :
            stopwatch.is_running =False
        else:
            stopwatch.is_running = True

class watch (Label):
    def on_create(self):
        self.text = '0'
        self.position = Point(200,500)
        self.timer = 0
        self.is_running = False
    def on_update(self, dt):
        if self.is_running :
            self.timer += dt
        self.text = str(self.timer)
        


class resetbutton (Sprite):
    def on_create(self):
        self.scale = 0.1
        self.image = 'button2.png'
        self.position =(500,200) 
    def on_left_click(self):
        stopwatch.is_running =False
        stopwatch.timer = 0

window.create_sprite(image = 'image.png',x = 1000, y=300, scale = 1.5)
stopwatch = window.create_label(watch)
window.create_sprite(startbutton)
window.create_sprite(resetbutton)
window.run()