
numbers: list[int]=list(range(1,11))
text:str="hello world"
rev: slice = slice(None,None,-1)
print(numbers[::-1])
print(text[::-1])
########
# 如果我想复用这个反转的操作
# 但是不想赋值粘贴这个代码
# 我想到的是构建一个slice对象
# 结果是一样的
###########

print(numbers[rev])
print(text[rev])

###########
# 修改最后一个参数为-2
# 我们就得到了一个每2个元素反转后的可迭代对象
###############

rev2: slice = slice(None,None,-2)

print(numbers[rev2])
print(text[rev2])

#############
# 同样我也可以构建一个返回一个切片前5个元素的对象
##############
f_five:slice = slice(None,5)

print(numbers[f_five])
print(text[f_five])

#################
# tips2
# 求差集、对称差集、交集
# 通过运算符 就可以实现类似操作
#############
set_a : set[int] = {1,2,3,4,5}
set_b : set[int] = {4,5,6,7,8}

print(set_a | set_b)
print(set_b - set_a)
print(set_a & set_b)
print(set_a ^ set_b)

#####################
# tips3
# 如何让一个类支持 f-string
#############
"""
class Book:
    def __init__(self,title:str,pages:int):
        self.title = title
        self.pages = pages
    def __format__(self, format_spec: Any) -> str:
        match format_spec:
            case 'time':
                return f"{self.pages/60:.2f}h"
            case "caps":
                return self.title.upper()
            case _:
                raise ValueError('unknown specifier for Book()')

def main()->None:
    hari_potter:Book = Book('Very Hairy Potter',300)
    python_daily:Book = Book('Python Daily',20)

    print(f"{hari_potter:caps}")
    print(f"Read Time:{hari_potter:time}")

    print(f"{python_daily:caps}")
    print(f"Read Time:{python_daily:time}")

    print(f"{python_daily:test}")

if __name__ == '__main__':
    main()

"""

###############
# tips 3:
# 判断一个用户是否存在
# 1 可以用一个类型守卫
# 2.也可以用wallet运算符
# 同样可以应用到函数和类中
# 1.普通函数统计一个字符串单词数量和字符总数
# 2.偏函数 柯里化
################
users:dict[int,str] = {0:'Bob',1:'Mario'}

# user: str | None = users.get(1)

# if user:
#     print(f'User found: {user}')
# else:
#     print('User not found')

if user := users.get(1):
    print(f'User found: {user}')
else:
    print('User not found')

def get_info(text:str)->dict:
    return {'words':(words:=text.split()),
             'word_count':len(words),
             "character_count":len(text)
            }
print(get_info("Hello World! This is a test."))

from typing import Callable


def multiply_setup(a:float)->Callable:
    def multiply(b:float)->float:
        return a * b
    return multiply

double:Callable = multiply_setup(2.0)
triple:Callable = multiply_setup(3.0)

print(double(5.0))  # 输出 10.0
print(triple(5.0))  # 输出 15.0



