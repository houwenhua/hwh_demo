import threading
import time


start = time.perf_counter()

def do_something(num):
    print(f'线程{num}------启动')
    time.sleep(num)
    print(f'线程{num}------结束')

thread1 = threading.Thread(target=do_something,args=[1])
thread2 = threading.Thread(target=do_something,args=[2])

thread1.start()
thread2.start()

# 将主进程挂起，让子线程运行完
thread1.join()
thread2.join()

finish = time.perf_counter()

print(f'线程运行时间长：{round(finish-start,2)}')