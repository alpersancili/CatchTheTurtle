import turtle
import random

screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch The Turtle")
FONT = ("Arial", 15, "normal")
my_score = 0
game_over = False

#Turtle List
turtles = []

#Score
score_turtle = turtle.Turtle()

#Countdown
countdown_turtle = turtle.Turtle()

def score():
    score_turtle.color("blue")
    score_turtle.hideturtle()
    score_turtle.penup()
    score_turtle.setposition(0,250)
    score_turtle.write(arg="Score: 0", move=False, align="center", font=FONT)

def set_up_turtle(row,col):
    new_turtle = turtle.Turtle()

    def handle_click(x, y):
        global my_score
        my_score += 1
        score_turtle.clear()
        score_turtle.write(arg=f"Score: {my_score}", move=False, align="center", font=FONT)

    new_turtle.onclick(handle_click)
    new_turtle.shape("turtle")
    new_turtle.color("green")
    new_turtle.shapesize(2)
    new_turtle.penup()
    new_turtle.goto(col * 100 - 200, 100 - row * 100)
    turtles.append(new_turtle)
    new_turtle.pendown()

#Create Turtle
def create_turtle():
    for row in range(4):
        for col in range(5):
            set_up_turtle(row, col)

#Hide Turtle
def hide_turtle():
    for t in turtles:
        t.hideturtle()

#Show Turtle
def show_turtle():
    hide_turtle()
    if not game_over:
        random.choice(turtles).showturtle()
        screen.ontimer(show_turtle,700)

def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.color("black")
    countdown_turtle.penup()
    countdown_turtle.setposition(0, 220)
    countdown_turtle.clear()
    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg=f"Time: {time}", move=False, align="center", font=FONT)
        screen.ontimer(lambda : countdown(time - 1), 1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtle()
        countdown_turtle.write(arg="GAME OVER!", move=False, align="center", font=FONT)

def execute_func():
    turtle.tracer(0)
    score()
    create_turtle()
    hide_turtle()
    show_turtle()
    countdown(10)
    turtle.tracer(1)

execute_func()
turtle.mainloop()