
# Introduction: Basics of For Loops and Range

# Print numbers from 0 to 4
for number in range(5):
    print(number)

print("----------------------------")

# Print numbers from 1 to 5

for n in range(1, 6):
    print(n)

print("----------------------------")

# Print numbers from 0 to 10 with a step of 2 (Even numbers)

for n in range(0, 12, 2):
    print(n)

print("----------------------------")

# Countdown from 5 to 1 using a negative step (-1)

for n in range(5, 0, -1):
    print(n)

print("----------------------------")

# Calculate the sum of numbers from 1 to 5

total = 0
for number in range(1, 6):
    total += number
print(f"Total sum is: {total}")

print("-----------------------------")



# Introduction: While Loops and User Input

# Basic while loop counting from 1 to 5

count = 1
while count <= 5:
    print("While count:", count)
    count += 1

print("------------------------------")

# Validating user input using a while loop

age = input("Enter your age: ")
while not age.isdigit():
    print("Invalid age.")
    age = input("Enter your age: ")

age = int(age)
print(f"Age accepted: {age}")

print("-------------------------")

# Using 'break' to exit an infinite while loop

while True:
    command = input("Enter command (type 'exit' to stop): ")
    if command == "exit":
        break
    print(f"You entered: {command}")

print("-------------------------")

# Using 'continue' to skip a specific iteration

for number in range(1, 11):
    if number == 5:
        continue # Skips printing the number 5
    print(f"Number: {number}")

print("-----------------------")

# Simple Interactive Menu

while True:
    print("1. Say Hello")
    print("2. Check Number")
    print("3. Exit")
    choice = input("Choose: ")

    if choice == "1":
        print("Hello!")
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Try again")

print("--------------------------")

# Checking even and odd numbers up to a maximum limit

total_count = 0
max_num = int(input("Enter the max number: "))

for n in range(1, max_num):
    total_count += 1
    print(f"count is {total_count}")
    if n % 2 == 0:
        print(n, "is an even number")
    else:
        print(n, "is an odd number")

print(f"The total numbers checked: {total_count}")
print("----------------------------------")



# LAB 1: Loop with Attempts

for attempts in range(3):
    print(f"Attempt index: {attempts}")
    print(f"Attempts count: {attempts + 1}")



# LAB 2: Even Numbers using Range

for num in range(2, 11, 2):
    print("Lab 2 Even number:", num)



# LAB 3: Countdown

for secondsToLaunch in range(10, 0, -1):
    print(f"T- :  {secondsToLaunch}")



# LAB 4: Iterating over a String

course = "python"
for letter in course:
    print("Letter:", letter)


# LAB 5: Iterating over a List

students = ["Shahad", "Khadija", "Yamam", "Abdullah"]
for student in students:
    print(f"Processing student: {student}")



# LAB 6: Even or Odd with Modulus

for number in range(1, 11):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")



# LAB 7: Counting specific items in a List

numbers = [4, 7, 10, 13, 16, 21, 22]
even_counter = 0

for num in numbers:
    if num % 2 == 0:
        even_counter += 1

print(f"Total even numbers in the list is: {even_counter}")



# LAB 8: Calculating Total and VAT

prices = [25, 30, 55, 115]
total_price = 0

for price in prices:
    total_price += price

# Fixed the missing closing brace '}' in the f-string format

print(f"Your total is {total_price}, VAT: {total_price * 0.15:.2f}")



# LAB 9: While Loop Counter

count = 0
while count < 5:
    count += 1
    print(f"count......   {count}")
print("Loop completed")



# LAB 10: Input Validation

age_text = input("Please enter your age: ").strip()

while not age_text.isdigit():
    age_text = input("Invalid input. Please enter your age (numbers only): ").strip()

age = int(age_text)
print(f"You are: {age}")



# LAB 11: Password Validation

password = input("Please Enter your password: ")

while password != "python123":
    password = input("Incorrect Password, try again: ")

print("Access Granted!")



# LAB 12: Pass, Continue, and Break Controls

# 1. Using pass (Does nothing, just avoids syntax error)

for score in [80, 55, 45, 90]:
    if score < 50:
        pass
    print(f"Using pass, current score: {score}")

print("---")

# 2. Using continue (Skips the rest of the loop for this iteration)

for scored in [80, 55, 45, 90]:
    if scored < 50:
        continue
    print(f"Using continue, passed score: {scored}")

print("---")

# 3. Using break (Stops the loop entirely)

for badscore in [80, 55, 45, 90]:
    if badscore < 50:
        break
    print(f"Using break, we saw: {badscore}")



# LAB 13: Nested Loops

for row in range(1, 4):
    for column in range(1, 4):
        print(f"Row: {row}, Column: {column} | {row} X {column} = {row * column}")