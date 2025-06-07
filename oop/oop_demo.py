"""
面向对象编程（OOP）是一种编程范式，它使用“对象”来组织代码。对象是类的实例，类定义了对象的属性和方法。OOP的主要特点包括封装、继承和多态。
面向对象编程的主要优点包括：
1. **封装**：将数据和操作数据的方法封装在一起，隐藏内部实现细节。
2. **继承**：允许新类从现有类继承属性和方法，促进代码重用。
3. **多态**：允许不同类的对象以相同的方式调用方法，提高代码的灵活性和可扩展性。

"""
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"
class Bird(Animal):
    def speak(self):
        return f"{self.name} says Tweet!"

def main():
    animals = [
        Dog("Buddy"),
        Cat("Whiskers"),
        Bird("Tweety")
    ]

    for animal in animals:
        print(animal.speak())
if __name__ == "__main__":
    main()
    # Output:
    # Buddy says Woof!
    # Whiskers says Meow!
    # Tweety says Tweet!