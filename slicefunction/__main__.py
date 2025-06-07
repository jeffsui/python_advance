"""
slice 函数
 Python内置的一个函数,用于生成一个切片对象。
 切片对象可以用来切片序列类型的数据,如字符串、列表和元组。
 基本语法 slice(start,end,step)
"""
s = "Hello, World!"
print(s[slice(0, 5)])  # 输出 "Hello"
print(s[slice(None, 5)])  # 输出 "Hello"

numbers = list(range(1,11))
print(numbers[slice(2,4)]) # [3,4]

print(s[slice(None,None,-1)]) #倒序输出:!dlroW ,olleH

print(numbers[slice(None,None,-2)]) #输出 [10, 8, 6, 4, 2]



