class Student:
    def greeting(self):
        return "Hello"
    def show(self):
        return f"{self.name}"


s1 = Student()
print(type(Student))
print(isinstance(Student, type))