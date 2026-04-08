# Python Advance 项目集合

本仓库包含多个 Python 高级用法与示例项目，涵盖生成器、装饰器、枚举、上下文管理器、类型注解、日志、mock、枚举、IO、迭代器等主题，适合进阶学习和参考,持续更新中。

## 目录结构

### 核心编程概念
| 目录 | 描述 |
|------|------|
| `aio/` | 异步编程相关示例 |
| `assignment_expressions/` | 赋值表达式 (海象运算符) 示例 |
| `ast/` | 抽象语法树相关 |
| `class_decorator/` | 类装饰器用法 |
| `codewisperer/` | 代码智能提示相关 |
| `comprehensions/` | 推导式用法 (列表/字典/集合推导) |
| `context_manager_demo/` | 上下文管理器示例 |
| `decorator_overload/` | **[新增]** Python 类型注解高级教程 (@overload/TypeVar/Literal/Final) |
| `decorator_property_setter_getter/` | 属性装饰器 (@property/@setter/@getter) 用法 |
| `decorator_staticmethod/` | 静态方法装饰器 |
| `descriptor/` | 描述符协议示例 |
| `dict_usage/` | 字典 10 个常用内置方法 |
| `enum_demo/` | 枚举类型用法 |
| `feishu_sdk_starter/` | 飞书 SDK 网页应用免登示例 |
| `function_annotations/` | **[新增]** 函数类型注解，演示参数和返回值的类型标注 |
| `function_overloading/` | 单分派实现函数重载 |
| `generator/` | 生成器用法 |
| `generic_demo/` | 泛型用法 |
| `global_nonlocal/` | global 与 nonlocal 作用域 |
| `importlib_module/` | 动态导入模块 |
| `io_StringIO/` | 字符串 IO 操作 |
| `iterator/` | 迭代器协议 |
| `itertools_demo/` | itertools 模块用法 |
| `lambda_usage/` | lambda 表达式 |
| `logging_demo/` | logging 标准库日志用法 |
| `loguru_example/` | loguru 第三方日志库用法 |
| `match_case/` | 模式匹配 (Python 3.10+) |
| `math/` | 数学相关 |
| `math_to_shape/` | 数学与图形可视化 |
| `mockdemo/` | mock 测试用法 |
| `mutable/` | 可变对象示例 |
| `myproj/` | 个人项目示例 |
| `mypy_generic/` | mypy 类型检查与泛型 |

### 数据结构与集合
| 目录 | 描述 |
|------|------|
| `collections/` | **[新增]** Counter 模块示例，基本用法和算术操作 |
| `tuple_usage/` | **[新增]** 长度固定元组实现 |

### 类型系统
| 目录 | 描述 |
|------|------|
| `type_annotations/` | 高级类型注解系统 |
| `typeclass/` | TypeClass 类型类模式 |
| `noneVsNoneType/` | None 与 NoneType 区别 |

### IO 与文件
| 目录 | 描述 |
|------|------|
| `pathlib_demo/` | pathlib 路径操作 |
| `getpass_demo/` | getpass 密码输入演示 |
| `secrets/` | **[新增]** secrets 安全随机数生成 |

### 设计模式与架构
| 目录 | 描述 |
|------|------|
| `dependency_injection/` | **[新增]** 依赖注入实现数据管道，Excel→JSON 导出 |

### 网络 & 数据库
| 目录 | 描述 |
|------|------|
| `requests_demo/` | HTTP 请求库示例 |
| `redis_starter/` | Redis 入门 |
| `mysql_dev/` | MySQL 开发 |

### 自动化测试
| 目录 | 描述 |
|------|------|
| `selenium4/` | Selenium 浏览器自动化 |
| `playwright_demo/` | Playwright 浏览器自动化 |

### 系统 & 工具
| 目录 | 描述 |
|------|------|
| `process/` | 进程管理 |
| `notification/` | Windows 通知消息 |
| `zmail/` | ZMail 邮件处理 |
| `sympy_math/` | SymPy 符号数学 |

## 最近更新

根据 git 提交记录：

| 提交信息 | 新增内容 |
|----------|----------|
| `docs: 添加 Python 类型注解高级教程文档和示例代码` | `decorator_overload/` — @overload/TypeVar/Literal/Final 完整教程 + README 文档 |
| `feat: 添加函数注解(type annotations)示例代码` | `function_annotations/` — 参数和返回值类型标注 |
| `feat: 添加PEP695类型参数语法示例` | Python 3.12+ 泛型类/函数新语法 |
| `feat: 使用依赖注入实现数据管道` | `dependency_injection/` — Excel 加载 → JSON 导出 |
| `feat: 添加Counter模块示例代码` | `collections/` — Counter 基本用法和算术操作 |
| `feat: 添加secrets安全随机数生成演示` | `secrets/` — 密码学安全随机数 |

## 运行环境

- **Python**: 推荐 3.10+（部分特性需 3.12+）
- **IDE**: 推荐使用 [Visual Studio Code](https://code.visualstudio.com/) 进行开发和调试

## 快速开始

```bash
git clone https://github.com/jeffsui/python_advance.git
cd python_advance
python decorator_overload/__main__.py   # 运行类型注解示例
```

## 示例：飞书网页应用免登

详细参考 [feishu_sdk_starter/server/web_app_with_auth/python/README.zh.md](feishu_sdk_starter/server/web_app_with_auth/python/README.zh.md)。

## 贡献

欢迎提交 PR 和 Issue！
