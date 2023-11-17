import turtle
from random import randint
turtle.colormode(255)
turtle.speed(0)


def draw_house(
        x=0,
        y=0,
        base_w=100,
        base_h=10,
        base_color='grey',
        walls_w=100,
        walls_h=150,
        walls_color='red',
        roof_w=120,
        roof_h=70,
        roof_color='black'
    ):
    '''
    контракт:
        x - левый нижний угол фундамента
        y - левый нижний угол фундамента
        ширина фундамента
        высота фундамента
        цвет фундамента
        ширина стен
        высота стен
        цвет стен
        ширина крыши
        высота крыши
        цвет крыши

    вызвать функцию строительства фундамента
    вызвать функцию строительства стен
    вызвать функцию строительства крыши
    '''
    draw_base(x, y, base_w, base_h, base_color)
    walls_y = y + base_h
    draw_walls(x, walls_y, walls_w, walls_h, walls_color)
    roof_y = walls_y + walls_h
    draw_roof(x, roof_y, roof_w, roof_h, roof_color, walls_w)


def draw_base(x, y, base_w, base_h, base_color):
    ''' рисует фундамент '''

    draw_rectangle(x, y, base_w, base_h, base_color)


def draw_walls(x, y, walls_w, walls_h, walls_color):
    '''
    рисует стены
    из каих координат?
    '''

    draw_rectangle(x, y, walls_w, walls_h, walls_color)


def draw_roof(x, y, roof_w, roof_h, roof_color, walls_w):
    ''' рисует крышу '''
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(roof_color)
    turtle.begin_fill()

    turtle.fd(walls_w // 2)
    turtle.fd(roof_w // 2)
    top_x = x + walls_w // 2
    top_y = y + roof_h
    turtle.goto(top_x, top_y)
    left_x = top_x - roof_w // 2
    turtle.goto(left_x, y)
    turtle.fd(roof_w // 2)
    turtle.end_fill()
    turtle.goto(x, y)
    turtle.penup()



def draw_rectangle(x, y, width, height, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.fd(width)
    turtle.lt(90)
    turtle.fd(height)
    turtle.lt(90)
    turtle.fd(width)
    turtle.lt(90)
    turtle.fd(height)
    turtle.lt(90)
    turtle.end_fill()
    turtle.penup()



def draw_street(first_house_x=0, first_house_y=0, houses=10):
    counter = 0
    print('рисуем улицу')
    while counter < houses:
        base_w = randint(50, 100)
        walls_w = randint(base_w - 10, base_w)
        roof_w = randint(walls_w, walls_w + 50)
        draw_house(
            x = first_house_x,
            y = first_house_x,
            base_w=base_w,
            base_h=randint(10, 20),
            base_color=(randint(0, 255), randint(0, 255), randint(0, 255)),
        )
        counter += 1
        first_house_x += 200
        



draw_street()

turtle.done()
