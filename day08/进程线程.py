from multiprocessing import Process, Queue
from threading import Thread
import queue, time


# 线程A1
def xcA1(xcq):
    a = [1, 2, 3, 4, 5, 6]
    for element in a:
        xcq.put(element)
        print('进程A的线程1发送数据', element)
        time.sleep(1)


# 线程A2
def xcA2(xcq,jcq):
    while True:
        try:
            element = xcq.get(timeout=2)
            jcq.put(element)
        except:
            break


# 线程B1
def xcB1(xcq):
    while True:
        try:
            element = xcq.get(timeout=2)
            print('进程B的线程1接收数据', element)
        except:
            break


# 线程B2
def xcB2(jcq, xcq):
    while True:
        try:
            element = jcq.get(timeout=2)
            xcq.put(element)
        except:
            break

# 进程A
def jcA(jcq):
    print('进程A启动')
    xcq = queue.Queue(3)
    aT1 = Thread(target=xcA1, args=(xcq,))
    aT2 = Thread(target=xcA2, args=(xcq,jcq))
    # aT2 = Thread(target=xcA2, args=(jcq,xcq))
    aT1.start()
    aT2.start()
    aT1.join()
    aT2.join()

# 进程B
def jcB(jcq):
    print('进程B启动')
    xcq = queue.Queue(3)
    aTB1 = Thread(target=xcB1, args=(xcq,))
    aTB2 = Thread(target=xcB2, args=(jcq,xcq))
    aTB1.start()
    aTB2.start()
    aTB1.join()
    aTB2.join()

if __name__ == '__main__':
    jcq = Queue(3)
    j1 = Process(target=jcA, args=(jcq,))
    j2 = Process(target=jcB, args=(jcq,))
    j1.start()
    j2.start()
