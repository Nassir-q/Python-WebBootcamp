
# 1. CSV Module: Writing Data

import csv


with open("students.csv", "w",
          encoding="utf-8", newline="") as file:
    
    writer = csv.writer(file)
    writer.writerow(["name", "course"])
    writer.writerow(["Sara", "Python"])
    writer.writerow(["Ali", "Django"])



# 2. JSON Module: Dumping and Loading Data


import json 

students = [
    {"name" : "Sara", "score" : 92},
    {"name" : "Ali", "score" : 85}
]

with open("students.json", "w" , encoding="utf-8") as file:
    json.dump(students, file, indent=2) # يقرا الملف 

with open("students.json", "r", encoding="utf-8") as file:
    loaded = json.load(file) # يجهز الملف 

print(loaded[0]["name"])



# 3. Exception Handling: Basic Try-Except


try:
    score = int(input("score : "))
except ValueError as e:  # يحدد نوع الايرور
    print("Enter a whole number")
    print(e)

print("Program continues")



# 4. Exception Handling: Multiple Exceptions

from pathlib import Path


try:
    text = Path("students.txt").read_text(
        encoding="utf-8"
    )

except FileNotFoundError:
    print("Student file not found")
except PermissionError:
    print("Student file cannot be read")



# 5. Exception Handling: Else and Finally Clauses


path = Path("students.txt")

try:
    text = path.read_text(encoding="utf-8")
except OSError as error:
    print("Load filed : ", error)
else:
    print(text)
finally:
    print("Load attmpt finished")



# 6. Exception Handling: Raising Exceptions


def validate_score(score):
    if not 0 <= score <=100:
        raise ValueError("Score must be 0 to 100")
    return score 

try:
    # score = validate_score(120)
    score = input("Enter your number : " )
except ValueError as error:
    print(error)



# 7. Custom Exceptions

class StudentNotFoundError(Exception):
    pass

def find_student(name, students):
    for student in students:
        if student["name"] == name:
            return student
    raise StudentNotFoundError(name)


students = [{"name" : "Sara"}]


try:
    print(find_student("Ali", students))

except StudentNotFoundError as error:
    print("Missing student:", error)



# 8. LAB 1: Class Attributes and State Management

class Ticket:
   def __init__(self, name, status = "Open"):

        self.name = name
        self.stutus = status

   def newStatus(self, status):
      self.stutus = status

myTicket1 = Ticket("1000", "in progress")
myTicket2 = Ticket("1001","Pending")

print(myTicket1.stutus)
print(f"Ticked  ID : {myTicket2.name} is {myTicket2.stutus}")



# 9. LAB 2: Instance Methods and Return Values

class Greeter:
    def __init__(self, message):
        self.message = message

    def greet(self, user):
        self.user = user

        return (f"Hello {user}, {self.message}")\

mygreet = Greeter("Welcome to tuwiq")


mymsg = mygreet.greet("Salem")

print(mymsg)



# 10. LAB 3: Lists of Objects and Iteration

class welcome:
    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"Welcome {self.name}")
        
students = [
    welcome("Sara"),
    welcome("Mohammed"),
    welcome("Khadihah"),
    welcome("Omer")
]

for student in students:
   
    student.welcome()



# 11. LAB 4: Pathlib Directory Creation and File Writing

from pathlib import Path

path = Path("home")/"students"/ "students.txt"

path.parent.mkdir(parents= True, exist_ok=True)

print(path.is_dir())
print(path.suffix)
print(path.name)
print(path.is_file())

path.write_text("Welcome to class", encoding="utf-8")