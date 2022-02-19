import random
import turtle
from turtle import *

sc = Screen()  # initializing a screen
sc.bgcolor("light blue")
sc.setup(500, 500)
sc.tracer(0)
single_squar = Turtle()  # The name single_square is used because the grid will be draw using a .stamp in turtle
table = [[0, 0, 0, 0],  # This is the original grid
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]


# startgame function used to display the front page when the whole code is run
def startgame():
    turtle.title("2048 BY YOHANNES ASFAW")  # Title of the screen(display)
    single_squar.speed(0)
    single_squar.shape("square")
    single_squar.color("silver")
    single_squar.penup()
    single_squar.goto(0, 180)
    single_squar.turtlesize(4, 20)
    single_squar.color("white")
    single_squar.write("WELCOME TO 2048", align="center",
                       font=("normal", 20, "bold"))  # using .write to write text on the screen
    single_squar.goto(0, 80)
    single_squar.write("PRESS SPACE KEY TO START THE GAME", align="center", font=("normal", 15, "bold"))
    single_squar.hideturtle()


startgame()


# drawingtable draw the table or board to play using a square shaped turtle by stamping it in a correct sequence
def drawingtable():
    single_squar.goto(0, 180)
    single_squar.write("PRESS LEFT KEY TO MERGE", align="center", font=("normal", 15, "bold"))
    single_squar.hideturtle()
    single_squar.turtlesize(3, 3)  # single square size to be stamped
    x_initalpos = -100  # initial position of the turtle in x coordinate to draw the grid
    y_initialpos = 100  # initial position of the turtle in y coordinate to draw the grid
    y_pos_move = 0
    for i in range(4):
        x_pos_move = 0  # space between square in the x direction this is going to be incremented
        for j in range(4):
            if table[i][j] == 0:
                single_squar.color("white")
                single_squar.goto(x_initalpos + x_pos_move, y_initialpos - y_pos_move)
                single_squar.stamp()
                single_squar.sety(single_squar.ycor() - 15)
                # if the table's single square is initially 0 nothing is done
                single_squar.write("", align="center",
                                   font=("normal", 5, "bold"))
                single_squar.sety(single_squar.ycor() + 15)

            elif table[i][j] != 0:
                single_squar.color("grey")
                single_squar.goto(x_initalpos + x_pos_move, y_initialpos - y_pos_move)
                single_squar.stamp()
                single_squar.sety(single_squar.ycor() - 15)
                single_squar.color("white")
                single_squar.write(table[i][j], align="center",
                                   font=("normal", 20, "bold"))  # writing what have been entered
                single_squar.sety(single_squar.ycor() + 15)

            x_pos_move += 65  # correcting space between consecutive squares in the x direction
        y_pos_move += 65  # correcting space between consecutive squares in the y direction


# This function merge the numbers to the left according to the law of the game
# This function also accept the original list and return a new list with out altering the original list
def mergeleft(original_table):
    new_list = original_table
    # for loop to move the none zero numbers to the left
    for i in range(3):
        for row in range(4):
            for column in range(3, 0, -1):
                if new_list[row][column - 1] == 0:
                    new_list[row][column - 1] = new_list[row][column]
                    new_list[row][column] = 0
    # for loop to merge consecutive same numbers
    for row in range(4):
        for column in range(3):
            if new_list[row][column + 1] == new_list[row][column]:
                new_list[row][column] *= 2
                new_list[row][column + 1] = 0
    # for loop to move any zero numbers(space) after merging
    for i in range(3):
        for row in range(4):
            for column in range(3, 0, -1):
                if new_list[row][column - 1] == 0:
                    new_list[row][column - 1] = new_list[row][column]
                    new_list[row][column] = 0
    # for loop to insert 2 or 4 to a random index if the index value is 0
    addrandom(table)
    drawingtable()

    return new_list  # returning a new list with out altering the original


def mergeright(original_table):
    new_list = original_table
    # for loop to move the none zero numbers to the left
    for i in range(3):
        for row in range(4):
            for column in range(3):
                if new_list[row][column + 1] == 0:
                    new_list[row][column + 1] = new_list[row][column]
                    new_list[row][column] = 0
    # for loop to merge consecutive same numbers
    for row in range(3):
        for column in range(3):
            if new_list[row][column] == new_list[row][column + 1]:
                new_list[row][column + 1] *= 2
                new_list[row][column] = 0
    # for loop to move any zero numbers(space) after merging
    for i in range(3):
        for row in range(4):
            for column in range(3):
                if new_list[row][column + 1] == 0:
                    new_list[row][column + 1] = new_list[row][column]
                    new_list[row][column] = 0
    # for loop to insert 2 or 4 to a random index if the index value is 0
    addrandom(table)
    drawingtable()
    return new_list


def mergeup(original_table):
    new_list = original_table
    # for loop to move the none zero numbers to the left
    for i in range(3):
        for column in range(4):
            for row in range(3, 0, -1):
                if new_list[row - 1][column] == 0:
                    new_list[row - 1][column] = new_list[row][column]
                    new_list[row][column] = 0
    # for loop to merge consecutive same numbers
    for column in range(4):
        for row in range(3):
            if new_list[row + 1][column] == new_list[row][column]:
                new_list[row][column] *= 2
                new_list[row + 1][column] = 0
    # for loop to move any zero numbers(space) after merging
    for i in range(3):
        for column in range(3, 0, -1):
            for row in range(4):
                if new_list[row - 1][column] == 0:
                    new_list[row - 1][column] = new_list[row][column]
                    new_list[row][column] = 0
    addrandom(table)
    drawingtable()
    return new_list


def addrandom(original):
    for i in range(17):  # iterating through all 16 different indexes
        val = random.choice([2, 4])  # random choice from 2 and 4 to insert in to the table
        random_column_index = random.randint(0, 3)
        random_row_index = random.randint(0, 3)
        if original[random_column_index][random_row_index] == 0:
            original[random_column_index][random_row_index] = val
            break
        else:
            continue


# New function to execute a left key press and pass the necessary function
def leftpress():
    pass
    mergeleft(table)


def rightpress():
    pass
    mergeright(table)


def uppress():
    pass
    mergeup(table)


# New function to execute a space key press and pass the function drawingtable
def startgame():
    single_squar.clear()  # clearing the first page after displaying
    pass
    drawingtable()



sc.listen()
sc.onkeypress(leftpress, "Left")
sc.onkeypress(rightpress, "Right")
sc.onkeypress(uppress, "Up")
sc.onkeypress(startgame, "space")
sc.update()
mainloop()
