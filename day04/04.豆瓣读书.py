import requests
import re
from lxml import etree
from selenium import webdriver
driver=webdriver.PhantomJS(executable_path=r'C:\Users\Administrator\Desktop\新建文件夹\phantomjs-2.1.1-windows\bin\phantomjs.exe')

url='https://search.douban.com/book/subject_search?search_text=python&cat=1001'
driver.get(url)
with open('book2.html','w',encoding='utf-8') as fp:
    fp.write(driver.page_source)
driver.save_screenshot('book.png')

#数据提取
tree=etree.HTML(driver.page_source)

#书名
title_list=tree.xpath('//div[@class="title"]/a/text()')
print(title_list)
#作者
author_list=tree.xpath('//div[@class="title"]/a/@href')
print(author_list)
#时间
time_list=tree.xpath('//div[@class="meta abstract"]/text()')
print(time_list)
#正则匹配时间和价格
for time1 in time_list:
    pattern=re.compile(r'\d+-\d+-{,1}\d{,2}')
    result=pattern.findall(time1)
    print(result)
print('-----------------')
#价格
for price in time_list:
    pattern=re.compile(r'\d{2,3}.{,1}\d{,2}元{,1}')
    result1=pattern.findall(price)
    print(result1[-1])

# headers={
#     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3732.400 QQBrowser/10.5.3819.400'
# }
#
# content=requests.get(url,headers=headers).content.decode('utf-8')
#
# with open ('book.html','w',encoding='utf-8') as fp:
#     fp.write(content)