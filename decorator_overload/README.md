# Python 类型注解高级教程

本文档详细介绍了 Python 类型注解的高级用法，包括 `@overload`、`TypeVar`、`Literal`、`Union` 和 `Final` 等类型提示工具，涵盖了函数和类方法的重载、泛型编程、字面量类型等实用场景。

## 目录

1. [@overload 基础示例](#1-overload-基础示例)
2. [@overload 复杂示例 - 多参数重载](#2-overload-复杂示例---多参数重载)
3. [TypeVar 泛型示例 - 类型守恒](#3-typevar-泛型示例---类型守恒)
4. [带约束的 TypeVar](#4-带约束的-typevar)
5. [TypeVar + @overload 组合示例](#5-typevar--overload-组合示例)
6. [Literal 字面量类型示例](#6-literal-字面量类型示例)
7. [Literal + @overload 组合示例](#7-literal--overload-组合示例)
8. [Union 类型示例](#8-union-类型示例)
9. [Final 最终类型示例](#9-final-最终类型示例)
10. [综合示例：类型安全的 API 响应处理](#10-综合示例类型安全的-api-响应处理)
11. [类中方法示例：Calculator](#11-类中方法示例calculator)
12. [类中方法示例：DataProcessor](#12-类中方法示例dataprocessor)
13. [类中方法示例：ResponseBuilder](#13-类中方法示例responsebuilder)
14. [类中方法示例：GenericContainer](#14-类中方法示例genericcontainer)
15. [类中方法示例：MatrixOperations](#15-类中方法示例matrixoperations)
16. [类中方法示例：ConfigManager](#16-类中方法示例configmanager)
17. [类中方法示例：StringHelper](#17-类中方法示例stringhelper)

---

## 1. @overload 基础示例

`@overload` 装饰器允许为同一个函数定义多个类型签名，实现函数重载。

```python
from typing import overload

@overload
def double(x: int) -> int: ...

@overload
def double(x: str) -> str: ...

def double(x: int | str) -> int | str:
    if isinstance(x, (int, str)):
        return x * 2
    else:
        raise ValueError("Unsupported Type")
```

**运行示例：**

```python
y = double(5)        # 返回 int 类型
print(y + 3)         # 输出: 13

Y = double("hello")  # 返回 str 类型
print(Y + "world")   # 输出: hellohelloworld
```

**说明：**
- `@overload` 装饰器只用于类型检查，不参与实际运行
- 必须提供一个非装饰的实现在最后
- 类型检查器会根据参数类型推断返回类型

---

## 2. @overload 复杂示例 - 多参数重载

支持多个参数的不同组合类型。

```python
@overload
def process_data(data: int, scale: float) -> float: ...

@overload
def process_data(data: str, scale: int) -> str: ...

@overload
def process_data(data: list[int], scale: Literal["sum", "avg", "max"]) -> int: ...

def process_data(
    data: int | str | list[int], 
    scale: float | int | Literal["sum", "avg", "max"]
) -> float | str | int:
    """根据不同类型和参数处理数据"""
    if isinstance(data, int) and isinstance(scale, float):
        return data * scale
    elif isinstance(data, str) and isinstance(scale, int):
        return data * scale
    elif isinstance(data, list) and isinstance(scale, str) and scale in ("sum", "avg", "max"):
        if scale == "sum":
            return sum(data)
        elif scale == "avg":
            return sum(data) // len(data) if data else 0
        elif scale == "max":
            return max(data) if data else 0
    raise ValueError("Invalid parameters")
```

**运行示例：**

```python
result1 = process_data(10, 2.5)              # 输出: 25.0, 类型: float
result2 = process_data("hello", 3)          # 输出: hellohellohello, 类型: str
result3 = process_data([1, 2, 3, 4, 5], "avg") # 输出: 3, 类型: int
```

---

## 3. TypeVar 泛型示例 - 类型守恒

`TypeVar` 用于创建泛型变量，保持类型守恒。

```python
from typing import TypeVar

T = TypeVar("T")

def get_first(items: list[T]) -> T | None:
    """返回列表第一个元素，保持类型不变"""
    return items[0] if items else None
```

**运行示例：**

```python
first_int = get_first([1, 2, 3, 4, 5])      # 返回 int 类型: 1
first_str = get_first(["a", "b", "c"])      # 返回 str 类型: 'a'
```

**说明：**
- `T` 是一个泛型变量，可以根据输入类型自动推断
- 返回类型与输入类型保持一致

---

## 4. 带约束的 TypeVar

限制 TypeVar 只能是特定的类型。

```python
T1 = TypeVar("T1", int, float)  # T1 只能是 int 或 float

def add_numbers(a: T1, b: T1) -> T1:
    """只能添加数字类型"""
    return a + b
```

**运行示例：**

```python
sum1 = add_numbers(5, 10)      # 返回 int: 15
sum2 = add_numbers(5.5, 10.5)  # 返回 float: 16.0
```

---

## 5. TypeVar + @overload 组合示例

结合使用 TypeVar 和 @overload 实现更复杂的类型重载。

```python
@overload
def safe_divide(x: int, y: int) -> float: ...

@overload
def safe_divide(x: float, y: float) -> float: ...

@overload
def safe_divide(x: str, y: str) -> str: ...

def safe_divide(x: int | float | str, y: int | float | str) -> float | str:
    """安全的除法操作，支持不同类型"""
    if isinstance(x, (int, float)) and isinstance(y, (int, float)):
        if y == 0:
            return float("inf")
        return x / y
    elif isinstance(x, str) and isinstance(y, str):
        return f"{x}/{y}"
    raise ValueError("Invalid types")
```

**运行示例：**

```python
div1 = safe_divide(10, 3)        # 输出: 3.333..., 类型: float
div2 = safe_divide(10, 0)        # 输出: inf, 类型: float
div3 = safe_divide("apple", "pie")  # 输出: apple/pie, 类型: str
```

---

## 6. Literal 字面量类型示例

`Literal` 用于限制参数只能是特定的字面量值。

```python
from typing import Literal

Color = Literal["red", "green", "blue"]
Direction = Literal[0, 1, 2, 3]  # 0:上, 1:右, 2:下, 3:左

def set_color(color: Color) -> Color:
    """只接受特定的颜色值"""
    valid_colors: list[Color] = ["red", "green", "blue"]
    if color in valid_colors:
        return color
    raise ValueError(f"Invalid color: {color}")

def move(direction: Direction, steps: int = 1) -> tuple[int, int]:
    """根据方向移动"""
    directions = {
        0: (0, -steps),  # 上
        1: (steps, 0),   # 右
        2: (0, steps),   # 下
        3: (-steps, 0),  # 左
    }
    return directions[direction]
```

**运行示例：**

```python
color = set_color("red")     # 输出: 'red'
position = move(1, 5)        # 输出: (5, 0), 向右移动 5 步
```

---

## 7. Literal + @overload 组合示例

结合 Literal 和 @overload 实现基于字面量的类型重载。

```python
@overload
def config_value(key: Literal["host"]) -> str: ...

@overload
def config_value(key: Literal["port"]) -> int: ...

@overload
def config_value(key: Literal["debug"]) -> bool: ...

def config_value(key: Literal["host", "port", "debug"]) -> str | int | bool:
    """配置值获取，根据键返回不同类型"""
    config = {"host": "localhost", "port": 8080, "debug": True}
    return config[key]
```

**运行示例：**

```python
host = config_value("host")   # 返回 str: "localhost"
port = config_value("port")   # 返回 int: 8080
debug = config_value("debug") # 返回 bool: True
```

---

## 8. Union 类型示例

`Union` 表示参数可以是多种类型之一。

```python
from typing import Union

def parse_value(value: Union[int, str, bool]) -> str:
    """解析多种类型值为字符串"""
    if isinstance(value, bool):
        return "True" if value else "False"
    elif isinstance(value, int):
        return f"Number: {value}"
    else:
        return f"String: {value}"
```

**运行示例：**

```python
parse_value(100)    # 输出: "Number: 100"
parse_value("hello") # 输出: "String: hello"
parse_value(True)   # 输出: "True"
```

---

## 9. Final 最终类型示例

`Final` 用于声明不可重新赋值的常量。

```python
from typing import Final

MAX_CONNECTIONS: Final = 100
DEFAULT_TIMEOUT: Final[float] = 30.0
```

**说明：**
- 标记为 `Final` 的变量不应被重新赋值
- 类型检查器会发出警告

---

## 10. 综合示例：类型安全的 API 响应处理

结合多种类型注解实现类型安全的 API 响应处理。

```python
ResponseType = TypeVar("ResponseType", bound=dict)

@overload
def parse_api_response(response: dict[str, str]) -> list[str]: ...

@overload
def parse_api_response(response: dict[str, int]) -> list[int]: ...

def parse_api_response(
    response: dict[str, str] | dict[str, int]
) -> list[str] | list[int]:
    """解析 API 响应，返回对应类型的列表"""
    if not response:
        return []
    
    first_value = next(iter(response.values()))
    
    if isinstance(first_value, str):
        return [f"{k}: {v}" for k, v in response.items()]
    elif isinstance(first_value, int):
        return [int(v) for v in response.values()]
    
    return []
```

**运行示例：**

```python
str_response = {"name": "Alice", "city": "Beijing"}
parse_api_response(str_response)  # 输出: ['name: Alice', 'city: Beijing']

int_response = {"score": 95, "age": 25, "count": 3}
parse_api_response(int_response)  # 输出: [95, 25, 3]
```

---

## 11. 类中方法示例：Calculator

演示类方法的基础重载。

```python
class Calculator:
    """计算器类，演示方法重载"""

    @overload
    def calculate(self, x: int, y: int) -> int: ...

    @overload
    def calculate(self, x: float, y: float) -> float: ...

    @overload
    def calculate(self, x: str, y: str) -> str: ...

    def calculate(
        self, x: int | float | str, y: int | float | str
    ) -> int | float | str:
        """根据不同类型执行计算"""
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            return x + y
        elif isinstance(x, str) and isinstance(y, str):
            return f"{x} + {y}"
        raise ValueError("Unsupported types")
```

**运行示例：**

```python
calc = Calculator()
result1 = calc.calculate(10, 20)         # 输出: 30, 类型: int
result2 = calc.calculate(3.14, 2.86)      # 输出: 6.0, 类型: float
result3 = calc.calculate("Hello", "World")  # 输出: Hello + World, 类型: str
```

---

## 12. 类中方法示例：DataProcessor

演示 TypeVar 和 Literal 在类方法中的使用。

```python
class DataProcessor:
    """数据处理类，演示 TypeVar 在类方法中的使用"""

    @overload
    def process(self, data: list[int], mode: Literal["sum", "avg"]) -> int: ...

    @overload
    def process(self, data: list[str], mode: Literal["join"]) -> str: ...

    @overload
    def process(
        self, data: list[dict[str, int]], mode: Literal["merge"]
    ) -> dict[str, int]: ...

    def process(
        self,
        data: list[int] | list[str] | list[dict[str, int]],
        mode: Literal["sum", "avg", "join", "merge"],
    ) -> int | str | dict[str, int]:
        """处理不同类型的数据"""
        if not data:
            raise ValueError("Empty data")

        if isinstance(data[0], int) and mode in ("sum", "avg"):
            if mode == "sum":
                return sum(data)
            else:
                return sum(data) // len(data)

        elif isinstance(data[0], str) and mode == "join":
            return " ".join(data)

        elif isinstance(data[0], dict) and mode == "merge":
            result: dict[str, int] = {}
            for item in data:
                for k, v in item.items():
                    result[k] = result.get(k, 0) + v
            return result

        raise ValueError("Invalid combination of data type and mode")
```

**运行示例：**

```python
processor = DataProcessor()
processor.process([1, 2, 3, 4, 5], "sum")                    # 输出: 15
processor.process([10, 20, 30, 40, 50], "avg")              # 输出: 30
processor.process(["Hello", "World", "Python"], "join")   # 输出: "Hello World Python"
processor.process([{"a": 1, "b": 2}, {"a": 3, "b": 4}], "merge")  # 输出: {'a': 4, 'b': 6}
```

---

## 13. 类中方法示例：ResponseBuilder

演示 Literal + @overload 在类方法中的使用。

```python
class ResponseBuilder:
    """响应构建器，演示 Literal + @overload 在类方法中的使用"""

    @overload
    def build(self, status: Literal["success"], data: dict) -> dict: ...

    @overload
    def build(self, status: Literal["error"], message: str) -> dict: ...

    @overload
    def build(self, status: Literal["warning"], data: dict, message: str) -> dict: ...

    def build(
        self,
        status: Literal["success", "error", "warning"],
        data: dict | None = None,
        message: str | None = None,
    ) -> dict:
        """构建不同类型的响应"""
        response: dict = {"status": status}

        if status == "success" and isinstance(data, dict):
            response["data"] = data
        elif status == "error" and isinstance(message, str):
            response["message"] = message
        elif (
            status == "warning" and isinstance(data, dict) and isinstance(message, str)
        ):
            response["data"] = data
            response["message"] = message

        return response
```

**运行示例：**

```python
builder = ResponseBuilder()
builder.build("success", {"id": 1, "name": "Alice"})  
# 输出: {'status': 'success', 'data': {'id': 1, 'name': 'Alice'}}

builder.build("error", "Invalid input")  
# 输出: {'status': 'error', 'message': 'Invalid input'}

builder.build("warning", {"warning": "Low disk space"}, "Disk at 90%")  
# 输出: {'status': 'warning', 'data': {'warning': 'Low disk space'}, 'message': 'Disk at 90%'}
```

---

## 14. 类中方法示例：GenericContainer

演示 TypeVar 在类中的应用。

```python
T = TypeVar("T")

class GenericContainer:
    """泛型容器类，演示 TypeVar 在类中的应用"""

    def __init__(self, initial_value: T):
        self.value = initial_value

    @overload
    def update(self, new_value: int) -> int: ...

    @overload
    def update(self, new_value: str) -> str: ...

    @overload
    def update(self, new_value: list) -> list: ...

    def update(self, new_value: T) -> T:
        """更新容器中的值"""
        self.value = new_value
        return self.value

    def get(self) -> T:
        """获取容器中的值"""
        return self.value

    def transform(self, func) -> T:
        """对值应用转换函数"""
        self.value = func(self.value)
        return self.value
```

**运行示例：**

```python
container_int = GenericContainer(100)
container_int.get()                              # 输出: 100
container_int.update(200)                        # 输出: 200
container_int.transform(lambda x: x * 2)         # 输出: 400

container_str = GenericContainer("Hello")
container_str.get()                              # 输出: "Hello"
container_str.update("World")                    # 输出: "World"
container_str.transform(lambda x: x.upper())      # 输出: "WORLD"
```

---

## 15. 类中方法示例：MatrixOperations

演示复杂的类方法重载。

```python
class MatrixOperations:
    """矩阵操作类，演示复杂的类方法重载"""

    @overload
    def multiply(self, matrix: list[list[int]], scalar: int) -> list[list[int]]: ...

    @overload
    def multiply(
        self, matrix: list[list[int]], other: list[list[int]]
    ) -> list[list[int]]: ...

    def multiply(
        self, matrix: list[list[int]], factor: int | list[list[int]]
    ) -> list[list[int]]:
        """矩阵乘法：标量乘法或矩阵乘法"""
        if isinstance(factor, int):
            # 标量乘法
            return [[cell * factor for cell in row] for row in matrix]
        else:
            # 矩阵乘法
            if len(matrix[0]) != len(factor):
                raise ValueError("Invalid matrix dimensions for multiplication")

            result: list[list[int]] = []
            for i in range(len(matrix)):
                result_row: list[int] = []
                for j in range(len(factor[0])):
                    sum_val = 0
                    for k in range(len(factor)):
                        sum_val += matrix[i][k] * factor[k][j]
                    result_row.append(sum_val)
                result.append(result_row)
            return result
```

**运行示例：**

```python
matrix_ops = MatrixOperations()
matrix_ops.multiply([[1,2],[3,4]], 2)  
# 输出: [[2, 4], [6, 8]]

matrix_ops.multiply([[1,2],[3,4]], [[5,6],[7,8]])  
# 输出: [[19, 22], [43, 50]]
```

---

## 16. 类中方法示例：ConfigManager

演示类方法的类型守恒。

```python
class ConfigManager:
    """配置管理器，演示类方法的类型守恒"""

    def __init__(self):
        self._config: dict[str, Union[str, int, bool, list]] = {
            "host": "localhost",
            "port": 8080,
            "debug": True,
            "allowed_hosts": ["127.0.0.1", "localhost"],
        }

    @overload
    def get(self, key: Literal["host"]) -> str: ...

    @overload
    def get(self, key: Literal["port"]) -> int: ...

    @overload
    def get(self, key: Literal["debug"]) -> bool: ...

    @overload
    def get(self, key: Literal["allowed_hosts"]) -> list[str]: ...

    def get(self, key: str) -> Union[str, int, bool, list]:
        """获取配置值，根据键返回特定类型"""
        return self._config[key]

    @overload
    def set(self, key: Literal["host"], value: str) -> None: ...

    @overload
    def set(self, key: Literal["port"], value: int) -> None: ...

    @overload
    def set(self, key: Literal["debug"], value: bool) -> None: ...

    @overload
    def set(self, key: Literal["allowed_hosts"], value: list[str]) -> None: ...

    def set(self, key: str, value: Union[str, int, bool, list]) -> None:
        """设置配置值"""
        self._config[key] = value
```

**运行示例：**

```python
config_mgr = ConfigManager()
config_mgr.get("host")            # 返回 str: "localhost"
config_mgr.get("port")            # 返回 int: 8080
config_mgr.get("debug")           # 返回 bool: True
config_mgr.get("allowed_hosts")   # 返回 list: ["127.0.0.1", "localhost"]

config_mgr.set("host", "example.com")
config_mgr.set("port", 9000)
config_mgr.set("debug", False)
config_mgr.set("allowed_hosts", ["192.168.1.1", "example.com"])
```

---

## 17. 类中方法示例：StringHelper

演示字符串处理的重载。

```python
class StringHelper:
    """字符串辅助类，演示字符串处理的重载"""

    @overload
    def format(self, template: str, values: tuple) -> str: ...

    @overload
    def format(self, template: str, values: dict) -> str: ...

    def format(self, template: str, values: tuple | dict) -> str:
        """格式化字符串"""
        if isinstance(values, tuple):
            return template.format(*values)
        elif isinstance(values, dict):
            return template.format(**values)
        else:
            # 如果是单个值，包装成元组处理
            return template.format(values)

    @overload
    def extract(self, text: str, pattern: str, count: Literal[1]) -> str: ...

    @overload
    def extract(self, text: str, pattern: str, count: int) -> list[str]: ...

    def extract(self, text: str, pattern: str, count: int) -> str | list[str]:
        """从文本中提取匹配项"""
        import re

        matches = re.findall(pattern, text)

        if count == 1:
            return matches[0] if matches else ""
        else:
            return matches[:count] if len(matches) >= count else matches
```

**运行示例：**

```python
helper = StringHelper()

# format 方法
helper.format("Hello, {}!", "World")                              # 输出: "Hello, World!"
helper.format("Hello, {name}!", {"name": "Python"})              # 输出: "Hello, Python!"
helper.format("Values: {}, {}, {}", (1, 2, 3))                  # 输出: "Values: 1, 2, 3"

# extract 方法
text = "Emails: alice@example.com, bob@test.com, charlie@demo.org"
helper.extract(text, r"\b[\w.]+@[\w.]+\b", 1)    # 输出: "alice@example.com", 类型: str
helper.extract(text, r"\b[\w.]+@[\w.]+\b", 3)    # 输出: ['alice@example.com', 'bob@test.com', 'charlie@demo.org'], 类型: list
```

---

## 总结

本教程涵盖了 Python 类型注解的高级用法：

1. **@overload**: 函数/方法重载，实现同一函数的不同类型签名
2. **TypeVar**: 泛型变量，保持类型守恒
3. **Literal**: 字面量类型，限定参数为特定值
4. **Union**: 联合类型，参数可以是多种类型之一
5. **Final**: 最终类型，声明不可重新赋值的常量

通过合理使用这些类型注解工具，可以：
- 提高代码的可读性和可维护性
- 让类型检查器更好地推断类型
- 减少运行时错误
- 改善 IDE 的代码提示和自动补全

**运行完整示例：**

```bash
cd e:\code\python_advance
python decorator_overload/__main__.py
```

所有示例都已包含在 `decorator_overload/__main__.py` 文件中，可以直接运行查看效果。
