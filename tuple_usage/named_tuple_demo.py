"""
namedtuple_demo.py
Demonstrates the use of named tuples in Python.

"""
from collections import namedtuple

# Define a named tuple for a point in 2D space
Point = namedtuple('Point', ['x', 'y'])

def main():
    p1 = Point(1, 2)
    p2 = Point(3, 4)
    print("Point 1:", p1)
    print("Point 2:", p2)
    print("Distance:", calculate_distance(p1, p2))

def calculate_distance(p1, p2):
    return ((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2) ** 0.5

if __name__ == "__main__":
    main()