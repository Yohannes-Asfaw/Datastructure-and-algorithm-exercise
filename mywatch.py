import time
import turtle
from turtle import *

time.time()
bob = Turtle()
sc = Screen()
sc.setup(600, 500)
sc.title("analog clock")
sc.bgcolor("light green")
sc.tracer(0)
bob.hideturtle()
bob.speed(1)
bob.pensize(5)

circle = Turtle()
circle.color("light blue", "light blue")
circle.begin_fill()
circle.penup()
circle.goto(0, -200)
circle.pendown()
circle.pensize(3)
circle.circle(200)
circle.hideturtle()
circle.end_fill()


def drawing(a, b, c, pnt):
   pnt.hideturtle()
   pnt.penup()
   pnt.goto(0, 0)
   pnt.pendown()
   pnt.penup()
   pnt.goto(0, 0)
   pnt.setheading(90)
   pnt.pensize(3)

   # start drawing the hour division
   for i in range(12):
       pnt.forward(160)
       pnt.pendown()
       pnt.forward(40)
       pnt.penup()
       pnt.backward(200)
       pnt.right(30)
   pnt.pensize(2)
   # start drawing the minute division
   for i in range(60):
       pnt.forward(180)
       pnt.pendown()
       pnt.forward(20)
       pnt.penup()
       pnt.goto(0, 0)
       pnt.right(6)

   pnt.goto(0, 0)
   pnt.setheading(60)
   pnt.fd(130)
   pnt.write("1", move=False, align="center", font=("arial", 10, "normal"))

   pnt.goto(0, 0)
   pnt.setheading(25)
   pnt.fd(140)
   pnt.write("2", move=False, align="center", font=("arial", 10, "normal"))

   pnt.goto(0, 0)
   pnt.setheading(-6)
   pnt.fd(150)
   pnt.write("3", move=False, align="center", font=("arial", 10, "normal"))

   pnt.goto(0, 0)
   pnt.setheading(-35)
   pnt.fd(160)
   pnt.write("4", move=False, align="center", font=("arial", 10, "normal"))

   pnt.goto(0, 0)
   pnt.setheading(-63)
   pnt.fd(160)
   pnt.write("5", move=False, align="center", font=("arial", 10, "normal"))

   pnt.goto(0, 0)
   pnt.setheading(-89)
   pnt.fd(160)
   pnt.write("6", move=False, align="center", font=("arial", 10, "normal"))

   pnt.goto(0, 0)
   pnt.setheading(-116)
   pnt.fd(160)
   pnt.write("7", move=False, align="center", font=("arial", 10, "normal"))

   pnt.goto(0, 0)
   pnt.setheading(-143)
   pnt.fd(152)
   pnt.write("8", move=False, align="center", font=("arial", 10, "normal"))

   pnt.goto(0, 0)
   pnt.setheading(-173)
   pnt.fd(150)
   pnt.write("9", move=False, align="center", font=("arial", 10, "normal"))

   pnt.goto(0, 0)
   pnt.setheading(-205)
   pnt.fd(136)
   pnt.write("10", move=False, align="center", font=("arial", 10, "normal"))

   pnt.goto(0, 0)
   pnt.setheading(-240)
   pnt.fd(130)
   pnt.write("11", move=False, align="center", font=("arial", 10, "normal"))

   pnt.goto(0, 0)
   pnt.setheading(-270)
   pnt.fd(126)
   pnt.write("12", move=False, align="center", font=("arial", 10, "normal"))

   pnt.goto(0, 0)
   pnt.setheading(90)
   pnt.fd(0)
   pnt.setheading(0)
   pnt.fd(5)
   pnt.write("YOHANNES ASFAW ", move=False, align="center", font=("arial", 10, "normal"))
   # drawing the hour hand

   pnt.penup()
   pnt.goto(0, 0)
   pnt.pencolor("red")
   pnt.setheading(90)
   angle = (a / 12) * 360
   pnt.right(angle)
   pnt.pendown()
   pnt.forward(80)

   # drawing the minute hand
   pnt.penup()
   pnt.goto(0, 0)
   pnt.pencolor("blue")
   pnt.setheading(90)
   angle = (b / 60) * 360
   pnt.right(angle)
   pnt.pendown()
   pnt.forward(120)

   # drawing the second hand
   pnt.penup()
   pnt.goto(0, 0)
   pnt.pencolor("yellow")
   pnt.setheading(90)
   angle = (c / 60) * 360
   pnt.right(angle)
   pnt.pendown()
   pnt.forward(160)
   pnt.pencolor("black")


try:
   while True:
       h = int(time.strftime("%I"))
       s = int(time.strftime("%S"))
       m = int(time.strftime("%M"))
       drawing(h, m, s, bob)
       sc.update()
       time.sleep(1)
       bob.clear()
except:
   turtle.Terminator()

