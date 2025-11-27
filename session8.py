class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"{self.name} is saying hello and welcome")



class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def give_exam(self):
        print(f"{self.name} is giving exam")







class Teacher(Person):
    def __init__(self, name, age, level):
        super().__init__(name, age)
        self.level = level

    def exam(self):
        print(f"{self.name} is takimg exam")



s1 = Student("sara", 12, 19)
s1.greet()
s1.give_exam()
t1 = Teacher("ali", 42, 3)
t1.greet()
t1.exam()

p1 = Person("artin", 32)
p1.greet()