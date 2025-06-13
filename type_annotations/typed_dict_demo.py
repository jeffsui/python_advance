"""
This script demonstrates how to use TypedDict in Python.
TypedDict is a way to specify the expected structure of a dictionary.
It allows you to define a dictionary with specific keys and their corresponding value types.

"""
from typing import List, NotRequired, Optional, Required, TypedDict


class Person(TypedDict):
    name: str
    age: int
    hobbies: List[str]


def print_person_info(person: Person) -> None:
    """
    Prints the information of a person.

    :param person: A dictionary representing a person with keys 'name', 'age', and 'hobbies'.
    """
    print(f"Name: {person['name']}")
    print(f"Age: {person['age']}")
    print(f"Hobbies: {', '.join(person['hobbies'])}")


# Example usage
if __name__ == "__main__":
    person_info: Person = {"name": "Alice", "age": 30, "hobbies": ["reading", "hiking", "coding"]}
    print_person_info(person_info)

    # Example of a function that expects a TypedDict
    def get_person_hobby(person: Person) -> str:
        return person['hobbies'][0] if person['hobbies'] else "No hobbies"

    print(get_person_hobby(person_info))
    # Example of a TypedDict with optional fields


class Employee(TypedDict, total=False):
    name: str
    age: int
    position: Optional[str]  # Optional field
    department: Optional[str]  # Optional field


def print_employee_info(employee: Employee) -> None:
    """
    Prints the information of an employee.
    :param employee: A dictionary representing an employee with keys 'name', 'age', 'position', and 'department'.
    """
    print(f"Name: {employee['name']}")
    print(f"Age: {employee['age']}")
    if 'position' in employee:
        print(f"Position: {employee['position']}")
    if 'department' in employee:
        print(f"Department: {employee['department']}")


# Example usage of Employee TypedDict
if __name__ == "__main__":
    employee_info: Employee = {"name": "Bob", "age": 28, "position": "Software Engineer"}
    print_employee_info(employee_info)

    # Example with missing optional fields
    employee_info_partial: Employee = {"name": "Charlie", "age": 35}
    print_employee_info(employee_info_partial)
    # Example with all fields
    employee_info_full: Employee = {"name": "Diana", "age": 40, "position": "Project Manager", "department": "IT"}
    print_employee_info(employee_info_full)

# 3.11 support Required NotRequired
class Print2D(TypedDict):
    x:int
    y:int
    label: NotRequired[str]

def print2D(print2d: Print2D):
    print(f'x:{print2d["x"]}')
    print(f'y:{print2d["y"]}')
# 3.11 中 可以设置total属性,false代表所有属性都不是必须的
class Print3D(TypedDict,total=False):
    x:Required[int]
    y:Required[int]
    z:Required[int]
    label: NotRequired[str]

# 3.13 中新增了 TypeAlias(类型别名的方式,我个人倾向用类语法实现)
# Print3D = TypedDict(
#     "Print3D",
#     {
#         'x':int,
#         'y':int,
#         'z':int,
#         'label': str
#     }
# )

def print3D(print3d: Print3D):
    print(f'x:{print3d["x"]}')
    print(f'y:{print3d["y"]}')
    print(f'z:{print3d["z"]}')
    print(f'label:{print3d["label"]}')

if __name__ == '__main__':
    print2D({'x':1,'y':2})
    print3D({'x':3,'y':4,'z':5,'label':"3D"})
