"""
Python 类型注解高级示例：
- @overload: 函数重载
- TypeVar: 泛型变量
- Literal: 字面量类型
- Union: 联合类型
- Final: 最终类型
"""

from typing import Final, Literal, TypeVar, Union, overload

# ============================================
# 1. @overload 基础示例
# ============================================


@overload
def double(x: int) -> int: ...


@overload
def double(x: str) -> str: ...


def double(x: int | str) -> int | str:
    if isinstance(x, (int, str)):
        return x * 2
    else:
        raise ValueError("Unsupported Type")


# ============================================
# 2. @overload 复杂示例 - 多参数重载
# ============================================


@overload
def process_data(data: int, scale: float) -> float: ...


@overload
def process_data(data: str, scale: int) -> str: ...


@overload
def process_data(data: list[int], scale: Literal["sum", "avg", "max"]) -> int: ...


def process_data(
    data: int | str | list[int], scale: float | int | Literal["sum", "avg", "max"]
) -> float | str | int:
    """根据不同类型和参数处理数据"""
    if isinstance(data, int) and isinstance(scale, float):
        return data * scale
    elif isinstance(data, str) and isinstance(scale, int):
        return data * scale
    elif (
        isinstance(data, list)
        and isinstance(scale, str)
        and scale in ("sum", "avg", "max")
    ):
        if scale == "sum":
            return sum(data)
        elif scale == "avg":
            return sum(data) // len(data) if data else 0
        elif scale == "max":
            return max(data) if data else 0
    raise ValueError("Invalid parameters")


# ============================================
# 3. TypeVar 泛型示例 - 类型守恒
# ============================================

T = TypeVar("T")


def get_first(items: list[T]) -> T | None:
    """返回列表第一个元素，保持类型不变"""
    return items[0] if items else None


# 带约束的 TypeVar
T1 = TypeVar("T1", int, float)  # T1 只能是 int 或 float


def add_numbers(a: T1, b: T1) -> T1:
    """只能添加数字类型"""
    return a + b  # type: ignore


# ============================================
# 4. TypeVar + @overload 组合示例
# ============================================


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


# ============================================
# 5. Literal 字面量类型示例
# ============================================

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
        1: (steps, 0),  # 右
        2: (0, steps),  # 下
        3: (-steps, 0),  # 左
    }
    return directions[direction]


# ============================================
# 6. Literal + @overload 组合示例
# ============================================


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


# ============================================
# 7. Union 类型示例
# ============================================


def parse_value(value: Union[int, str, bool]) -> str:
    """解析多种类型值为字符串"""
    if isinstance(value, bool):
        return "True" if value else "False"
    elif isinstance(value, int):
        return f"Number: {value}"
    else:
        return f"String: {value}"


# ============================================
# 8. Final 最终类型示例
# ============================================

MAX_CONNECTIONS: Final = 100
DEFAULT_TIMEOUT: Final[float] = 30.0


# ============================================
# 9. 综合示例：类型安全的 API 响应处理
# ============================================

ResponseType = TypeVar("ResponseType", bound=dict)


@overload
def parse_api_response(response: dict[str, str]) -> list[str]: ...


@overload
def parse_api_response(response: dict[str, int]) -> list[int]: ...


def parse_api_response(
    response: dict[str, str] | dict[str, int],
) -> list[str] | list[int]:
    """解析 API 响应，返回对应类型的列表"""
    if not response:
        return []

    first_value = next(iter(response.values()))

    if isinstance(first_value, str):
        return [f"{k}: {v}" for k, v in response.items()]
    elif isinstance(first_value, int):
        return [int(v) for v in response.values()]  # type: ignore

    return []


# ============================================
# 10. 类中方法的 @overload 示例
# ============================================


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
                return sum(data)  # type: ignore
            else:
                return sum(data) // len(data)  # type: ignore

        elif isinstance(data[0], str) and mode == "join":
            return " ".join(data)  # type: ignore

        elif isinstance(data[0], dict) and mode == "merge":
            result: dict[str, int] = {}
            for item in data:
                for k, v in item.items():
                    result[k] = result.get(k, 0) + v
            return result

        raise ValueError("Invalid combination of data type and mode")


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


# ============================================
# 测试代码
# ============================================

if __name__ == "__main__":
    print("=" * 60)
    print("1. @overload 基础示例")
    print("=" * 60)
    y = double(5)
    print(f"double(5) = {y}, type: {type(y).__name__}")
    print(f"y + 3 = {y + 3}")

    Y = double("hello")
    print(f"double('hello') = '{Y}', type: {type(Y).__name__}")
    print(f"Y + 'world' = '{Y}world'")

    print("\n" + "=" * 60)
    print("2. @overload 复杂示例")
    print("=" * 60)
    result1 = process_data(10, 2.5)
    print(f"process_data(10, 2.5) = {result1}, type: {type(result1).__name__}")

    result2 = process_data("hello", 3)
    print(f"process_data('hello', 3) = '{result2}', type: {type(result2).__name__}")

    result3 = process_data([1, 2, 3, 4, 5], "avg")
    print(
        f"process_data([1,2,3,4,5], 'avg') = {result3}, type: {type(result3).__name__}"
    )

    print("\n" + "=" * 60)
    print("3. TypeVar 泛型示例")
    print("=" * 60)
    first_int = get_first([1, 2, 3, 4, 5])
    print(f"get_first([1,2,3,4,5]) = {first_int}, type: {type(first_int).__name__}")

    first_str = get_first(["a", "b", "c"])
    print(f"get_first(['a','b','c']) = '{first_str}', type: {type(first_str).__name__}")

    print("\n" + "=" * 60)
    print("4. 带约束的 TypeVar")
    print("=" * 60)
    sum1 = add_numbers(5, 10)
    print(f"add_numbers(5, 10) = {sum1}, type: {type(sum1).__name__}")

    sum2 = add_numbers(5.5, 10.5)
    print(f"add_numbers(5.5, 10.5) = {sum2}, type: {type(sum2).__name__}")

    print("\n" + "=" * 60)
    print("5. safe_divide 示例")
    print("=" * 60)
    div1 = safe_divide(10, 3)
    print(f"safe_divide(10, 3) = {div1}, type: {type(div1).__name__}")

    div2 = safe_divide(10, 0)
    print(f"safe_divide(10, 0) = {div2}, type: {type(div2).__name__}")

    div3 = safe_divide("apple", "pie")
    print(f"safe_divide('apple', 'pie') = '{div3}', type: {type(div3).__name__}")

    print("\n" + "=" * 60)
    print("6. Literal 字面量类型示例")
    print("=" * 60)
    color = set_color("red")
    print(f"set_color('red') = '{color}'")

    position = move(1, 5)  # 向右移动 5 步
    print(f"move(1, 5) = {position}")

    print("\n" + "=" * 60)
    print("7. config_value 示例")
    print("=" * 60)
    host = config_value("host")
    print(f"config_value('host') = '{host}', type: {type(host).__name__}")

    port = config_value("port")
    print(f"config_value('port') = {port}, type: {type(port).__name__}")

    debug = config_value("debug")
    print(f"config_value('debug') = {debug}, type: {type(debug).__name__}")

    print("\n" + "=" * 60)
    print("8. parse_value 示例")
    print("=" * 60)
    print(f"parse_value(100) = {parse_value(100)}")
    print(f"parse_value('hello') = {parse_value('hello')}")
    print(f"parse_value(True) = {parse_value(True)}")

    print("\n" + "=" * 60)
    print("9. Final 常量示例")
    print("=" * 60)
    print(f"MAX_CONNECTIONS = {MAX_CONNECTIONS}")
    print(f"DEFAULT_TIMEOUT = {DEFAULT_TIMEOUT}")

    print("\n" + "=" * 60)
    print("10. 综合示例：API 响应处理")
    print("=" * 60)
    str_response = {"name": "Alice", "city": "Beijing"}
    parsed_str = parse_api_response(str_response)
    print(f"parse_api_response({str_response}) = {parsed_str}")

    int_response = {"score": 95, "age": 25, "count": 3}
    parsed_int = parse_api_response(int_response)
    print(f"parse_api_response({int_response}) = {parsed_int}")

    print("\n" + "=" * 60)
    print("11. 类中方法示例：Calculator")
    print("=" * 60)
    calc = Calculator()
    result1 = calc.calculate(10, 20)
    print(f"calc.calculate(10, 20) = {result1}, type: {type(result1).__name__}")

    result2 = calc.calculate(3.14, 2.86)
    print(f"calc.calculate(3.14, 2.86) = {result2}, type: {type(result2).__name__}")

    result3 = calc.calculate("Hello", "World")
    print(
        f"calc.calculate('Hello', 'World') = '{result3}', type: {type(result3).__name__}"
    )

    print("\n" + "=" * 60)
    print("12. 类中方法示例：DataProcessor")
    print("=" * 60)
    processor = DataProcessor()

    int_result = processor.process([1, 2, 3, 4, 5], "sum")
    print(
        f"processor.process([1,2,3,4,5], 'sum') = {int_result}, type: {type(int_result).__name__}"
    )

    avg_result = processor.process([10, 20, 30, 40, 50], "avg")
    print(
        f"processor.process([10,20,30,40,50], 'avg') = {avg_result}, type: {type(avg_result).__name__}"
    )

    str_result = processor.process(["Hello", "World", "Python"], "join")
    print(
        f"processor.process(['Hello','World','Python'], 'join') = '{str_result}', type: {type(str_result).__name__}"
    )

    dict_data = [{"a": 1, "b": 2}, {"a": 3, "b": 4}]
    dict_result = processor.process(dict_data, "merge")
    print(
        f"processor.process({dict_data}, 'merge') = {dict_result}, type: {type(dict_result).__name__}"
    )

    print("\n" + "=" * 60)
    print("13. 类中方法示例：ResponseBuilder")
    print("=" * 60)
    builder = ResponseBuilder()

    success_response = builder.build("success", {"id": 1, "name": "Alice"})
    print(
        f"builder.build('success', {{'id': 1, 'name': 'Alice'}}) = {success_response}"
    )

    error_response = builder.build("error", "Invalid input")
    print(f"builder.build('error', 'Invalid input') = {error_response}")

    warning_response = builder.build(
        "warning", {"warning": "Low disk space"}, "Disk at 90%"
    )
    print(
        f"builder.build('warning', {{'warning': 'Low disk space'}}, 'Disk at 90%') = {warning_response}"
    )

    print("\n" + "=" * 60)
    print("14. 类中方法示例：GenericContainer")
    print("=" * 60)

    container_int = GenericContainer(100)
    print(
        f"container_int.get() = {container_int.get()}, type: {type(container_int.get()).__name__}"
    )
    container_int.update(200)
    print(f"container_int.update(200) = {container_int.get()}")
    container_int.transform(lambda x: x * 2)
    print(f"container_int.transform(lambda x: x * 2) = {container_int.get()}")

    container_str = GenericContainer("Hello")
    print(
        f"\ncontainer_str.get() = '{container_str.get()}', type: {type(container_str.get()).__name__}"
    )
    container_str.update("World")
    print(f"container_str.update('World') = '{container_str.get()}'")
    container_str.transform(lambda x: x.upper())
    print(f"container_str.transform(lambda x: x.upper()) = '{container_str.get()}'")

    print("\n" + "=" * 60)
    print("15. 类中方法示例：MatrixOperations")
    print("=" * 60)
    matrix_ops = MatrixOperations()

    matrix1 = [[1, 2], [3, 4]]
    scalar_result = matrix_ops.multiply(matrix1, 2)
    print(f"matrix_ops.multiply([[1,2],[3,4]], 2) = {scalar_result}")

    matrix2 = [[5, 6], [7, 8]]
    matrix_result = matrix_ops.multiply(matrix1, matrix2)
    print(f"matrix_ops.multiply([[1,2],[3,4]], [[5,6],[7,8]]) = {matrix_result}")

    print("\n" + "=" * 60)
    print("16. 类中方法示例：ConfigManager")
    print("=" * 60)
    config_mgr = ConfigManager()

    host = config_mgr.get("host")
    print(f"config_mgr.get('host') = '{host}', type: {type(host).__name__}")

    port = config_mgr.get("port")
    print(f"config_mgr.get('port') = {port}, type: {type(port).__name__}")

    debug = config_mgr.get("debug")
    print(f"config_mgr.get('debug') = {debug}, type: {type(debug).__name__}")

    allowed = config_mgr.get("allowed_hosts")
    print(
        f"config_mgr.get('allowed_hosts') = {allowed}, type: {type(allowed).__name__}"
    )

    config_mgr.set("host", "example.com")
    config_mgr.set("port", 9000)
    config_mgr.set("debug", False)
    config_mgr.set("allowed_hosts", ["192.168.1.1", "example.com"])
    print("\nAfter config_mgr.set(...)...")
    print(f"config_mgr.get('host') = '{config_mgr.get('host')}'")
    print(f"config_mgr.get('port') = {config_mgr.get('port')}")
    print(f"config_mgr.get('debug') = {config_mgr.get('debug')}")
    print(f"config_mgr.get('allowed_hosts') = {config_mgr.get('allowed_hosts')}")

    print("\n" + "=" * 60)
    print("17. 类中方法示例：StringHelper")
    print("=" * 60)
    helper = StringHelper()

    # format 方法
    formatted1 = helper.format("Hello, {}!", "World")
    print(f"helper.format('Hello, {{}}!', 'World') = '{formatted1}'")

    formatted2 = helper.format("Hello, {name}!", {"name": "Python"})
    print(f"helper.format('Hello, {{name}}!', {{'name': 'Python'}}) = '{formatted2}'")

    formatted3 = helper.format("Values: {}, {}, {}", (1, 2, 3))
    print(f"helper.format('Values: {{}}, {{}}, {{}}', (1, 2, 3)) = '{formatted3}'")

    # extract 方法
    text = "Emails: alice@example.com, bob@test.com, charlie@demo.org"
    email1 = helper.extract(text, r"\b[\w.]+@[\w.]+\b", 1)
    print(
        f"\nhelper.extract(text, pattern, 1) = '{email1}', type: {type(email1).__name__}"
    )

    emails = helper.extract(text, r"\b[\w.]+@[\w.]+\b", 3)
    print(f"helper.extract(text, pattern, 3) = {emails}, type: {type(emails).__name__}")

    print("\n" + "=" * 60)
    print("所有示例运行完成！")
    print("=" * 60)
