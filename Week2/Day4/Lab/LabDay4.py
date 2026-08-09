
# Main Assignment: Student Data Validation

# Requirements:
# 1. Ask for a student's name, score, and selected course.
# 2. Validate the name is not empty.
# 3. Validate the score is numeric and between 0 and 100.
# 4. Assign a grade using if / elif / else.
# 5. Confirm the course using the membership operator (in).

name = input("Enter your name: ").strip()
score_input = input("Enter your score: ").strip()
selected_course = input("Enter the Course: ").title()

courses = ["Python", "Java", "HTML"]

# Validate Course

if selected_course not in courses:
    print("Course doesn't exist!")

# Validate Name

if not name:
    print("Please enter your name.")
else:
    print(f"Welcome, {name}!")

# Validate Score
# Using isdigit() is safer to check if the user entered numbers only

if not score_input.isdigit():
    print("Please enter a valid numeric score.")
else: 
    score = int(score_input)
    if score < 0 or score > 100:
        print("The score must be between 0 and 100.")
    elif score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    else:
        print("Grade: Failed")



# Lab 1: Basic If Statement
# Executing code only if a specific condition is true.

age = 20

if age >= 18:
    print("Welcome")

print("Code completed")



# Lab 2: If / Else Statement
# Choosing between two different paths based on a condition.

temperature = 31

if temperature >= 35:
    print("It's hot outside")
else:
    print("Cool")



# Lab 3: If / Elif / Else Statement
# Checking multiple conditions in order. 
# Once a true condition is found, the rest are skipped.

score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("You need to improve")



# Lab 4: Logical Operators (and, or, not)
# Combining multiple conditions together.

is_active = True
is_verified = True
role = "Editor"
is_blocked = False

# 'and' requires BOTH conditions to be True

if is_active and is_verified:
    print("Account is ready")

# 'or' requires AT LEAST ONE condition to be True

if role == "Admin" or role == "Editor":
    print("User can edit")

# 'not' reverses the boolean value (False becomes True)

if not is_blocked:
    print("User is not blocked")
else:
    print("User is blocked")



# Lab 5: Nested If Statements
# Placing an if statement inside another if statement.

account_active = True
has_permission = True

if account_active:
    if has_permission:
        print("Access granted")
    else:
        print("Access denied")
else:
    print("Account is not active")


# Lab 6: Truthiness in Python
# In Python, empty strings, empty lists, and 0 are considered False.
# Everything else is generally considered True.

name = "Faisal"
cart = []
balance = 990

if name: # True because the string is not empty
    print("Name has a value")

if not cart: # True because the list is empty (False reversed by 'not')
    print("Your cart is empty")

print("Is balance True or False?", bool(balance))



# Lab 7: String Validation (isalpha)
# Checking if a string only contains letters.

first_name = input("Enter your first name: ").strip()

if not first_name:
    print("Please enter a name")
elif not first_name.replace(" ", "").isalpha():
    print("Name must contain letters only")
else:
    print(f"Valid name: {first_name}")



# Lab 8: Numeric Validation (isdigit) and Math
# Ensuring input is a number before doing mathematical operations.

age_text = input("Enter your age: ").strip()

if age_text.isdigit():
    age = int(age_text)
    print(f"You will be {age + 5} in 5 years")
else:
    print("Please enter a valid number")



# Lab 9: Range Validation
# Checking if a number falls within a specific range cleanly (0 <= score <= 100).

score_text = input("Enter a score between 0 and 100: ").strip()

if score_text.isdigit():
    score = int(score_text)
    if 0 <= score <= 100:
        print("Valid score")
    else:
        print("Invalid score")
else:
    print("Please enter a valid number")



# Lab 10: Membership Operator (in) & Ternary Operator

memberships = ["Admin", "Editor", "Viewer"]
current_membership = input("Enter your membership: ").strip().title()

# Using 'in' to check if the value exists inside the list

if current_membership in memberships:
    print("You are allowed to view the content")
else:
    print("Please contact the admin team")

# Ternary operator: A quick, one-line if/else statement

user_age = 20
status = "Adult" if user_age >= 18 else "Minor"
print("User status:", status)



# Lab 11: Match / Case Statement
# Python's equivalent to the 'switch' statement in other languages.
# It's a clean way to check a variable against multiple specific values.

command = input("Enter a command (start, stop, status): ").strip().lower()

match command:
    case "start":
        print("Starting system...")
    case "stop":
        print("Stopping system...")
    case "status":
        print("System is running")
    case _: # The underscore (_) acts as the 'default' or 'else' case
        print("Unknown command")