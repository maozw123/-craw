import requests
from lxml import etree
from urllib.parse import urljoin
from model import News
from db import DBManager,RedisManager
from common import first_object,hash_item
from settings import UPDATE_RATE




# 网络访问
def request_connent(url):
    headers = {
        'user-agent': 'assdfsadsa'
    }
    response = requests.get(url, headers=headers)
    connent=response.content.decode('utf-8')
    # 调用数据解析函数，进行数据解析
    parse_connent(connent,url)
# 数据解析
def parse_connent(connent,ori_url):
    # with open('1.html','w',encoding='utf-8')as fp:
    #     fp.write(connent)
    tree=etree.HTML(connent)
    new_list=tree.xpath('//ul[@class="u-newsList01 f-mt10"]/li')
    # 创建一个数据库对象
    # 关系型数据库的操作
    # db=DBManager()
    # 非关系型数据库的操作
    rDB=RedisManager()
    for news in new_list:
        title=first_object(news.xpath('./a/text()'))
        href=first_object(news.xpath('./a/@href'))

        url=urljoin(ori_url,href)
        data_time=first_object(news.xpath('./span/text()'))
        # print(title,url,data_time)
        # 利用数据模型创建数据模型 ，给对象属性赋值
        item=News(title,url,data_time)

        # 存储数据
        # 判断数据是否为重复数据
        str_obj=item.title+item.url+item.data_time
        sign=hash_item(str_obj)
        item.sign=sign
        if item.title and item.url:

            # db.save_item(item)
            rDB.save_item(item)

if __name__ == '__main__':

    base_url = 'http://www.mofcom.gov.cn/article/ae/ai/?'
    # 第二页：：http://www.mofcom.gov.cn/article/ae/ai/?2
    # 第三页：：http://www.mofcom.gov.cn/article/ae/ai/?3
    # 第n页：：http://www.mofcom.gov.cn/article/ae/ai/?n
    # 兼容了策略一和策略二
    total=UPDATE_RATE if UPDATE_RATE else 200

    for i in range(1, total+1, 1):
        if i == 1:
            url = base_url
        else:
            url = base_url + str(i)
        print(url)
        request_connent(url)
