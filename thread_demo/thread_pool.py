import concurrent.futures
import threading
import time

# 线程池的使用
def thread_fun(name):
    print(f'子线程{name}:启动{threading.current_thread().name}')
    time.sleep(2)
    print(f'子线程{name}:结束{threading.current_thread().name}')

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        for i in range(10):
            pool.submit(thread_fun,i)