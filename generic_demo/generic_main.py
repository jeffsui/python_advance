"""
python中泛型 的示例
"""
from typing import List

class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Store:
    def __init__(self,stock:List[Animal])->None:
        self.stock = stock

    def sell(self)-> Animal:
        return self.stock.pop()

if __name__ == '__main__':
    mystore = Store([Dog(),Cat()])
    print(mystore.sell())
