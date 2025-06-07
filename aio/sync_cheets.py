import time


def play():
    print("enter play")
    for _ in range(5):
        time.sleep(1) #模拟等待过程(IO同步操作)
        for _ in range(1000): #模拟 下一步落子过程(CPU运算)
            pass

def main():
    print("enter main")
    start = time.time()
    for _ in range(10):
        play()
    print(f"Time taken: {time.time() - start} seconds")


main() # 执行main函数,函数耗时50秒以上