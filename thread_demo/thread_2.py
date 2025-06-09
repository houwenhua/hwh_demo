import threading
import time


start = time.perf_counter()

def do_something():
    print('线程------启动')
    time.sleep(1)
    print('线程------结束')

thread1 = threading.Thread(target=do_something)
thread2 = threading.Thread(target=do_something)

thread1.start()
thread2.start()

# 将主进程挂起，让子线程运行完
thread1.join()
thread2.join()


finish = time.perf_counter()

print(f'线程运行时间长：{round(finish-start,2)}')


