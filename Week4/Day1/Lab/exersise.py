# Give each Student a name and an initially empty score list
# Add an add_score method that accepts values only form 0 to 100
# Add an average method that returns zero when no scores exit
# Store several Student objects inside one Course object
# Display every student's name, score, and calculated average clearly



class Students:
    
    def __init__(self, name, score=None):
        self.name = name
        self.score = [] if score is None else score

    def add_score(self, score):
        if 0 <= score <= 100:
           self.score.append(score)

    def average(self):
        if not self.score:
            return 0
        return sum(self.score) / len(self.score)

class Course:
    
    def __init__(self, course_name, students=None):
        self.course_name = course_name
        self.students = [] if students is None else students

    def add_students(self, student):
        if isinstance(student, Students):
            self.students.append(student)

    def display(self):
        print(f"--- Course: {self.course_name} ---")
        for student in self.students:
           
            print(f"Name : {student.name}\nScore : {student.score}\nAverage : {student.average():.2f}\n")




course = Course("Python")


course.add_students(Students("Nasser", [90, 70, 80]))
course.add_students(Students("Abdullah", [90, 90, 90]))


student = Students("Ali")
student.add_score(85)
student.add_score(95)
course.add_students(student)

course.display()