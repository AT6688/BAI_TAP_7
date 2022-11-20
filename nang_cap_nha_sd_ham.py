import turtle
import math

t = turtle.Turtle()
t.pensize(3)
t.speed(0)
turtle.bgcolor("#FDF5E6")

def draw_rectange(t,toa_do,a,b,mau):
    t.penup()
    t.goto(toa_do)
    t.pendown()
    t.fillcolor(mau)
    t.begin_fill()
    for i in range(2):
        t.forward(a)
        t.left(90)
        t.forward(b)
        t.left(90)
        
    t.end_fill()
    
def draw_triangle(t,toa_do,c,mau):
    t.penup()
    t.goto(toa_do)
    t.pendown()
    t.fillcolor(mau)
    t.begin_fill()

    d = c/(math.sqrt(2))
    t.forward(c)
    t.left(135)
    t.forward(d)
    t.left(90)
    t.forward(d)
    t.left(135)

    t.end_fill()
    
#nha chinh    
draw_rectange(t,(-200,0),400,200,"#DAA520")

#cua
draw_rectange(t,(-50,0),100,120,"#8B4513")

#ong khoi
draw_rectange(t,(0,200),20,150,"gray")

#mai nha
draw_triangle(t,(-200,200),300,"#DC143C")

#cay 1
draw_triangle(t,(250,50),300,"#006400")
draw_triangle(t,(300,200),200,"#006400")
draw_triangle(t,(350,300),100,"#006400")

draw_rectange(t,(375,-100),50,150,"brown")

turtle.done()