#CTI 110
#M5LAB
#October 16



import turtle

wn = turtle.Screen()
t= turtle.Turtle()
wn.bgcolor("cyan")
t.pencolor("orange")

t.penup()
t.forward(90)
t.right(30)
t.pendown()


def main():
    t.speed(10)
    for m in range(8):
        t.forward(45)
        t.backward(18)
        t.left(50)
    t.left(90)
    t.forward(90)



    t.penup()
    t.forward(50)
    t.left(35)
    t.forward(80)
    t.pendown()
for n in range(20):



    main()
