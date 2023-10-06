# -*- coding:utf-8 -*-
import random
import threading, time


def process():
    for i in range(3):
        time.sleep(random.randint(1, 3))
        print(f'thread name is {threading.current_thread().name}')


if __name__ == '__main__':
    print('--------------主线程开始执行----------')
    # 创建4个线程，存入列表
    threads = [threading.Thread(target=process) for i in range(4)]
    for t in threads:
        # 开启线程
        t.start()
    for t in threads:
        # 等待子线程结束
        t.join()
    print('--------------主线程结束执行----------')

