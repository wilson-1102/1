
from pycat.core import Window, Sprite
from pycat.extensions.turtle import Turtle

window = Window()

turtle =  window.create_sprite(Turtle ,image = 'turtle.png', scale = 0.2 , position = (400, 500))
pencil =  window.create_sprite(Turtle ,image = 'pencil.png', scale = 0.06, position = (100,500) )
#U
pencil.turn_right(90)
pencil.move_forward(300)
pencil.turn_right(270)
pencil.move_forward(100)
pencil.turn_right(270)
pencil.move_forward(300)
#A
for _ in range (2):
    turtle.turn_right(90)
    turtle.move_forward(300)
    turtle.turn_right(90)
    turtle.move_forward(100)
turtle.turn_right(80)
turtle.move_forward(300)
#R
turtle.position = (500,500)
turtle.rotation = (0)
turtle.turn_right(90)
turtle.move_forward(300)
turtle.turn_right(180)
turtle.move_forward(150)
turtle.turn_right(40)
turtle.move_forward(150)
#E
turtle.position = (630,500)
turtle.rotation = (0)
for _  in range (2):
    turtle.move_forward(100)
    turtle.turn_right(90)
    turtle.move_forward(150)
    turtle.turn_right(90)

turtle.turn_right(90)
turtle.move_forward(300)
turtle.turn_right(270)
turtle.move_forward(100)

#G
gay =  window.create_sprite(image = 'gay.png', scale = 2, position = (1000, 300))

window.run()