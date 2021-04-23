import requests
from lxml import etree

url='https://www.biqugecom.com/0/15/32748551.html'

content=requests.get(url).content.decode('gbk')
with open('biqugexiaoshuo.html','w',encoding='gbk') as fp:
    fp.write(content)