import random
import threading
import time


def do_something(num):
    global results
    lock.acquire() # 加锁
    print(f'线程{num}------启动')
    time.sleep(random.randint(1,10))
    results.append(num)
    print(f'线程{num}------结束')
    lock.release() # 解锁


if __name__ == '__main__':
    start = time.perf_counter()

    lock = threading.Lock() # 定义锁
    list_thread = []

    # 定义一个操作的数据集合
    results = []

    for i in range(10):
        thread = threading.Thread(target=do_something, args=[i + 1])
        list_thread.append(thread)
        thread.start()

    # 将主进程挂起，让子线程运行完
    for thread in list_thread:
        thread.join()

    finish = time.perf_counter()
    print(f'线程运行时间长：{round(finish - start, 2)}')
    print(f'操作的数据集合结果：{results}')



