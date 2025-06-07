from multiprocessing import Process
import os,time

def worker(second):
    print("线程  {} Start Sleep {} seconds".format(os.getpid(), second))
    # os.system("ping 127.0.0.1")
    time.sleep(second)
    print("线程 {} Sleep End".format(os.getpid()))

if __name__ == '__main__':
    for i in range(5):
        p = Process(target=worker, args=(i,))
        p.start()
