import time
# def timer(func):
#     """
#     Decorator that prints the time a function takes to execute
#     """
#     def wrapper(*args, **kwargs):
#         start = time.perf_counter()
#         result = func(*args, **kwargs)
#         end = time.perf_counter()
#         duration = end - start
#         print(f"{func.__name__} took {duration:0.4f} seconds to complete")
#         return result
#     return wrapper

# @timer
# def add(a, b):
#     return a + b
############################
# Timer 类装饰器
############################
# class Timer:
#     def __init__(self, func):
#         self.func = func

#     def __call__(self, *args, **kwargs):
#         start = time.perf_counter()
#         result = self.func(*args, **kwargs)
#         end = time.perf_counter()
#         duration = end - start
#         print(f"{self.func.__name__} took {duration:0.4f} seconds to complete")
#         return result
# @Timer
# def add(a, b):
#     return a + b

# print(add(2,3))
###################################
# 装饰器类 Timer
# 其实就是把类当作装饰器的参数使用,
# 和之前的函数装饰器很像
# 区别就是函数装饰器 被装饰的函数是参数
##################################
"""
class Timer:
    def __init__(self,prefix):
        self.prefix = prefix

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            end = time.perf_counter()
            duration = end - start
            print(f"{func.__name__}{self.prefix} took {duration:0.4f} seconds to complete")
            return result
        return wrapper

@Timer(prefix="Current time")
def add(a, b):
    return a+b

#等价于
# add = Timer(prefix="Current time")(add)
print(add(2,3))
"""
#################################
# 类的装饰器
# 下面给类添加了一个装饰器
# 主要功能将类属性 转换成字典形式
#################################

def add_str(cls):
    def __str__(self):
        return str(self.__dict__)
    cls.__str__ = __str__
    return cls

@add_str
class MyObject:
    def __init__(self, a, b):
        self.a = a
        self.b = b
# 等价于
# MyObject = add_str(MyObject)

o = MyObject(1,2)
print(o)
##################################
# 此处加上了我自定义的打印类的装饰器
#################################
from objprint import add_objprint
@add_objprint
class MyObject:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # def __str__(self):
    #     return str(self.__dict__)

o = MyObject(2,3)
print(o)