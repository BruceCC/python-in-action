from threading import Thread, Lock
import time

# 100张票
n = 100


def task():
    global n
    # 上锁
    mutex.acquire()
    # 赋值给临时变量
    temp = n
    time.sleep(0.1)
    n = temp - 1
    print(f'购买成功，剩余{n}张电影票')
    # 释放锁
    mutex.release()


if __name__ == '__main__':
    # 实例化lock类
    mutex = Lock()
    # 初始化列表
    t_l = []
    for i in range(101):
        # 实例化线程类
        t = Thread(target=task)
        # 将线程实例存入列表中
        t_l.append(t)
        t.start()

    for t in t_l:
        t.join()
