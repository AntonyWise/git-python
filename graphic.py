# coding: utf-8

import turtle
import random
import math

import robot

PHI = 360.0/7
R = 50


def goto(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def draw_circle(r, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()


def draw_gun_drum(base_x, base_y):
    goto(base_x, base_y)
    turtle.circle(80)
    goto(base_x, base_y + 160)
    draw_circle(5, 'red')

    for i in range(0, 7):
        phi_rad = PHI * i * math.pi / 180.0
        goto(base_x + math.sin(phi_rad) * R, base_y + math.cos(phi_rad) * R + 60)
        # turtle.circle(22)
        # draw_circle(22, 'brown')
        draw_circle(22, 'white')


def draw_drum_rotation(base_x, base_y, start):
    for i in range(start, random.randrange(7, 21)):
        phi_rad = PHI * i * math.pi / 180.0
        goto(base_x + math.sin(phi_rad) * R, base_y + math.cos(phi_rad) * R + 60)
        # turtle.circle(22)
        draw_circle(22, 'brown')
        draw_circle(22, 'white')

    goto(base_x + math.sin(phi_rad) * R, base_y + math.cos(phi_rad) * R + 60)
    draw_circle(22, 'brown')

    return i % 7


turtle.speed(0)

answer = ''
start = 0

draw_gun_drum(100, 100)

while answer != 'N':
    answer = turtle.textinput("Let's play?", "[Y/N]")

    if answer == 'Y':
        start = draw_drum_rotation(100, 100, start)

        # start = 0 -- тест вызова ф-ции копирования файлов
        if start == 0:
            goto(-150, 250)
            turtle.write("You lose!", font=("Arial", 18, "normal"))
            robot.duple_files(".")  # . - тукещая директория
        else:
            goto(-150, 250)
            turtle.write("You won!", font=("Arial", 18, "normal"))

        '''turtle.penup()
        turtle.goto(random.randrange(1,100), random.randrange(-200,200))  # x,y
        turtle.pendown()
        turtle.fillcolor(random.random(), random.random(), random.random())
        turtle.begin_fill()
        turtle.circle(random.randrange(1,100))
        turtle.end_fill()'''

    else:
        pass
