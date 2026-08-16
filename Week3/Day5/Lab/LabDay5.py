
# Practice: Generator Expressions & Sum

numbers = range(1_000_000)

total = sum(       # => Expression

    number ** 2
    for number in numbers 
)

print(total)



# Practice: Object Identity & Mutability

items = ["Python", "Git"]
items .append("Django")


name = "  Sara"
name = name.title().strip()


print(id(items))
print(id(name))



# Practice: Aliasing (Reference Assignment)

original = ["Python", "Git"]
alias = original

alias.append("Django")

print(original)
print(alias)
print(original is alias)



# Practice: Shallow Copy

original = ["Python", "Git"]
clone = original.copy()

clone.append("Django")
print(original)
print(clone)
print(original is clone)

print(id(original))
print(id(clone))
print(id(original is clone))



# Practice: Shallow Copy on Nested Lists

original = [["Sara", 90], ["Omar", 85]]
clone = original.copy()

clone[0][1] = 95

print(original)
print(clone)
print(original[0] is clone[0])



# Practice: Deep Copy

from copy import deepcopy

original = [["Sara", 90], ["Omar", 85]]

clone = deepcopy(original)

clone[0][1] = 95
original[0][1] = 100

print(original)
print(clone)
print(original[0] is clone[0])



# Practice: Time Complexity (List vs Set)

names = ["Sara", "Omar", "Lina"]

# #   Searches items one by one : 0(n)

print("Lina" in names)

name_set = set(names)

# #   Average membership lookup: 0(1)

print("Lina" in name_set)



# Practice: Dictionary Lookups

students = [
    {"id" : 101, "name" : "Sara"},
    {"id" : 102, "name" : "Omar"}
]

student_by_id = {
    student["id"]: student
    for student in students
}


print(student_by_id[102]["name"])



# LAB 1 

numbers = [1, 2, 3, 4, 5]
sqaure_number = []


for number in numbers:
    sqaure_number.append(number ** 2)

print(sqaure_number)
comp_numbers = [
    number ** 2
    for number in numbers
]
print(comp_numbers)



# LAB 2

prices = [10, 25, 40]

prices_with_vat = [
    round(price * 1.15, 2)
    for price in prices
]

print(prices_with_vat)



# LAB 3

names = ["SaRa", "ArEej ","Mashael", "nasser"]

lower = [
    name.lower()
    for name in names

]

upper = [
    name.upper()
    for name in names
]

titled = [
    name.title()
    for name in names
]
print(lower, upper,titled)



# LAB 4

c_temp =[20,33,15,1]

f_temp = [
    (temp * 1.8 + 32)
    for temp in c_temp
    if temp > 0
]
print(f_temp)



# LAB 5

nested_list = [[1,2],[3,4],[5,6]]

flattened_list = []

for row in nested_list:
    for column in row:
        flattened_list.append(column)

print(flattened_list)

comp_flattened_list = [
    column
    for row in nested_list
    for clumn in row
]
print(comp_flattened_list)



# LAB 6

scores = [45, 55, 65, 75, 85, 95]

passing_score = [
    "Pass" if score >= 60 else "Failld"
    for score in scores
]
print(passing_score)



# LAB 7

skills = ["PYTHON", "Git", "python", "Javascript", "SQL", "git"]

skills_set = {
    skill.lower().title()
    for skill in skills

}
print(skills_set)



# LAB 8

list_name = ["Sara", "Dalal", "Nouf", "Taif"]
counted_chars = [
    {
        "name" : name, "count" : len(name)
    }
    for name in list_name
]
print(counted_chars)



# LAB 9

new_names = ["Mada", "Khadija", "Yamam", "Mashael"]

upp = (
    name.upper()
    for name in new_names
)
print(next(upp))
print(next(upp))
print("-"*5)
print(list(upp))

for x in upp:
    print(x)