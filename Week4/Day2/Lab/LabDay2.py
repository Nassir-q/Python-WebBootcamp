
# 1. Class Variables vs Instance Variables

class Dog:
    _legs = 4

    def __init__(self, name):
        self.name = name

    def getlegs(self):
        return Dog._legs

    def setlegs(self, number):
        self._legs = number

    def talk(self, sound):
        return(f" {self.name} says : {sound} !")

myDog = Dog("Slogi")
myDog.setlegs(3)
print(myDog.name)
print(myDog.getlegs())
print(myDog._legs)

Dog._legs = 3
print(myDog._legs)
print(Dog._legs)



# 2. Pathlib: Inspecting Paths

from pathlib import Path

data_file = Path("data") / "students.txt"

print(data_file)
print(data_file.name)
print(data_file.suffix)



# 3. Pathlib: Creating Directories

data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

data_file = data_dir / "students.txt"

print(data_dir.is_dir())
print(data_file.exists())



# 4. File Handling: File Mode


# "r" read an existing file 
# "w"  write and replec content
# "a" append after exsiting content
# "x" create only when absent

with open("notes.txt", "a", encoding="utf-8") as file:
    file.write("New note\n")



# 5. File Handling: Reading and Context Managers

path = Path("notes.txt")

with path.open("r", encoding="utf-8") as file:
    content = file.read()

print(content)
print(file.closed)  # True



# 6. File Handling: read() vs read_text()

path = Path("notes.txt")

with path.open("r", encoding="utf-8") as file:
    text = file.read()

same_text = path.read_text(encoding="utf-8")

print(text == same_text)



# 7. File Handling: Iterating Line by Line

path = Path("student.txt")
with path.open("r", encoding="utf-8") as file:
    for line in file:
        name = line.strip()
        if name:
            print(name)



# 8. File Handling: Write Mode

path = Path("student.txt")

with path.open("w", encoding="utf-8") as file:
    count = file.write("Sara\nAli\n")

print(count)



# 9. File Handling: Appending Logs

path = Path("activity.log")

with path.open("a", encoding="utf-8") as file:
    file.write("Student enrolled : Sara\n")

print("Activity saved")



# 10. File Handling: write_text() with Encoding

names = ["Sara", "ناصر", "Ali"]
text = "\n".join(names) + "\n"

Path("student.txt").write_text(
    text,
    encoding="utf-8"
)