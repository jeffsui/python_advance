"""
PEP695 示例 - 类型参数语法 (Type Parameter Syntax)
Python 3.12+ 引入的新语法，简化泛型编程
"""

from typing import TypeVar, Generic

# 传统方式 (PEP695之前)
T_old = TypeVar('T_old')
class BoxOld(Generic[T_old]):
    def __init__(self, value: T_old):
        self.value = value

# PEP695 新语法
class Box[T]:
    """泛型容器类"""
    def __init__(self, value: T):
        self.value = value

    def get_value(self) -> T:
        return self.value

    def set_value(self, new_value: T) -> None:
        self.value = new_value

# 多类型参数
class Pair[K, V]:
    """键值对容器"""
    def __init__(self, key: K, value: V):
        self.key = key
        self.value = value

    def get_pair(self) -> tuple[K, V]:
        return (self.key, self.value)

# 带约束的类型参数
class NumberBox[T: (int, float)]:
    """只接受数字类型的容器"""
    def __init__(self, value: T):
        self.value = value

    def double(self) -> T:
        return self.value * 2  # type: ignore

# 带默认值的类型参数
class OptionalBox[T = str]:
    """带默认类型参数的容器"""
    def __init__(self, value: T | None = None):
        self.value = value

# 函数中的类型参数
def first_item[T](items: list[T]) -> T:
    """返回列表的第一个元素"""
    return items[0]

def merge_dicts[K, V](dict1: dict[K, V], dict2: dict[K, V]) -> dict[K, V]:
    """合并两个字典"""
    return {**dict1, **dict2}

# 继承中的类型参数
class Stack[T]:
    """泛型栈"""
    def __init__(self):
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

class BoundedStack[T: (int, str)](Stack[T]):
    """限制类型的栈"""
    pass

# 实际使用示例
def demo_usage():
    """演示PEP695语法的使用"""

    # 基本泛型类
    int_box = Box(42)
    str_box = Box("hello")
    print(f"int_box: {int_box.get_value()}")
    print(f"str_box: {str_box.get_value()}")

    # 多类型参数
    pair = Pair("age", 25)
    key, value = pair.get_pair()
    print(f"Pair: {key} = {value}")

    # 带约束的类型
    num_box = NumberBox(3.14)
    print(f"Double: {num_box.double()}")

    # 带默认值的类型
    default_box = OptionalBox()  # 使用默认类型str
    int_opt_box = OptionalBox[int](100)
    print(f"Default box: {default_box.value}")
    print(f"Int box: {int_opt_box.value}")

    # 泛型函数
    numbers = [1, 2, 3]
    names = ["Alice", "Bob", "Charlie"]
    print(f"First number: {first_item(numbers)}")
    print(f"First name: {first_item(names)}")

    # 字典合并
    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3, "d": 4}
    merged = merge_dicts(dict1, dict2)
    print(f"Merged dict: {merged}")

    # 泛型栈
    stack = Stack[int]()
    stack.push(1)
    stack.push(2)
    print(f"Popped: {stack.pop()}")

# 高级特性：类型别名
Vector = list[float]
Matrix = list[Vector]

class Tensor[T]:
    """张量类"""
    def __init__(self, data: list[list[T]]):
        self.data = data

# 类型参数的高级用法示例
class Animal:
    def speak(self) -> str:
        return "Animal sound"

class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"

class Cat(Animal):
    def speak(self) -> str:
        return "Meow!"

class Container[T]:
    """通用容器"""
    def __init__(self, item: T):
        self.item = item
    
    def get_item(self) -> T:
        return self.item

class Processor[T]:
    """通用处理器"""
    def process(self, item: T) -> None:
        print(f"Processing: {item.speak()}")

# 类型参数的高级约束
class ComparableBox[T: (int, float, str)]:
    """可比较类型的容器"""
    def __init__(self, value: T):
        self.value = value
    
    def is_greater_than(self, other: T) -> bool:
        return self.value > other

# 递归类型参数
class TreeNode[T]:
    """二叉树节点"""
    def __init__(self, value: T):
        self.value = value
        self.left: TreeNode[T] | None = None
        self.right: TreeNode[T] | None = None

if __name__ == "__main__":
    print("=== PEP695 类型参数语法演示 ===")
    demo_usage()
    
    print("\n=== 高级用法演示 ===")
    # 容器使用
    animal_container = Container[Animal](Dog())
    print(f"Animal speaks: {animal_container.get_item().speak()}")
    
    # 处理器使用
    dog_processor = Processor[Dog]()
    dog_processor.process(Dog())
    
    # 可比较类型
    comp_box = ComparableBox(10)
    print(f"Is 10 > 5: {comp_box.is_greater_than(5)}")
    
    # 二叉树示例
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(f"Tree root: {root.value}, left: {root.left.value}, right: {root.right.value}")