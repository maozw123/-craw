# 改文件主要用于将任务加到redis数据库中
from redis import Redis

# import requests
# from lxml import etree

with open("E:\python\Crawler\day10\SC\city2.txt", "r", encoding="utf-8") as fp:
    all_city = fp.read()
citys = list(set(all_city.strip().split("\n")))

with open("E:\python\Crawler\day10\SC\PinPai2.txt", "r", encoding="utf-8") as fp:
    all_pinpai = fp.read()
pinpais = list(set(all_pinpai.strip().split("\n")))

# 创建一个redis对象
r = Redis()
count=0
for city in citys:
    for pinpai in pinpais:
        url = "https://{0}.taoche.com/{1}/".format(city, pinpai)
        r.lpush('taoche:start_urls', url)
        print(url)
        count+=1
r.set('total_task',count)
        # response = requests.get(url)
        # content = response.text
        # try:
        #     tree = etree.HTML(content)
        # except:
        #     print(url)
        #     exit()
        # page = tree.xpath('//div[@class="paging-box the-pages"]/div/a[last()-1]/text()')
        # if page:
        #     for i in range(1, int(page[0]) + 1):
        #         new_url = url + "?page={0}".format(str(i))
        #         # r.lpush('taoche:start_url', new_url)
        #         print(new_url)
        # else:
        #     # r.lpush('taoche:start_url', url)
        #     print(url)
