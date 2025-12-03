"""
Counter

"""

from collections import Counter

# Create a list of items
num = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# Use Counter to count occurrences
cnt = Counter(num)
print(cnt)

# create from dictionary
ctr1 = Counter([1, 2, 2, 3, 3, 3])  # From a list
ctr2 = Counter({1: 2, 2: 3, 3: 1})  # From a dictionary
ctr3 = Counter("hello")  # From a string

print(ctr1)
print(ctr2)
print(ctr3)

ctr = Counter([1, 2, 2])

# elements()
ctr = Counter([1, 2, 2, 3, 3, 3])
items = list(ctr.elements())
print(items)

# Adding new elements
ctr.update([2, 3, 3, 3])
print(ctr)

# elements()
ctr = Counter([1, 2, 2, 3, 3, 3])
items = list(ctr.elements())
print(items)

# most_common()
ctr = Counter([1, 2, 2, 3, 3, 3])
common = ctr.most_common(2)
print(common)

# subtract()
ctr = Counter([1, 2, 2, 3, 3, 3])
ctr.subtract([2, 3, 3])
print(ctr)


# Arithmetic Operations on Counters
ctr1 = Counter([1, 2, 2, 3])
ctr2 = Counter([2, 3, 3, 4])

print(ctr1 + ctr2)  # Addition
print(ctr1 - ctr2)  # Subtraction
print(ctr1 & ctr2)  # Intersection
print(ctr1 | ctr2)  # Union
