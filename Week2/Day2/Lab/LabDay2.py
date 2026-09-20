# class Dog:
#     _legs = 4

#     def __init__(self, name):
#         self.name = name


#     def getlegs(self):
#         return self._legs


#     def setlegs(self, number):
#         self.number = number


#     def talk(self, sound):
#         return(f" {self.name} says : {sound} !")

# myDog = Dog("Peter")
# print(myDog.name)
# print(myDog._legs)
# Dog._legs = 3
# print(myDog._legs)
# print(Dog._legs)





from pathlib import Path

# data_file = Path("data") / "students.txt"

# print(data_file)
# print(data_file.name)
# print(data_file.suffix)


data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

data_file = data_file = data_dir / "students.txt"

print(data_dir.is_dir())
print(data_file.exists())