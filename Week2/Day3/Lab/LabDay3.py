
# Introduction: Object Identity and Equality

# Demonstrating the difference between checking if values are equal (==)
# and checking if variables point to the exact same object in memory (is).

first = [1, 2]
second = [1, 2]
alis = first

print("Is first equal to second (values)?", first == second) 
print("Is first exactly second (memory)?", first is second)  
print("Is first exactly alis (memory)?", first is alis)      



# Introduction: Splitting and Joining Strings

csv_line = "Ali, Nasser, Yazan"

# Split the string by comma and space to create a list

name = csv_line.split(", ")

# Join the list back together using a pipe symbol

message = "    |    ".join(name)

print("Joined Message:", message)
print("Type of csv_line:", type(csv_line))



# Introduction: Input, Slicing, and Type Casting

sentence = input("Enter first Sentence : ")
number1 = input("Enter first number : ")
number2 = input("Enter second number : ")

# Slicing the sentence string and trying to cast parts of it to integer

print("First character:", sentence[:1])
print("Characters from index 2 to end:", sentence[2:])

# Converting string inputs to integers to perform mathematical addition

total = int(number1) + int(number2) 
print("Total Sum:", total)



# LAB 1: Order of Operations (PEMDAS)
# Multiplication and division are calculated before addition and subtraction.

result = 10 + 5 * 2 - 4/2
print("Lab 1 Result:", result)



# LAB 2: Floor Division and Modulus
# Using // to find how many full boxes we have, and % to find the remainder.

total_items = 17
box_capacity = 5

full_box = total_items // box_capacity
remaining_items = total_items % box_capacity

print(f"You can fill up to: {full_box} boxes")
print(f"And you will have {remaining_items} remaining items")



# LAB 3: Exponentiation and Grouping
# Using ** for powers, and () to change the order of calculation.

base_calc = 2 + 3 * 2 ** 2
gcalc = (2+3) * 2 ** 2
print("Base calc:", base_calc, "Grouped calc:", gcalc)



# LAB 4: Logical Operators and Inline If

user_age = 25
has_permission = True

# Standard boolean logic

is_eligible = (user_age >= 18 and has_permission)

# Inline ternary operator

IS_eligible = True if (user_age >= 18 or has_permission) else False 
print(f"Eligibility status : {is_eligible}")



# LAB 5: Assignment Operators
# Modifying variable values directly using += and *=
score = 10
score += 5  
score *= 5  
print(f"Your score is : {score}")


# LAB 6: The 'in' Operator
# Checking if a value exists inside a list.

membership = ["Admin", "Editor", "Viewer"]
current_membership = "Editor"

if current_membership in membership and "Admin" in membership:
    print("Welcome")
else:
    print("Go to sign up page")



# LAB 7: Finding Substrings

# Finding the index of the first occurrence of a specific letter.
sentence1 = "Python Web Developer"
new_sentence = sentence1.find("e")
print("Index of 'e':", new_sentence)



# LAB 8: Indexing, Slicing, and Reversing

message = "python programming"
first_char = message[0]
last_char = message[-1]
print(f"First char is: {first_char} and Last char is: {last_char}")

# Extracting the first 6 characters
sliced_message = message[:6]
# Reversing the entire string
reversed_message = message[::-1]

print(f"""
Your message was: {message}
First 6 chars: {sliced_message}
Reversed message: {reversed_message}
""")



# LAB 9: String Methods (Strip, Lower, Title)

# Cleaning white spaces and formatting text.
my_email = "     nasser.y.qasem@example.com              "
cleaned_email = my_email.strip().lower()

course_message = "python programming"
titeld_message = course_message.title()

print(f"Your email is {cleaned_email}, and your course is {titeld_message}")



# LAB 10: Split and Join Practical Example

csv_text = "apple, orange, bnana, cherry, dates"

splitted_text = csv_text.split(", ")
joined_text = " |  ".join(splitted_text)

print(f"""Your list is: {csv_text}
Splitted like this: {splitted_text}
Rejoined like this: {joined_text}
""")



# LAB 11: Immutability and Object ID

# Strings are immutable (cannot be changed). We handle the error using try/except.
name = "Nasser"
try:
    name[0] = "A"
except TypeError as e:
    print("Error caught:", e)

x = 5
y = 5
if x is y:
    print("They are the same object")
else:
    print("They are not the same object")

print("Memory ID of x:", id(x))
print("Memory ID of y:", id(y))



# LAB 12: Replacing Strings, Swapping, and NoneType

# 1. String Replace
Message = "python programming"
new_message = Message.replace("programming", "Developer")
print(new_message)


x = 6
y = 9
x, y = y, x
print("Swapped values: x =", x, ", y =", y)


is_online = None

if is_online:
    print("True")
elif is_online is False:
    print("False")
else:
    print("Status is None")
print("is_online value:", is_online)