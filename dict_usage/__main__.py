"""
演示了 Python 字典(dict)的常用内置方法：
1. values()      # 获取所有值
2. keys()        # 获取所有键
3. pop()         # 按键移除并返回对应的值
4. popitem()     # 移除并返回最后一个键值对
5. copy()        # 浅拷贝字典
6. get()         # 按键安全获取值,找不到返回None或指定默认值
7. setdefault()  # 获取键对应的值，不存在则插入并返回默认值
8. clear()       # 清空字典
9. fromkeys()    # 用序列创建新字典
10. items()      # 获取所有键值对元组
"""

# 1. values()
users:dict = {0:'Mario',1:'Luigi',2:'James'}
print(users.values())

# 2. keys()
print(users.keys())

# 3. pop()
print(users.pop(1))


# 4. popitem()
users.popitem()
print(users)

# 5. copy()
sample_dict:dict = {0:['a','b'],1:['c','d']}
my_copy: dict = sample_dict.copy()
print(id(sample_dict))
print(id(my_copy))
# 因为是潜拷贝 所以修改会传递
my_copy[0][0] = '!!!'
print(my_copy)
print(sample_dict)

# 6. get()
print(users.get(0)) #found key return value
print(users.get(999)) #not found key return None

# 7. setdefault()

users1:dict = {0:'Mario',1:'Luigi',2:'James'}
print(users1.setdefault(0,'???')) # key exsist return origin value
print(users1.setdefault(999,'???')) # key not exsist return new value
print(users1) # add an  new key-value item

# 8. clear()
users1.clear() # clear up dict
print(users1)

# 9. fromkeys()
people:list[str] = ['Mario','Luigi','James']
users2: dict = dict.fromkeys(people)
print(users2)
users3: dict = dict.fromkeys(people,'unknown')
print(users3)

# 10. items()

print(users3.items())

# 11. update()

users4:dict = {0:'Mario',1:'Luigi',2:'James'}
users4.update({2:'Bob',3:'James\'s Sister'}) # if key exsist will update value, or will add an new key-value item
print(users4)
users4 |= {10:'Spam',11:'Eggs'} # we can use the pipline (|) to extends dict
print(users4)
