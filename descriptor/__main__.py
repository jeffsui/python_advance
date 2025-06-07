"""
descriptor 描述器

"""
# 请使用python代码实现一个descriptor描述器
class Descriptor:
   def __init__(self, value=0):
       self.value = value

   def __get__(self, instance, owner):
       print("Getting value:", self.value)
       return self.value

   def __set__(self, instance, value):
       print("Setting value:", value)
       self.value = value

   def __delete__(self, instance):
       print("Deleting value")
       del self.value

class MyClass:
   descriptor = Descriptor()


# 创建一个MyClass的实例
obj = MyClass()

# 访问descriptor的值
print(obj.descriptor)  # 输出：Getting value: 0

# 设置descriptor的值
obj.descriptor = 10
print(obj.descriptor)  # 输出：Setting value: 10

# 删除descriptor的值
del obj.descriptor
print(obj.descriptor)  # 输出：Deleting value