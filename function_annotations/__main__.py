"""
function-annotations
根据type hint 编写的函数
可以通过函数.__annotations__查看注解

下面是具体示例:
可以看到__annotations__返回一个字典, key是参数名, value是参数类型
return是返回值类型

1. ham, eggs, spam 是参数

2. str 是参数类型

3. str 是返回值类型

但是如果你写函数的时候, 不写参数类型, 也不会报错

因为python是动态语言, 类型检查是在运行时进行的

文档地址:
https://docs.python.org/zh-cn/3.13/tutorial/controlflow.html#function-annotations
"""


###############
# 使用type hint
# 可以查看__annotations__的具体内容
###############
def my_function(ham: str, eggs: str = "eggs", spam: str = "spam") -> str:
    print("Annotations", my_function.__annotations__)
    print("Arguments", ham, eggs, spam)
    return ham + " and " + eggs + " and " + spam


my_function("ham")

################
# 没有使用type hint
# 但是仍然可以查看__annotations__
###############


def add(a, b):
    print(add.__annotations__)
    return a + b


add(1, 2)
