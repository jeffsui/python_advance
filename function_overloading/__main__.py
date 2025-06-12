from functools import singledispatch, singledispatchmethod
from typing import Any

###############################
# 单分派场景 实现函数重载
#@singledispatch 不能使用在类中
#@singledispatchmethod 可以使用在类中
################################

@singledispatch
def func(arg:Any,verbose=False):
    raise NotImplementedError(f'Type:{type(arg)}cannot be used with func()')


@func.register
def _(arg: int | float,verbose=False):
    if verbose:
        print(f"Here\'s are your text :{arg}")
        return

    print('Text:',arg)

@func.register
def _(arg:str,verbose=False):
    if verbose:
        print(f"Here\'s are your text :{arg}")
        return

    print('Text:',arg)




class Computer:
    @singledispatchmethod
    def display(self,arg:Any,verbose=False):
        if verbose:
            print(f"Displaying: {arg}")

        print(arg)

    @display.register
    def _(self,arg:str,verbose=False):
        if verbose:
            print("Here\'s your text: {arg}")
            return

        print('Text:',arg)

    @display.register(int)
    def _(self,arg,verbose=False):
        if verbose:
            print(f"Here\'s are your number :{arg}")

            return

        print('Number:',arg)




if __name__ == '__main__':
    func('Hello',verbose=True)
    func(10,verbose=True)

    # class
    com = Computer()
    com.display(10,True)
    com.display('Text',False)
    com.display(None,False)


