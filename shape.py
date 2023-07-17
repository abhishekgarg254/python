import turtle

def draw_body1():
    window=turtle.Screen()
    window.bgcolor("white")
    draw_Abhishek()
    window.exitonclick()

def draw_Abhishek():
    Abhishek=turtle.Turtle()
    Abhishek.shape("turtle")
    Abhishek.color("red")
    draw_head(Abhishek)
    draw_body(Abhishek)
    draw_arm(Abhishek)
    draw_leg1(Abhishek)
    draw_leg2(Abhishek)

def draw_head(Abhishek):
    Abhishek.circle(60)
    Abhishek.speed(3)
    Abhishek.right(60)

def draw_body(Abhishek):
    num=0
    while num<3:
        Abhishek.forward(150)
        Abhishek.right(120)
        Abhishek.speed(1)
        num+=1

def draw_arm(Abhishek):
    Abhishek.forward(60)
    Abhishek.left(60)
    Abhishek.forward(60)


    Abhishek.backward(60)
    Abhishek.right(60)
    Abhishek.backward(60)


    Abhishek.right(60)

    Abhishek.forward(60)
    Abhishek.right(60)
    Abhishek.forward(60)


    Abhishek.backward(60)
    Abhishek.left(60)
    Abhishek.forward(90)

def draw_leg1(Abhishek):
    Abhishek.left(120)
    Abhishek.forward(40)
    Abhishek.right(120)
    Abhishek.forward(120)
    draw_foot1(Abhishek)

def draw_leg2(Abhishek):
    Abhishek.right(180)
    Abhishek.forward(120)
    Abhishek.right(60)
    Abhishek.forward(70)
    Abhishek.right(60)
    Abhishek.forward(120)
    draw_foot2(Abhishek)

def draw_foot1(Abhishek):
    Abhishek.color("blue")
    num=0
    while num<4:
        Abhishek.forward(20)
        Abhishek.left(90)
        num+=1

def draw_foot2(Abhishek):
    Abhishek.color("blue")
    num=0
    while num<4:
        Abhishek.forward(20)
        Abhishek.left(90)
        num+=1

draw_body1()