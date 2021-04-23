import time
import requests
import threading
from lxml import etree
from queue import Queue
from urllib.parse import urljoin

#爬取数据
def get_content(page_queue,t_name):
    while True:
        if page_queue.empty():
            print('队列为空，可以退出',t_name)
            break
        try:
            page=page_queue.get(block=False)
            #page_queue.get()如果队列为空，表示取不到，取不到就等待----阻塞
            #如果想在队列为空时get()不阻塞，加参数，block=Flase
            print(t_name,'取到了任务：',page)
            pn = (page - 1) * 50
            url='http://tieba.baidu.com/f?kw=%E4%B8%AD%E5%9B%BD&ie=utf-8&pn='+str(pn)
            headers = {'user-agent': 'saffafaa'}
            content = requests.get(url, headers=headers).content.decode('utf-8')
            print('当前爬取到第%d页'%(page))
            # with open('第%d页.html'%(page),'w',encoding='utf-8') as fp:
            #     fp.write(content)
            parser_content(content, url, t_name,page)
        except:
            print(t_name,'没取到，有异常')
 #解析


#解析数据
def parser_content(content,url,t_name,page):
    tree = etree.HTML(content)
    li_list = tree.xpath('//li[@class=" j_thread_list clearfix"]')
    for li in li_list:
        title = li.xpath('.//a[@class="j_th_tit "]/text()')
        href = li.xpath('.//a[@class="j_th_tit "]/@href')

        # full_href = 'http://tieba.baidu.com'+href[0]
        full_href = urljoin(url,href[0])
        info = title[0]+','+full_href+'\n'

        flag=lock.acquire()
        if flag:
        #保存---持久化/序列化
            with open('tieba.txt','a',encoding='utf-8') as fp:
                fp.write(info)
            #完成后释放锁
            lock.release()

    #     print(title,full_href)
    # print(len(li_list))
    print(t_name,'完成了任务：',page)
# 加锁
lock=threading.Lock()
# 用来创建一个锁对象

if __name__ == '__main__':
    start_time=time.time()
    q=Queue()
    for page in range(1,100):
        q.put(page)
    t_list=[]
    for i in range(1,4):
        t_name='线程%d'%(i)
        t=threading.Thread(target=get_content,args=(q,t_name))
        t.start()
        t_list.append(t)
    for t in t_list:
        t.join()
    end_time=time.time()
    print('时间差', end_time -start_time)
