# import time
# def work():
#     for i in range(1,10):
#         print('程序执行第%s次'%(i))
#         yield i
# x=work()
# # print(next(x))
# # print(next(x))
# # print(next(x))
# for a in x:
#     time.sleep(1)
#     print(a)


def ha1():
    for i in range(10):
        print('我是函数1',i)
        yield i
def ha2(a):
    for i in range(10):
        print('我是函数2',i)
        next(a)
a=ha1()
ha2(a)