"""
如何实现一个固定长度的元组
1. 使用类型标注(无法限制长度,不建议)
2. 使用具名元组 NamedType(推荐使用*****)
3. 自定义类型模拟固定长度行为
4. 使用dataclass进行限制(推荐使用,建立数据模型****)
"""
from dataclasses import dataclass
from typing import NamedTuple, Tuple

#################
# 方法一: 类型标注
################
point:Tuple[int,int] = (10,20)
print(point,type(point))

class Point(NamedTuple):
    x:int
    y:int
    label:str = 'default'

#################
# 方法二: 具名元组
#################
p = Point(10,20)
print(p,type(p))
# p.z = 30

################
# 方法三: 自定义类型模拟固定长度行为
################
class FixedTuple:
    def __init__(self,items):
        self._items = tuple(items)

    def __getitem__(self,index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return repr(self._items)

t  = FixedTuple([1,2,3])
print(t,type(t))
# 可以修改 t._items = (3,4,5),但是可以约束限制修改

###############
# 方法四: 使用dataclass进行限制(推荐使用,建立数据模型****)
###############
@dataclass(frozen=True)
class FixedTuple2:
    x:int
    y:int
    label:str = 'default'
p = Point(10,20)
print(p,type(p))
