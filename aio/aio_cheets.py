import time
import asyncio
"""
async 关键字decorator 定义一个协程函数, 该函数可以被 asyncio.create_task() 创建一个协程对象, 并加入到事件循环中执行。

asyncio.sleep() 是一个协程函数, 它会暂停当前协程的执行, 并等待指定的时间, 之后再恢复执行。

await 关键字可以让当前协程暂停, 等待另一个协程的执行结果, 之后再恢复执行。

asyncio.run() 是一个函数, 它会运行一个协程对象, 并阻塞当前线程, 直到协程执行完毕。

event——loop 是一个事件循环, 它会管理协程的执行, 并在适当的时候切换到其他协程执行。
asyncio 模块提供了一系列的工具, 用于处理异步IO,
包括文件I/O, 网络I/O, 子进程, 线程, 锁, 条件变量等。

"""

async def play():
    print("enter play")
    for _ in range(5):
        # time.sleep(1) #模拟等待过程(IO同步操作)
        await asyncio.sleep(1) #模拟等待过程(IO异步操作)
        for _ in range(1000): #模拟 下一步落子过程(CPU运算)
            pass

async def main():
    print("enter main")
    start = time.time()
    tasks = []
    for _ in range(10):
        play_coro = play()
        tasks.append(asyncio.create_task(play_coro))
    for t in tasks:
        await t
    print(f"Time taken: {time.time() - start} seconds")


main_coroutine = main()
# print(main_coroutine)
asyncio.run(main_coroutine) # 运行协程,耗时5秒
