from typing import Any

#############################
# 使用isinstance对比用单分派的版本
# 减少了多个if判断
# 更加关注函数的实现方式不同
#############################

def func(arg:Any,verbose=False):
    if isinstance(arg, int):
        if verbose:
            print(f'Here\'s your number: {arg}')
            return
        print('Number:', arg)
    elif isinstance(arg, str):
        if verbose:
            print(f'Herel\'s your text: {arg}')
            return
        print('Text:', arg)
    else:
        if verbose:
            print(f'Displaying: {arg}')
            print(arg)

