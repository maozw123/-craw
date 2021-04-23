#爬取梨视频首页前五个视频
import requests
import json
from lxml import etree
from urllib.parse import urljoin
url='https://www.pearvideo.com/'
response=requests.get(url)
content=response.content.decode('utf-8')
# with open('lishipin.html','w',encoding='utf-8') as fp :
#     fp.write(content)
tree=etree.HTML(content)
#视频名称
video_name_list=tree.xpath('//div[@class="vervideo-name"]/text()')
# 视频链接
video_href_list=tree.xpath('//a[@class="actwapslide-link"]/@href')
# print(video_href_list)
# print(video_name_list)
# https://www.pearvideo.com/video_1613606
data={}
for i in range(5):
    data['视频名称']=video_name_list[i]
    # data['视频链接']='https://www.pearvideo.com/'+video_href_list[i]
    data['视频链接']=urljoin(url,video_href_list[i])
    print(data['视频链接'])
    data_str = json.dumps(data, ensure_ascii=False)
    with open('lishipin.txt', 'a', encoding='utf-8')as fp:
        fp.write(data_str+'\n')