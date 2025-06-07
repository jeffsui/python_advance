from typing import List, TypeVar, Generic
T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self.items: List[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

stack = Stack[int]()
stack.push(1)
stack.push(2)
print(stack.pop())  # 2
1