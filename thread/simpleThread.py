from multiprocessing import Process


# 执行子进程代码
def test(interval):
    print("子进程开始执行")
    print(f'interval: {interval}')
    print("子进程结束执行")


# 执行主进程
def main():
    print('主进程开始执行')
    p = Process(target=test, args=(2,))
    p.start()
    print('主进程结束执行')


if __name__ == "__main__":
    main()

