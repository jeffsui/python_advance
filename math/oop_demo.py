"""
class 关键字 用于声明类
类名: 驼峰命名法 首字母大写

类初始化后才能使用
__init__ 方法用于初始化对象,同时给属性赋值
成员属性: 在__init__中声明并初始化的变量
成员方法: 第一个参数是self,代表当前实例(对象)

私有属性 vs 共有属性
1. 私有属性 两个下划线修饰 无法直接访问
2. 公有属性 通过对象.属性名,可以直接访问

"""
class Microwave:
    def __init__(self,brand:str,power:float) -> None:
        self.brand = brand
        self.power = power
        self.turnd_on:bool = False
    def turn_on(self):
        if self.turn_on:
            print(f"Microwave({self.brand}) is already turned on")
        else:
            self.turnd_on = True
            print(f"Microwave({self.brand}) is now turned on")
    def turn_off(self):
        if self.turnd_on:
            self.turnd_on = False
            print(f"Microwave({self.brand}) is now turned off")
        else:
            print(f"Microwave({self.brand}) is already turned off")
    def run(self,second:int):
        if self.turnd_on:
            print(f"Running ({self.brand}) for {second} seconds")
    def __add__(self,other):
        if isinstance(other,Microwave):
            return self.brand+" "+other.brand
        else:
            raise Exception("not the same Type,can't add operation")


smage:Microwave = Microwave("Smage",2.5)
print(smage)
print(f"车 型号:{smage.brand},{smage.power} 匹马力")
smage.turn_on()
smage.run(8)
smage.turn_off()

bosch:Microwave = Microwave('Bosch',2.8)

print(smage+bosch)