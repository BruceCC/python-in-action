from queue import Queue
import random, threading, time


# 生产者类
class Producer(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.data = queue

    def run(self):
        for i in range(5):
            print(f'生产者{self.name}将产品{i} 加入了队列')
            self.data.put(i)
            time.sleep(random.random())
        print(f'生产者{self.name}完成')


# 消费者类
class Consumer( threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.data = queue

    def run(self):
        for i in range(5):
            val = self.data.get()
            print(f'消费者{self.name}将产品{val}从队列中取出')
            time.sleep(random.random())
        print(f'消费者{self.name}完成')


if __name__=='__main__':
    print('-------------主线程开始-------------')
    queue = Queue()
    producer = Producer('Producer', queue)
    consumer = Consumer('Consumer', queue)

    producer.start()
    consumer.start()
    producer.join()
    producer.join()
    print('-------------主线程结束-------------')

