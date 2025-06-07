"""
attrgetter 方法
attrgetter 方法可以根据属性名获取对象属性的值。
语法：
attrgetter(attr1[, attr2[,...]])
参数：
attr1, attr2, …：属性名，可以是字符串或元组。
返回值：
一个函数，该函数可以获取对象属性的值。
"""
from operator import attrgetter

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age

        if gender == 'male':
            self.gender = 'Male'
        elif gender == 'female':
            self.gender = 'Female'
        else:
            self.gender = 'Unknown'

p1 = Person('Alice', 25, 'female')
p2 = Person('Bob', 30,'male')
p3 = Person('Charlie', 20, 'unknown')

# 获取对象属性的值
print(attrgetter('name')(p1))  # Alice
print(attrgetter('age')(p2))  # 30
print(attrgetter('gender')(p3))  # Unknown

get_name_age = attrgetter('name', 'age')
print(get_name_age(p1))  # ('Alice', 25)
print(get_name_age(p2))  # ('Bob', 30)