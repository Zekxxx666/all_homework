
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    grade: int


def info(student: Student):
    print(f"{student.name}, {student.age} лет, {student.grade} класс")

def up_grade(student: Student):
    student.grade += 1

def adult(student: Student):
    if student.age > 18:
        return True
    else:
        return False
    
def comparison(student1: Student, student2: Student):
    if student1.age > student2.age:
        print(f"старше {student1.name} с возрастом {student1.age}")
    elif student1.age < student2.age:
        print(f"старше {student2.name} с возрастом {student2.age}")
    else:
        print("ученики ровесники")

def classmates(student1: Student, student2: Student):
    if student1.grade == student2.grade:
        return True
    
def edit_age(student: Student, up_age):
    student.age += up_age

student1 = Student("Иван", 14, 3)
student2 = Student("Мария", 13, 7)






