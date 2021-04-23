
#需求：把网易云音乐所有歌手信息爬取下来

import requests
from lxml import etree
import json

#网络访问
def request_url(url):

    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
    }

    content = requests.get(url,headers=headers).content.decode('utf-8')

    tree = etree.HTML(content)

    return tree



#数据解析
def parser_tree(tree):
    data = {}

    #分组歌手
    href_list = tree.xpath('//div[@class="blk"]/ul/li/a/@href')
    print(href_list)

    #爬取每一个分组的歌手---二级页
    for href in href_list:
        #每个组的歌手列表
        singer_list = []

        new_url = 'https://music.163.com'+href
        print(new_url)

        #网络请求
        sub_tree = request_url(new_url)
        #类型
        singer_type = sub_tree.xpath('//h3/span[@class="f-ff2 d-flag"]/text()')[0]

        #歌手名
        # singer_name_list = sub_tree.xpath('//ul[@id="m-artist-box"]/li/p/a[@class="nm nm-icn f-thide s-fc0"]/text() | //ul[@id="m-artist-box"]/li[@class="sml"]/a[@class="nm nm-icn f-thide s-fc0"]/text()')
        #
        # #链接
        # singer_href_list = sub_tree.xpath('//ul[@id="m-artist-box"]/li/p/a[@class="nm nm-icn f-thide s-fc0"]/@href | //ul[@id="m-artist-box"]/li[@class="sml"]/a[@class="nm nm-icn f-thide s-fc0"]/@href')
        # print(singer_href_list)
        #有可能造成数据不对应，数据混乱，解决方法
        a_list = sub_tree.xpath('//ul[@id="m-artist-box"]/li/p/a[@class="nm nm-icn f-thide s-fc0"] | //ul[@id="m-artist-box"]/li[@class="sml"]/a[@class="nm nm-icn f-thide s-fc0"]')

        for a in a_list:
            #每个歌手
            singer = {}

            name = a.xpath('./text()')[0]
            href = a.xpath('./@href')[0]
            full_href = 'https://music.163.com{0}'.format(href.strip())
            singer['name'] = name
            singer['href'] = full_href
            singer_list.append(singer)

        data[singer_type] = singer_list

    return data


if __name__ == '__main__':
    #歌手的入口地址
    url = 'https://music.163.com/discover/artist'
    tree = request_url(url)
    data = parser_tree(tree)

    data_str = json.dumps(data)

    with open('singers.txt','w',encoding='utf-8') as fp:
        fp.write(data_str)
    for k,v in data.items():
        print(k,v)


