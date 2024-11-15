from pycat.core import Window 

window = Window()

ANIMALS = input("what animal do u want to see?")



ANIMALS_sprite = window.create_sprite()
ANIMALS_sprite.scale = 0.5
ANIMALS_sprite.x =600
ANIMALS_sprite.y = 300


if ANIMALS =="cokoala":
    ANIMALS_sprite.image = "ANIMALS.jpg"
       

if ANIMALS =="monkey":
    ANIMALS_sprite.image = "monkey.jpg"
    
size = input("Do u want it to be big or small?")

if size == "big":
    ANIMALS_sprite.scale = 0.8
 
if size == "small":
    ANIMALS_sprite.scale =0.3


window.run()