# Cearte data/student.json with pathlib and a prepared directory
# Save a list of student dicttionaries with json.dump()
# Load the file and validate evry name and score field
# Handele fileNotFoundError and JSONDecodeError separtary
# Raise InvalidStudentError when a loaded record is invalid



from pathlib import Path
import json



class InvalidStudentError(Exception):
    pass

Students = [
     {"name" : "Nasser", "score" : 92},
    {"name" : "Abdullah", "score" : 99},
    {"name" : "Ali", "score" : 88}
]

with open("Students.json", "w", encoding="utf-8") as file:
    json.dump(Students, file, indent=2 )

try:
    with open("Students.json", "r", encoding="utf-8") as file:
     loaded_file = json.load(file)
    for student in Students:
       if "name" not in student:
          raise InvalidStudentError("Student is Missing name")
       
       if "score" not in student:
          raise InvalidStudentError("Student is Missnig score")
       
except FileNotFoundError:
   print("Student file not found")

except json.JSONDecodeError:
   print("Student file contains invaled json")

except InvalidStudentError as error:
   print("Inavlid Student", error)

else:
   print("Loaded Successfully")
   for student in Students:
      print(student["name"], student["score"])