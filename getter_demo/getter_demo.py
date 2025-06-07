from operator import itemgetter
"""
itemgetter() 方法
itemgetter() 方法用于返回一个函数，该函数可以获取一个字典对象中指定键对应的值。
语法：itemgetter(item1[, item2[, ...]])
如果参数 中的key 字段中不存在,则会报 key error
"""
wang = {'name': 'wang', 'age': 25, 'gender':'M'}
li = {'name': 'li', 'age': 24, 'gender': 'F'}
# name,age,gender = wang.values()
name,age,gender = itemgetter('name','age','gender')(wang)

print(name,age,gender)

name,age,gender = itemgetter('name','age','gender','height')(li)
print(name,age,gender)

numbers = [4, 1, 3, 4, 7]
first_last = itemgetter(0,-1)
f,l = first_last(numbers)
print(f,l)

