"""
IFFE (Immediately Invoked Function Expression) is a way to create a function and execute it immediately.
Syntax:

(lambda arguments: expression)(arguments)

Example:

(lambda x: x**2)(5)

Output: 25

"""
from datetime import datetime
@lambda _:_()
def start_time()->str:
    date = datetime.now()
    return date.strftime("%Y-%m-%d %H:%M:%S")
print(start_time)
