import threading
import time


start = time.perf_counter()

list_thread = []
def do_something(num):
    print(f'线程{num}------启动')
    time.sleep(num)
    print(f'线程{num}------结束')

for i in range(10):
    thread = threading.Thread(target=do_something,args=[i+1])
    list_thread.append(thread)
    thread.start()

# 将主进程挂起，让子线程运行完
for thread in list_thread:
    thread.join()

finish = time.perf_counter()

print(f'线程运行时间长：{round(finish-start,2)}')