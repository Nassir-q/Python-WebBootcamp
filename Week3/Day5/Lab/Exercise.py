# Crate a list of student dictionaries with names and score lists
# Use a list comperehension to calculate each student's average
# Filter the report to keep only students whose average is at least 60
# Build a dictionary index that maps each student name to he report record
# Create an independent backup with deepcopy, then prove nested chages stay separate


from copy import deepcopy
students = [
    {"name" : "Nasser", "Score" : [88,91,95]},
    {"name" : "Abdullah", "Score" : [85,60,87]},
    {"name" : "Omar", "Score" :[30, 33, 44]}
]


student_avg = [
    {
     "name" : student["name"],
     "Score" : student["Score"],
    "average": round(sum (student["Score"]) / len(student["Score"]),2)
    
    }
    
    for student in students

]


paas_student = [
    student
    for student in student_avg
    if student["average"] >= 60
]
print("\n the student pass is :")
print(paas_student)

clone = deepcopy(students)
clone[0]["Score"][2] = 100

print("\n after changes the score in copy")
print(clone)
print("\n before changes the score original")
print(students)