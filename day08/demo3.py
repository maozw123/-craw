import time
from threading import Thread

def T1():
    for i in range(10):
        print('T1',i+1)

def T2():
    for i in range(10):
        print('T2',i+1)
        time.sleep(0.5)
if __name__ == '__main__':
    a=Thread(target=T1)
    b=Thread(target=T2)
    a.start()
    b.start()
    # a.join()
    b.join()
    print('你好')