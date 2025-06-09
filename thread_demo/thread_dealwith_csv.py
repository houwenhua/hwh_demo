import csv
import math
import threading


# 动态实现多线程处理csv文件
# 需求，将csv文件中字段zjid末尾是字母和数字分别拆分到2个csv文件中

csv_list = []
filepath = 'C:\\Users\\Administrator\\Desktop\\test.csv'
with open(filepath, 'r') as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        csv_list.append(line)


def worker(num,start,end):
    with lock:
        for line in csv_list[start:end]:
            char = line[0][-1]
            if char.isdigit():
                print(f'{threading.current_thread().name}线程--{num}---数字----' + line[0])
            else:
                print(f'{threading.current_thread().name}线程--{num}---字母----' + line[0])

def numss():
    # list集合是左闭右开的
    nums = [1,2,3,4,5,6,7,8,9,10]
    print(nums[0:3])
    print(nums[3:6])


if __name__ == '__main__':
    lock = threading.Lock()
    thread_list = []
    # 定义线程数量
    thread_num = 8
    part_size = math.ceil(len(csv_list)/thread_num)
    for i in range(thread_num):
        # 实现每个线程处理的动态分区范围
        # 开始位置，list集合是左闭右开的
        start = i * part_size
        # 结束位置
        end = start + part_size
        if end > len(csv_list):
            end = len(csv_list)
        thread = threading.Thread(target=worker,args=(i+1,start,end))
        thread.start()
        thread_list.append(thread)

    for thread in thread_list:
        thread.join()

    print("执行结束")

