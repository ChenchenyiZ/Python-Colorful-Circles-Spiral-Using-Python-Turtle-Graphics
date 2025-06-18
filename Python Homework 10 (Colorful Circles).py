import turtle
t=turtle.Turtle()
t.speed(100)

turtle.bgcolor("black")
cols=('purple','orange','yellow','blue','green','red')
#circle=['10','15','20','25','30','35']

t.pensize(5)

for n in range(36):
    t.penup()
    t.goto(0,0)
    t.circle(300,10)
    r=2
    d=25
    for i in range(6):
        t.begin_fill()
        r=r+1
        d=d+2
        t.penup()
        t.circle(r)
        t.color(cols[i])
        t.end_fill()
        t.forward(d)

        


t.hideturtle()
print(t.xcor(),t.ycor())
