from pyclbr import Class
from pycat.core import Window, Color,Sprite

window = Window()
ANIMALS = input("what animal do u want to see?")

COLOR = input('What color do u want to see?')


ANIMALS_sprite = window.create_sprite()

ANIMALS_sprite.scale = 0.7
ANIMALS_sprite.x =600
ANIMALS_sprite.y = 300

if COLOR == 'RED':
    ANIMALS_sprite.color = Color.RED

if COLOR == 'BLUE':
    ANIMALS_sprite.color = Color.BLUE

if COLOR == 'GREEN':
    ANIMALS_sprite.color = Color.GREEN

if ANIMALS =="cokoala":
    ANIMALS_sprite.image = "ANIMALS.jpg"


cokoala_detail = print('the ANIMALS postation', ANIMALS_sprite.x, ',' ,ANIMALS_sprite.y,'and the ANIMALS SIZE is' ,ANIMALS_sprite.scale, )
print (cokoala_detail)

class animal(sprite):
    def on_creat(self)

window.run()