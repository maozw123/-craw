import requests
from lxml import etree
'''
上次分析接口遇到jsonp分析没结果，今天发现删除后对数据没影响
今天尝试批量爬取苏宁母婴价格
'''

# 一级页面

url='https://search.suning.com/%E5%A5%B6%E7%B2%89/?safp=d488778a.682.1.3'
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3732.400 QQBrowser/10.5.3819.400'
}

