
# Main Assignment: Calculate Grade Function

# Defining a function that takes a score and returns the grade using if/elif/else conditions.

#Define calculate_grade(score)
#Use score as the function parameter
#Use if \ elif \ else to select A, B, C, D, or F
#Return the grade instead of printing it inside the function
#Call the function with several scores and print the returned grades


def calculate_grade(score):
    if score >= 90 and score <=100:
        return "A".strip()
    elif score >= 80 and score <=89:
        return "B".strip()
    elif score >= 70 and score <= 79:
        return "C".strip()
    elif score >= 60 and score <=69:
        return "D".strip()
    else:
        return "You Need work hard"
print(calculate_grade(90))
print(calculate_grade(81))
print(calculate_grade(55))



# LAB 1: Basic Function Definition

# Defining a simple function without parameters.

def greet():
    print("Welcom to python")
greet()



# LAB 2: Calling a Function Multiple Times

# Creating a menu function to demonstrate code reusability.

def show_menu():
    print("1- Coffee")
    print("2- Tea")
    print("3- Ginger")
show_menu()
print("Outsid the call")
show_menu()



# LAB 3: Variable Scope and Nested Functions

# Demonstrating that a nested function cannot be called globally.

def unknowScope():
 print("Line one")
 def gotoFunc():
    print("From within the GoTo")
 print("Where is line 2 ?")
 gotoFunc()

 print("I' am up here")



# LAB 4: Functions with Parameters

# Passing an argument (name) to a function to print a dynamic message.

def greet_student(name):
    print(f"Welcom  {name}")
greet_student("Nasser")
greet_student(" Abdullah")



# LAB 5: Input Validation Inside a Function

# Passing multiple parameters and checking string digits.

def show_booking(destination, nights):
    if nights.isdigit():
       nn = int(nights)
    print(f"You're traveling to {destination}, and will stay for {nights} nigthts")

show_booking("Jeddah", 4)
show_booking("Doha", 5)



# LAB 6: Default Parameters & Docstrings

# Using default parameter values and adding a docstring to explain the function.

def getVAT(total, rate = 0.15):

   """This function will get the total with VAT added to it, and return the sum """

   subtotal = total + (total * rate)

   return subtotal

print(getVAT(155))
print(getVAT(155, 0.05))
print(getVAT.__doc__)
help(getVAT)

total = getVAT(680)
print(total)