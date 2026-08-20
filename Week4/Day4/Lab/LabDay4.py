
# 1. LAB 5: Encapsulation and Properties (@property)

class Student:

    def __init__(self, name):
        self.name = name
        self.score = []
        self.__enrolled = True 

    def add_score(self, score):
        if score < 0 or score > 100:
            raise ValueError("score must be btween 0 and 100")
        self.score.append(score)

    # Getter 
    @property
    def enrolled(self):
        return self.__enrolled

    # Setter 
    @enrolled.setter
    def enrolled(self, status):
        self.__enrolled = status

    @property
    def average(self):
        if not self.score:
            return 0
        else:
            return sum(self.score) / len(self.score)

        
student = Student("khalifa")

student.enrolled = False  
print(student.enrolled)   

print(student.score)



# 2. LAB 6: Class Inheritance and super()

class Food:
    def __init__(self, name):
        self.name = name

    def showName(self):
        return self.name  


class Fruites(Food):
   
    def __init__(self, name, cal):
        super().__init__(name)
        self.cal = cal

    
    def stripName(self, newName):
      return newName

myfruites = Fruites("Apple", 200)
print(myfruites.showName())