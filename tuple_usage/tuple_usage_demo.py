"""
tuple has hashable
"""
coords = set()
a = (1, 2)
b = (2, 2)
coords.add(a)
coords.add(b)
print(coords)
"""
memory sharing
"""
a = (1, 2)
b = (1, 2)
print(id(a))
print(id(b))
"""
packing & unpacking
"""
x, y, z = (1, 2, 3)
print(x)
print(y)
print(z)

nums = x, y, z
print(nums)
"""
tuple unpacking with * operator
"""


def sum_and_product(*args):
    total_sum = sum(args)
    total_product = 1
    for num in args:
        total_product *= num
    return total_sum, total_product


result = sum_and_product(1, 2, 3, 4)
print(f"Sum: {result[0]}, Product: {result[1]}")
