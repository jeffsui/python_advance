"""
This script demonstrates how to use TypedDict in Python.
TypedDict is a way to specify the expected structure of a dictionary.
It allows you to define a dictionary with specific keys and their corresponding value types.

"""
from typing import List, Optional, TypedDict


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
