# -*- coding:utf-8 -*-
import threading
import time


def plus():
    print('------子线程1开始执行--------')
    global g_num
    g_num += 50
    print(f'g_num is {g_num} ')
    print('------------子线程1结束----------------')


def minus():
    time.sleep(1)
    print('------子线程2开始执行--------')
    global g_num
    g_num -= 50
    print(f'g_num is {g_num} ')
    print('------------子线程2结束----------------')

# 定义一个全局变量
g_num = 100

if __name__=='__main__':
    print('------主线程开始执行--------')
    print(f'g_num is {g_num} ')
    # 实例化一个线程1
    t1 = threading.Thread(target=plus)
    # 实例化线程2
    t2 = threading.Thread(target=minus)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('------主线程结束执行--------')