"""
mutable type

"""
from typing import List

words = "Hello"
print(id(words))
words+="  World"
print(id(words))

###################
# list is mutable
###################

my_list:List[int] = [1, 2, 3]
print(id(my_list))  # e.g., 140390658723904

my_list.append(4)
print(my_list)      # [1, 2, 3, 4]
print(id(my_list))  # same ID as before

student:List[str] = ['Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose']
print(student)
#################
# dict is mutable
#################
my_dict = {'a': 1, 'b': 2}
print(id(my_dict))  # e.g., 140390658724096

my_dict['c'] = 3
print(my_dict)      # {'a': 1, 'b': 2, 'c': 3}
print(id(my_dict))  # same ID as before


##############
# set is mutable
###############
my_set = {1, 2, 3}
print(id(my_set))   # e.g., 140390658724128

my_set.add(4)
print(my_set)       # {1, 2, 3, 4}
print(id(my_set))   # same ID as before


##############
# bytearray is mutable
###############
my_bytes = bytearray(b'hello')
print(id(my_bytes))     # e.g., 140390658724256

my_bytes[0] = ord(b'H')  # Change first byte to 'H'
print(my_bytes)          # bytearray(b'Hello')
print(id(my_bytes))      # same ID as before