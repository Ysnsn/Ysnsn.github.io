from turtle import *
from time import sleep
def go_to(x, y):
    up()
    goto(x, y)
    down()
def small_Circle(size):  # 函数用于绘制心的小圆
    speed(10)
    for i in range(210):
        forward(size)
        right(0.786)
def big_Circle(size):  # 函数用于绘制心的大圆
    speed(10)
    for i in range(150):
        forward(size)
        right(0.3)
def line(size):
    speed(10)
    forward(51 * size)
def heart(x, y, size):
    go_to(x, y)
    left(150)
    begin_fill()
    line(size)
    big_Circle(size)
    small_Circle(size)
    left(120)
    small_Circle(size)
    big_Circle(size)
    line(size)
    end_fill()
def main():
    pensize(2)
    color('red', 'pink')
    getscreen().tracer(1, 0)
    heart(100, 0, 0.7)
    go_to(80, 70)
    write("洋洋", font=("楷体", 18, "normal"))
    setheading(0)
    heart(-80, -100, 1)
    go_to(-110, 15)
    write("杜杜", font=("宋体", 20, "normal"))
    go_to(40, -80)
    write("三生有幸遇见你！", move=True, align="left", font=("arial", 22, "italic"))
    done()
main()