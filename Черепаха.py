import turtle
import random

def createZone():
    painter.goto(-300, -300)
    painter.pendown()  # начать рисовать
    painter.goto(-300, 300)
    painter.goto(300, 300)
    painter.goto(300, -300)
    painter.goto(-300, -300)


screen = turtle.Screen() # создание объекта "экран"
t = turtle.Turtle() # создание объекта "черепашка"
t.shape('turtle') # изменение формы объекта
t.speed(9) # установка скорости
painter = turtle.Turtle()
painter.speed(0)
createZone()

a = ["forward", "back", "left", "right"]
while True:
    if t.xcor() < 299 and t.ycor() < 299 and t.xcor() > -299 and t.ycor() > -299:
        a = random.random
        print(a)
        t.a(10)
    else:
        t.back(10)
        temp = random.randint(120, 180)
        t.left(temp)


