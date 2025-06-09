import time


def do_something():
    print('线程------启动')
    time.sleep(1)
    print('线程------结束')

start = time.perf_counter()

do_something()
do_something()
finish = time.perf_counter()

print(f'线程运行时间长：{round(finish-start,2)}')