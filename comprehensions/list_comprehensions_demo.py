"""
推导式 comprehensions
1. List comprehensions
是 Python 中的一种简洁的语法，
用于从现有的列表、元组或其他可迭代对象中创建新的列表。
它们通常比使用传统的 for 循环更简洁、更易读。
2. 语法
[expression for item in iterable if condition]
"""
# 示例：使用列表推导式创建一个包含 0 到 9 的平方数的列表
squares = [x ** 2 for x in range(10)]
print("Squares:", squares)
# 示例：使用列表推导式过滤出偶数
evens = [x for x in range(10) if x % 2 == 0]
print("Evens:", evens)
# 示例：使用列表推导式将字符串转换为大写
words = ["hello", "world", "python"]
uppercase_words = [word.upper() for word in words]
print("Uppercase Words:", uppercase_words)
# 示例：使用列表推导式创建一个包含元组的列表
tuples = [(x, x ** 2) for x in range(5)]
print("Tuples:", tuples)