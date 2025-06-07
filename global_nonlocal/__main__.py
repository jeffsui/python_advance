"""
实例1:
外部定义的变量 a的值没有发生改变
实例2:
global 关键字修饰的变量 相当于外部变量引入内部 这样局部变量就可以改变外部定义的变量
案例3:
嵌套函数无法改变,上层局部变量的值
nonlocal 关键字修饰的变量 就可以解决这个问题

实例4:
globals(): 当前模块中字典形式存储所有全局变量和标识

实例5:
locals(): 当前局部作用域中的局部变量和标识
"""
# a = 10
# def func():
#     a = 20
#     print(a)
# func()
# print(a)

# a = 10
# def func():
#     global a
#     a = 20
#     print(a)
# func()
# print(a)

# def func():
#     a = 10
#     def func2():
#         nonlocal a
#         a = 20
#         print(a)
#     func2()
#     print(a)
# func()

# def func():
#     name = 'Jack'
#     age = 19
#     def func2():
#         nonlocal name
#         nonlocal age
#         name = 'Rose'
#         age = 20
#         print(name,age)
#     func2()
#     print(name,age)
# func()
# print(globals())

def func():
    name = 'Jack'
    age = 19
    def func2():
        address = "dalian"
        score = 99.5
        print(locals())
    func2()
    return locals()
print(func())
