
# Practice: Scope & LEGB Rule

massage = "Global"

def show_massage():
    massage = "Local"
    print(massage)

show_massage()
print(massage)

# Python searches in this order:

# L - Local
# E - Enclosing
# G - Global
# B - Buillt-in

print(len("Python"))



# Practice: Basic Functions

def calculate_total(price, qauntity):
    total = price * qauntity
    return total

result = calculate_total(20, 3)

print(result)


def outer():
    course ="Python"

    def inner():
        print(course)

    inner()
outer()


tax_rate = 0.15

def calculate_tax(amount):
    return amount * tax_rate

print(calculate_tax(200))



# Practice: Built-in Shadowing & Lists

score = [80, 90, 100]

print(len(score))
print(sum(score))
print(type(score))


list = [1, 2, 3]

# list("abc") now fails because 
# list refars to the variable above

student_list = [1, 2, 3]



# Practice: Modules & Imports

# math is a standard-library module
import math

radius = 4
area = math.pi * radius ** 2
print(area)


from math import sqrt,pi
print(sqrt(49))
print(pi)

# Avoid: from math import *


import datetime as dt 
from math import factorial as fact

today = dt.date.today()
print(today)
print(fact(5))


import random
import statistics
score = [82, 91, 75, 88]

print(random.choice(score))
print(statistics.mean(score))



# Practice: Main Guard & Modules

# calculator.py

def add(a, b):
    return a+b

#main.py 
# import 

def greet(name):
    return f"Hello,  {name}"

if __name__ == "__name__":
    print(greet("Sara"))

# Assignment

# Creat grades.py with calculate_grade(score)
# Return A, B, C, D or F from the function
# Creat main.py and import the grades module
# Call graded.calculate_grade() with several score 
# Add a main guard so tests run only when main.py is executed



# LAB 1

course = "Web Development Bootcamp"
duration = 12

def type(course):

    print("Opss!")


print(course)
print(duration)
print(type(course))
print(globals())



# LAB 2

building1 = "Tuwaiq"

cohrot_size = 20

print(f"Welcome to {building1}, class limit  is {cohrot_size}")
print("Tuwaiq" in building1)
print("cohort_size" in globals())
print(globals()["course"])

# shift + alt + dowen



# LAB 3

location = "Global"
def outter():
    location = "Outter"
    print(f"From {location}")
    def inner():
        location = "Inner"
        print(f"From {location}")
    inner()
outter()



# LAB 4

location = 0
def outter():
    location = 1
    print(f"From {location}")
    def inner():
        nonlocal location
        location += 2
        print(f"From {location}")
    inner()
outter()



# LAB 5

def printer():
    print("Welcome")

def desk():
   printer()
def room():
    desk()
def house():
    room()

def city():
    house()
def country():
    city()
country()



# LAB 6

language = "Python"

def show_language(language):
    print(language)

show_language("Dart")
print(language)



# LAB 7

rate = 0.15
def getTotal(amount):
    total = amount * rate + amount
    return total

print(f"{getTotal(199.99):.2f}")
print(round(getTotal(199.99)))



# LAB 8

def inspacet_order(item, qty):
    subtotal = 25 * qty
    print(locals())
    print(locals()["subtotal"])
inspacet_order("pen", 10)