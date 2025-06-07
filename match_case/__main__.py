"""
结构模式匹配
python3.10后的新语法
PEP 634 – Structural Pattern Matching: Specification
"""
################################
# switch case 和 match case区别
# match-case语法能做的事情远超C/Go这些语言里的switch-case，
# 它其实是Scala, Erlang等语言里面的match-case，它支持复杂的模式匹配，
# 接下来我会通过多个模式的例子详细演示这个新的语法的灵活性和pythonic。
################################

def http_error(status):
    if status == 400:
        return 'Bad request'
    elif status == 401:
        return 'Unauthorized'
    elif status == 403:
        return 'Forbidden'
    elif status == 404:
        return 'Not found'
    else:
        return 'Unknown status code'
# 此处使用 switch case语法
def http_error(status):
      match status:
        case 400:
            return 'Bad request'
        case 401:
            return 'Unauthorized'
        case 403:
            return 'Forbidden'
        case 404:
            return 'Not found'
        case _:
            return 'Unknown status code'
###################################
## Literal模式
# 如果greeting非空,就会赋值给name
# 如果greeting为空 会抛出NameError异常
###################################


def capture(greeting):
    match greeting:
        case "":
            print("Hello!")
        case name:
            print(f"Hi {name}!")
    if name == "Santa":
        print('Match')

####################################
# 序列(Sequence)模式
#
####################################
def sequnce(collection):
    match collection:
        case 1,[x, *others]:
            print(f"Got 1 and a nested sequence: {x=}, {others=}")
        case (1,x):
            print(f"Got 1 and {x}")
        case [x,y,z]:
            print(f"{x=},{y=},{z=}")

#######################################
# 通配符(Wildcard)模式
# case _
# 序列模式也支持 _
#######################################

# def http_error(status):
#     match status:
#         ... # 省略
#         case _:
#             return 'Unknown status code'

#######################################
# 恒定值(constant value)模式
# 通常匹配常量 或 enum模块的枚举值
########################################
def constant_value(color):
     match color:
         case Color.RED:
             print('Red')
         case NewColor.YELLOW:
             print('Yellow')
         case new_color:
             print(new_color)
#################################
#映射(Mapping)模式
#################################
def mapping(config):
      match config:
          case {'sub': sub_config, **rest}:
              print(f'Sub: {sub_config}')
              print(f'OTHERS: {rest}')
          case {'route': route}:
              print(f'ROUTE: {route}')
##################################
# 类(Class)模式
###################################
def class_pattern(obj):
      match obj:
          case Point(x=1, y=2):
              print(f'match')

if __name__ == '__main__':
    sequnce([1,2])
    sequnce([1, [2, 3]])
    sequnce([1, [2, 3,4]])
    sequnce((1,2))
    sequnce((1,2,3))
