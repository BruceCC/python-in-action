# -*- coding:utf-8 -*-
import threading
import time


class SubThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            # name属性中保存的是当前线程的名字
            msg = f'子线程{self.name}执行，i={i}\n'
            print(msg)


if __name__ == '__main__':
    print('--------主线程开始执行---------')
    t1 = SubThread()
    t2 = SubThread()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('--------主线程执行结束---------')
