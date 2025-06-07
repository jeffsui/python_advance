class A:
    @staticmethod
    def f(x):
        print(x)

A.f(1) #此时可以直接通过A(class)直接调用 staticmethod修饰的函数
A().f(1)
print(A.f) #A.f 看起来是一个function,但是实际上没那么简单
print(A.__dict__['f']) #如果f是一个function,根据我们已有的知识,它也应该存储在__dict__中,我们打印了之后发现,原来这个f是一个staticmethod object
print(A().f)
"""
深层理解
descriptor


classmethod 装饰器
第一个参数 cls 是一个Class,调用的时候不需要传入
第二个参数开始才是函数真正的参数
"""
class C:
    @classmethod
    def f(cls,x):
        print(cls,x)

C.f(1)
C().f(1)
print(C.f)
print(C.__dict__['f'])
print(C().f)
