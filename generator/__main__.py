"""
lst = [1,2,3,4,5]
# g = (n for n in lst if n in lst)
# 等价于
print(id(lst))
def __g(it):
    for n in it:
        if n in lst:
            yield n
print(__g,type(__g))
g = __g(iter(lst))
print(dir(g))
# 这里lst用的其实是全局的lst
lst = [0,1,2]
print(id(lst))
print(list(g))
"""
lst = [1,2,3]
g = ((a,b) for a in lst for b in lst)
lst = [1,2]
print(list(g))

