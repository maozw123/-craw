import requests
import json


with open('E:\python\Crawler\爬虫练习\JD\jdurl2.txt','r',encoding='utf-8') as fp:
    detail=fp.readlines()
    for i in detail:
        url=i.strip()
        # print(url)
        a=requests.get(url).json()
        # 获取原价
        print(a[0]['op'])
        # 获取现价
        print(a[0]['p'])