from pycat.core import Window,Sprite, KeyCode, Scheduler

window = Window(background_image='img/background.jpg')
 
class player (Sprite):
    def on_create(self):
        self.image = 'img/player.png'
        self.x = 200
        self.y = 170
        self.scale = 0.1
        self.Score = 10
    def on_update(self,dt):
        if window.is_key_pressed(KeyCode.A):
            self.scale_x =-1
            self.x -= 15
        if window.is_key_pressed(KeyCode.D):
            self.scale_x =1
            self.x +=15
        if player.Score >20:
            window.close()
            
           
player = window.create_sprite(player)

#monster
class monster (Sprite):
    def on_create(self):
        self.image= 'img/monster.png'
        self.goto_random_position()
        self.y = 630
        self.scale = 0.4
    def on_update(self, dt):
        self.y -=3
        if self.is_touching_any_sprite():
            player.Score -= 2
            print(player.Score)
            self.delete()

        if self.y < 0 :
            self.delete() 
def makemonster():
    window.create_sprite(monster)
Scheduler.update(makemonster, 1)   


#heart
class heart (Sprite):
    def on_create(self):
        self.image= 'img/heart.png'
        self.goto_random_position()
        self.y = 630
        self.scale = 0.07
    def on_update(self, dt):
        self.y -=3
        if self.is_touching_any_sprite():
            player.Score += 1
            print(player.Score)
            self.delete()
        if self.y < 0 :
            self.delete() 
def makeheart():
    window.create_sprite(heart)
Scheduler.update(makeheart, 1)




window.create_sprite(monster)
window.create_sprite(heart)
window.run()