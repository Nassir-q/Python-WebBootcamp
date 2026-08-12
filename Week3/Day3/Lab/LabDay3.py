import math


# Practice: Functions & Loops

def student_name(name):
    for char in student_name:
        print(char)
student_name("Abdullah")



# Practice: Lists Basics

student = ["Sara", "Omar", "Lina"]
print(student)
print(student[0])
print(type(student))


color = ["red", "green", "blue"]
print(color[0])
print(color[1])
print(color[-1])



# Practice: List Slicing

numbers =[10, 20, 30, 40, 50]
print(numbers[1:4])
print(numbers[:3])
print(numbers[::2])
print(numbers[::-1])


# Practice: List Methods

tasks =["Plan","Code"]
tasks[0] = "design"
tasks.append("test")
tasks.insert(1, "review")
print(tasks)


score = [88, 72, 95, 81]
score.remove(72)
last = score.pop()
score.sort()

print(score)
print(last)



# Practice: Looping over Lists & Enumerate

students = ["Sara", "Omar", "Lina"]

for student in students:
    print(student)


for index, student in enumerate(students):
    print(index, student)



# Practice: 2D Lists (Matrix)

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print(matrix[0])
print(matrix[1][2])



# Practice: Tuples (Immutable)

location = (24.7136, 46.6753)

print(location[0])
print(location[-1])

# location[0] = 25 # TypeError


student = ("Sara", 22, "Python", True, "win")

name, age, course, *other = student  # * ==> Catch all

print(name)
print(age)
print(course)



# Practice: Sets & Set Operations

skills = {"Pyhton", "Git", "Pyhton"}
skills.add("Django")

print(skills)
print("Git" in skills)
print(len(skills))


backend = {"Python", "Django", "SQL"}
frontend = {"HTML", "CSS", "JavaScript", "SQL"}

print(backend | frontend) # Union
print(backend & frontend) # Intersection
print(backend - frontend) # Diffrence



# Practice: Dictionaries

student = {
    "Name": "Nasser",
    "Age": 22,
    "course": "Pyhton" 
}

print(student["Name"])


student = {"name": "Nasser", "Score": 90}

student["Score"] = 95
student["grade"] = "A"


email = student.get("email", "Not det")
grade = student.pop("grade")

print(student)



# Practice: Looping over Dictionaries

student = {"name": "Nasser", "Score": 95}

for key in student:
    print(key)


for key, value in student.items():
    print(key, value)


for value in student.values():
    print(value)



# Practice: Validations & List of Dictionaries

name = ["Nasser", "Abdullah"]
skills = ["Python", "Git"]
student = {"name": "Nasser", "Score": 95}

print(len(name))
print("Git"in skills)
print("name" in student.keys())

students = [
  {"name": "Nasser", "Score": 95},
  {"name": "Abdullah", "Score": 90}
]

for student in students:
    print(student["name"], student["Score"])



# Main Assignment (Exercise)

# Store several student dictionaris inside one list 
# Give each student a name, tuple of scores, and set of skills
# Calculate each student's average by looping through the score 
# Add one new skill and prevent duplicates automaticlly
# Display every name, average, and unique skill set clearly

students_list = [
    {"name": "Nasser", "Scores": (95, 100, 90), "Skills": {"Python", "Git", "Java"}},
    {"name": "Abdullah", "Scores": (90, 88, 99), "Skills": {"Git", "PHP", "HTML"}}
]

for student in students_list:
    
    x = sum(student["Scores"])
    y = len(student["Scores"])
    average = x / y
    
    student["Skills"].add("CSS")
    
    print(f"Name: {student['name']}")
    print(f"Average: {average:.2f}")
    print(f"Skills: {student['Skills']}")



# LAB 1 

students = ["Nasser", "Abdullah", "Taif", "Mashael"]

for student in students:
    print(student)

iterable = enumerate(student)
print(next(iterable))



# LAB 2

set_col = {"Abdullah", "Nasser","Dalal", "Sara"}
tuple_col = (11, 22, 33, 44, 55, 66)
dict_col = {"name" : "Abdullah", "age" : 22, "has_car": True}
list_col = ["ABC", 333, (33, 33)]

for c in dict_col.values():
    print(type(c))

print(set_col)
print(tuple_col)
print(dict_col)
print(list_col)
print(type(set_col))
print(type(tuple_col))
print(type(dict_col))
print(type(list_col))


# LAB 3

cars = ["GMC", "BMW", "Geely", "Porsche", "Merc", "Chevy"]

print(cars[3])
print(cars[-1])
print(cars[-1::-1])



# LAB 4

tasks = ["Read email", "Open ticket"]
tasks[0] = "Login"
tasks.append("Get Coffee")
tasks.insert(0, "Get breakfast")
tasks.pop(3)
print(tasks)


# LAB 5

numbers = [11, 22, 33, 44, 55, 66]

print(sum(numbers))
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(math.sqrt(max(numbers)))
print(math.__doc__)
print(numbers)
print(numbers.pop(2))
print(sorted(numbers, reverse= True))



# LAB 6

skills ={"Python", "Django", "Flask", "FastAPI", "Java"}
skills.add("CSS")
skills.add("HTML")
skills.discard("CSS")
skills.remove("Java")
print(skills)