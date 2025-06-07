#############
# None 是一个特殊值
# NoneType 是 None的类型
################
print(None)
print(type(None))

#############
# 函数中 返回值
###########

def func()-> None:
    print("这是一个返回None的函数")
    return None

func()

#############
# 初始化变量
##############

result = None
if result is None:
    print("变量未赋值")

###############
# 作为函数参数默认值
###############
def append_item(item,lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(append_item(1))

##################
# 条件判断中的布尔值,
# 但不等于False 或 0
#####################
if None:
    print("True")
else:
    print("False")

#################
# NoneType的应用场景
# 类型检查
################
x = None
if type(x) == type(None):
    print("x 是 NoneType")

#####################
# 动态类型检测中的安全操作
# 不确定变量是否为None 时
# 先检查类型避免错误
#######################

def process_data(data):
    if isinstance(data, type(None)):
        print("数据为空")
    else:
        print(f"数据长度: {len(data)}")

process_data(None)
process_data([1, 2])

###################
# tips:
# None是单例(Singleton)
# 所有对None的引用都指向同一内存地址
##################

a = None
b = None
print(a is b)

##############
# 避免直接比较 == None
# 推荐用 is None
# 因为 == 会调用对象的__eq__方法
# 可能被自定义逻辑干扰
################

class Custom:
    def __eq__(self, other):
        return True

obj = Custom()
print(obj == None)
print(obj is None)

###############
# None不可赋值
###############

# None = 1 # SyntaxError: can't assign to keyword