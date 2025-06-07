from typing import TypeVar,Generic,Union

#定义类型变量T
T= TypeVar('T',int,str)


class MyGenericClass(Generic[T]):
    def __init__(self, value: T):
        self.value :T = value

    def get_value(self) -> T:
        return self.value

#实例化MyGenericClass
my_generic_class_int = MyGenericClass(10)

#调用get_value方法
print(my_generic_class_int.get_value()) #输出10

#实例化MyGenericClass
my_generic_class_str = MyGenericClass("hello")

#调用get_value方法
print(my_generic_class_str.get_value()) #输出hello