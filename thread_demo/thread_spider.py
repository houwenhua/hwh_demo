import threading
import time

from bs4 import BeautifulSoup
from faker import Faker
import requests
from loguru import logger

# 一个日志装饰器
def log_print(*args,**kwargs):
    def wrapper(func):
        logger.info('执行开始')
        result = func(*args,**kwargs)
        logger.info('执行结束')
        return result
    return wrapper



def spider_url(url):
    fake = Faker()
    headers = {'User-Agent':fake.user_agent()}
    r = requests.get(url,headers=headers)
    soup = BeautifulSoup(r.content,'html.parser')
    review_list = soup.find_all(class_='main review-item')

    for i in range(len(review_list)):
        title = review_list[i].select('h2>a')[0].text
        date = review_list[i].select('span')[1].text
        # user = review_list[i].select('header>a')[1].text
        print(threading.current_thread().name + '-->' + date + '----' + '333' + '---------' + title)
        # logger.info(threading.current_thread().name + '-->' + date + '----' + '333' + '---------' + title)


if __name__ == '__main__':
    start = time.perf_counter()

    url_list = [
        'https://movie.douban.com/subject/1652587/reviews?sort=hotest&start=0',
        'https://movie.douban.com/subject/1652587/reviews?sort=hotest&start=20'
         ]
    thread_list = []
    for url in url_list:
        thread = threading.Thread(target=spider_url,args=[url])
        thread.start()
        thread_list.append(thread)

    for thread in thread_list:
        thread.join()

    finish = time.perf_counter()
    print(f'线程运行时间长：{round(finish - start, 2)}')


