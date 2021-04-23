
import requests
from lxml import etree
url='https://voice.hupu.com/nba'
# headers={
#     'Cookie':'iciba_u_rand=44305e1e0627367024adc003b8ada5fa%4027.155.93.84; iciba_u_rand_t=1571223991; UM_distinctid=16dd43f748d9c-05fb566fc698fc-5b123211-100200-16dd43f748e65b; CNZZDATA1256573702=676068009-1571222282-http%253A%252F%252Fwww.iciba.com%252F%7C1571222282; __gads=ID=ea1a05b3f9d41ffa:T=1571224085:S=ALNI_MbFtcQOljdarDQbBK_i3qSMVqFa8w',
#     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
# }
response=requests.get(url)
content=response.content.decode('utf-8')

with open('hupunba.html','w',encoding='utf-8') as fp:
    fp.write(content)

tree=etree.HTML(content)
#标题
li_list=tree.xpath('//div[@class="list-hd"]/h4/a/text()')
#发布时间
time_list=tree.xpath('//span[@class="other-left"]/a/text()')
#出版社
perss_list=tree.xpath('//span[@class="comeFrom"]/a/text()')
#路径
herf_list=tree.xpath('//div[@class="list-hd"]/h4/a/@href')
# print(herf_list)
# for i in range(60):
#     news=str(i+1)+li_list[i]+'   '+time_list[i]+'   '+perss_list[i]+'  '+herf_list[i]+'\n'
#     print(news)
#     with open('hupuNBA.txt','a',encoding='utf-8') as fb:
#         fb.write(news)
# print(li_list)
# print(time_list)
# print(len(li_list))

for herf in herf_list:
    print(herf)
    response=requests.get(herf)
    content = response.content.decode('utf-8')
    tree=etree.HTML(content)

    a=tree.xpath('//div[@class="artical-main-content"]/p/text()')
    # print(a)
    for i in a:
        with open('hupuNBA23.txt', 'a', encoding='utf-8') as fb:
            fb.write(i)
