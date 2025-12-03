import json
from typing import Any, Callable

"""
dependency injection: 依赖注入

依赖注入是一种设计模式，其核心思想是将依赖关系从类内部移动到外部，
通过参数传递的方式注入依赖。

"""


# define type Data
type Data = list[dict[str, Any]]


def load_data_from_csv() -> Data:
    print("load data from csv....")
    return [
        {"name": "Jack", "age": 37},
        {"name": "Mick", "age": 35},
        {"name": "Jerry", "age": 32},
    ]


def load_data_from_excel() -> Data:
    print("load data from excel....")
    return [
        {"name": "xima", "age": 19},
        {"name": "laya", "age": 20},
        {"name": "mreay", "age": 23},
    ]


def export_to_json(data: Data) -> None:
    with open("./dependency_injection/output.json", "w") as f:
        json.dump(data, f, indent=2)


def clean_data(data: Data) -> Data:
    return [row for row in data if row["age"] is not None]


# create DataPipline class
class DataPipline:
    def run(self, loader_fn: Callable[[], Data]) -> None:
        # data loader
        data = loader_fn()
        # transformation
        cleand = clean_data(data)
        # export data
        export_to_json(cleand)


def main():
    pipline = DataPipline()
    pipline.run(load_data_from_excel)
    print("Pipline completed. Output written to output.json")


if __name__ == "__main__":
    main()
