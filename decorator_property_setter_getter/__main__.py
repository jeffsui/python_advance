class User:
    def __init__(self, name):
        self._name= name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if len(name) <5:
            raise ValueError("Name must be at least 5 characters long")
        self._name = name
    @classmethod
    def gen_user(cls):
        return cls("handsomeb")
    @staticmethod
    def length():
        return 18

    def greeting(self):
        return f"Hello, my name is {self._name}"

    def __str__(self):
        return f"{self._name}"

if __name__ == '__main__':
    user1 = User("handsomeb")
    print(user1.greeting())
    user2 = User("haha")
    user2.name = "haha"


