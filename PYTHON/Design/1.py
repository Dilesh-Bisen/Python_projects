from turtle import *

color("cyan")
bgcolor("black")
speed(1500)
right(45)
for n in range(100):
    if 14 < n < 60:
        left(5)
    if 80 < n < 150:
        right(10)
    circle(40)
    if n < 100:
        forward(15)
    else:
        forward(1)
