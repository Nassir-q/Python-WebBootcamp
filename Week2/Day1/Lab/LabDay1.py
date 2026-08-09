
# 1. Variables and Case Sensitivity

# In Python, variables are case-sensitive. 
# 'Student_name' and 'student_name' are two different variables.

Student_name = "Nasser"
student_name = "Abdullah"

print("First student:", Student_name)
print("Second student:", student_name)



# 2. Conditional Statements (If-Else)

# Using basic logic to check a condition. 
# If the score is 90 or above, it prints "Excellent", otherwise "Thank you".

score = 95

if score >= 90:
  print("Excellent")
else:
  print("Thank you")



# 3. Variables, Constants, and Multiple Assignment

# Constants are usually written in UPPERCASE.
# You can also assign multiple variables in a single line.

MAX_CLASS_SIZE = 25
MIN_CLASS_SIZE = 15


student_name, student_age, student_is_registered = "Nasser", 24, True



# 4. Checking Data Types

# Using type() to find out the data type of a variable.
# Using isinstance() to check if a variable matches a specific type.

print(type(student_name))          
print(type(student_age))           
print(type(student_is_registered)) 


print("Is age an integer?", isinstance(student_age, int))



# 5. User Input and Type Casting

# Taking input from the user. Since input() always returns a string,
# we must convert (cast) it to an integer using int() to do math.

age = input("Enter your age: ")

if isinstance(age, int):
  print("You are", age + 5, "AFTER 5 years")
else:
  
  print("You are", int(age) + 5, "after 5 years")



# 6. String Indexing and Length

# Strings are like lists of characters. We can access a specific letter 
# using its index. We use len() to make sure the index is not out of bounds.

teacher_name = "Faisel"
index = int(input("Select index (0 to 5): "))

if index < len(teacher_name):
  print("The character at index", index, "is:", teacher_name[index])
else:
  print("Out of range! The name only has", len(teacher_name), "characters.")

print("Type of length is:", type(len(teacher_name)))



# 7. Swapping Variables

# A quick Python trick to swap two values without needing a third temporary variable.

x = 0
y = 1

x, y = y, x 

print("After swapping: x =", x, ", y =", y)



# 8. Assignment: The Student Card

# This assignment demonstrates the use of f-strings (f"") to easily insert variables inside text.
# The triple quotes (""") allow the string to span multiple lines for a clean and structured layout.



course = "Web development bootcamp"
registered = True

print(f"""
-------------------------
      STUDENT CARD       
-------------------------
Welcome {Student_name} to {course}!
You are {student_age} years old.
Registration status is {registered}.
Thank you for joining us!
""")