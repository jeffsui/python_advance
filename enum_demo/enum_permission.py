from enum import Enum,Flag,unique,IntFlag

"""
class Permission(Enum):
    NONE = 0
    READ = 1
    WRITE = 2
    EXECUTE = 4


if __name__ == '__main__':
    print(Permission.READ)
    print(Permission(1))
"""
##################################################
# 枚举类可以定义常量，每个常量都有唯一的数值，可以直接通过数值访问常量
# 枚举类可以继承 Enum 类，也可以继承 Flag 类，
# Flag 类可以定义多个常量，每个常量都是一个二进制位，可以组合多个常量
# 枚举类可以用 in 操作符来判断某个常量是否被设置，也可以通过 for... in... 循环来遍历枚举类中的所有成员
###################################################

"""
class Permission(Flag):
    NONE = 0
    READ = 1
    WRITE = 2
    EXECUTE = 4

rw = Permission.READ | Permission.WRITE
print(rw,rw.value)
# 通过 in 操作符 可以判断某个权限是否被设置
if Permission.READ in rw:
    print("read permission is set")

if Permission.EXECUTE in rw:
    print("EXECUTE permission is set")
# Python3.11 可以通过 for... in... 循环来遍历枚举类中的所有成员
for perm in Permission:
    print(f"Has {perm.name} permission: {perm.value}")
"""

##################################################
# 可以通过继承 Flag 类来定义自己的枚举类
# 自定义的枚举类可以继承多个 Flag 类，并通过位运算来组合多个权限
###################################################
# class Permission(Flag):
#     NONE = 0
#     READ = 1
#     WRITE = 2
#     EXECUTE = 4
#     RW   = READ | WRITE
#     RX   = READ | EXECUTE
#     RWX  = READ | WRITE | EXECUTE

# rw = Permission.RW

# for perm in rw:
#     print(f"Has {perm.name} permission: {perm.value}")


#########################
# 还可以定义枚举类成员的别名
########################
"""
class Permission(Flag):
    NONE = 0
    READ = 1
    WRITE = 2
    EXECUTE = 4
    RW = READ | WRITE  # 定义 RW 权限
    R = READ  # 定义 READ 的别名

if Permission.R in Permission.RW:
    print("READ permission is set in RW")
"""
############################################
#unique 装饰器可以确保枚举类中的所有成员值都是唯一的
# 比如 Permission 类中定义了 READ 权限，如果再定义一个 READ 权限的别名 R，会报错
############################################
"""
@unique
class Permission(Flag):
    NONE = 0
    READ = 1
    WRITE = 2
    EXECUTE = 4
    RW = READ | WRITE  # 定义 RW 权限
    R = READ  # 定义 READ 的别名
"""
########################
# 枚举类不支持 算术运算符
#######################

# class Permission(Flag):
#     NONE = 0
#     READ = 1
#     WRITE = 2
#     EXECUTE = 3
# TypeError: unsupported operand type(s) for +: 'Permission' and 'Permission'
# rw = Permission.READ + Permission.WRITE
class Permission(IntFlag):
    NONE = 0
    READ = 1
    WRITE = 2
    EXECUTE = 3

# 虽然支持了算术运算,这时候已经不是枚举类了,而是普通的整数
rw = Permission.READ | Permission.WRITE
print(rw) # 输出 3
