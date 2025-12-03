# create a function that print a message based on the age of the user if user is above 18 user can drive and if user is not above 18 user is not eligable to drive
# create a function that prints number from 1 to 10 that shows if the number is even or odd
# write a function that add to an exsistng list


def can_drive(age):
     if age >= 18:
             print("You can drive")
     else:
             print("You can't drive")


def check_odd_even():
    for number in range(1,11): 
         if number % 2 == 0:
            print(f"{number} is Even")
         else:
            print(f"{number}is odd")
               
def add_single_item(my_list, item):
     my_list.append(item)

my_fruits =["apple","watermelon"]
add_single_item(my_fruits,"banana")
print(my_fruits)

my_bag =["pencil","ruler"]
add_single_item(my_bag,"pen")
print(my_bag)

check_odd_even()

can_drive(6)

import turtle
import random


screen = turtle.Screen()
screen.bgcolor("black") 
screen.title("Random Turtle Art")

t = turtle.Turtle()
t.speed(0)
t.hideturtle
turtle.colormode(255)

def get_random_color():
    """Generates a random RGB color tuple."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


for i in range(300):
    t.pencolor(get_random_color())

    t.forward(i + 10) 
    
    t.right(random.randint(90, 95)) 
    

    t.width(i / 100 + 1)

turtle.done()

def calculate_square_area(side):
  """Calculates the area of a square given its side length."""
  return side * side

side_length = 5
area = calculate_square_area(side_length)
print(f"The area of a square with side {side_length} is {area}")



