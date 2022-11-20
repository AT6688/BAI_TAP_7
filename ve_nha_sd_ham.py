import turtle

t = turtle.Turtle()
#t.hideturtle()
t.pencolor = "black"
t.speed(0)
t.pensize(3)
turtle.screensize(800,800)
t.hideturtle()

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

#hcn lon
draw_rectange(t,(-200,0),200,300,"brown")
draw_rectange(t,(0,0),200,300,"brown")
draw_rectange(t,(-200,-300),200,300,"brown")
draw_rectange(t,(0,-300),200,300,"brown")

#hnc nho
draw_rectange(t,(-150,100),100,150,"#DAA520")
draw_rectange(t,(50,100),100,150,"#DAA520")
draw_rectange(t,(-150,-200),100,150,"#DAA520")
draw_rectange(t,(50,-200),100,150,"#DAA520")

#toa nha ben canh
draw_rectange(t,(200,-300),300,300,"gray")
draw_rectange(t,(300,-300),50,200,"#4682B4")
draw_rectange(t,(350,-300),50,200,"#4682B4")


turtle.done()