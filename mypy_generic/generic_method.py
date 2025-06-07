from typing import TypeVar
from typing import List

T = TypeVar('T')

def first(items: List[T]) -> T:
    return items[0]

print(first([1, 2, 3]))  # 1
print(first(["apple", "banana", "cherry"]))  # apple
