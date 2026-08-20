
# 1. Class Definition and Type

class Student:
    pass
print(Student)
print(type(Student))



# 2. Object Instantiation and Identity

class Student:
    pass
student_one = Student()
student_two = Student()
print(student_one)
print(student_one is student_two)



# 3. The __init__ Method and Instance Attributes

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

student = Student("Sara", 92)

print(student.name)
print(student.score)



# 4. Instance Methods

class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I am {self.name}")

student = Student("Omar")
student.introduce()



# 5. Modifying Attributes and Checking Instances

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

sara = Student("Sara", 92)
omar = Student("Omer", 81)

sara.score = 95
print(sara.score)
print(omar.score)

print(isinstance(omar, Student))



# 6. Class Variables (Class Attributes)

class Student:
    academy = "Tuwaiq Acadmy"
    def __init__(self, name):
        self.name = name


sara = Student("Sara")

print(Student.academy)
print(sara.academy)



# 7. Method for Displaying Data

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def display_resulte(self):
        print(self.name, self.score)

student = Student("Lina", 88)
student.display_resulte()



# 8. Updating Object State (Incrementing)

class Counter:
    def __init__(self):
        self.value = 0
    def increment(self):
        self.value += 1

counter = Counter()
counter.increment()
counter.increment()
counter.increment()

print(counter.value)



# 9. Returning Values from Methods

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height 
    def area(self):
        return self.width * self.height

rectangle = Rectangle(5, 3)
print(rectangle.area())
 


# 10. Method Logic and Validation

class BankAccount:
    def __init__(self, balance = 0):
        self.balance = balance
    def withdraw(self, amount):
        if amount <=0 or amount > self.balance:
            return False

        self.balance -= amount
        return True

account = BankAccount(500)
print(account.withdraw(200))
print(account.balance)



# 11. The __str__ Magic Method

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return f"{self.name}: {self.score}"

student = Student("Sara", 95)
print(student)



# 12. Independent Object States

class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

first = Counter()
second = Counter()

first.increment()

print(first.value)
print(second.value)



# 13. Lists of Objects and Iteration

class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}"

students = [
    Student("Sara"),
    Student("Omar"),
    Student("Lina")
]
print(students[0].greet())

for student in students:
    print(student.greet())



# 14. Type Checking (type vs isinstance)

class Student:
    pass

student = Student()
print(type(student))
print(type(student)is Student)
print(isinstance(student, Student))



# 15. Encapsulation (Protected Attributes)

class Student:
    def __init__(self, name, score):
        self.name = name
        self._score = score
    def updet_score(self, newScore):
        self._score = newScore

student = Student("Sara", 96)

print(student.name)
print(student._score)
student.updet_score = 90
print(student.updet_score)



# 16. Working with Lists as Attributes

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def average(self):
        return sum(self.score) / len(self.score)

    def add_score(self, score):
        if 0<= score <=100:
            self.score.append(score)

student = Student("Sara", [80 , 90])
student.add_score(100)
print(student.name, student.average())