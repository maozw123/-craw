import requests
from lxml import etree
import re
from urllib.parse import urljoin

url='https://beijing.taoche.com/all/'
headers={
    'user-agent':'sasdafa'
}
response=requests.get(url,headers=headers)
content=response.content.decode('utf-8')

# with open('taoche.html','w',encoding='utf-8') as fp:
#     fp.write(content)

tree=etree.HTML(content)
city_href_list=tree.xpath('//div[@class="header-city-province-text"]/a/@href')
print(city_href_list)
for city in city_href_list:

    pattern=re.compile(r'//(.*?)\.')
    result=pattern.findall(city)
    print(result)

    with open('city.txt', 'a', encoding='utf-8') as fp:
        fp.write(result[0]+'\n')



