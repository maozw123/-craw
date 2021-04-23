'''
去哪儿景点数据
北京：
数据：图片url、名称、星级、热度、门票价格、月销量、地址、简介、坐标（选做）
'''
import json
import requests
from lxml import etree
for page in range(1,51,1):
    url='https://piao.qunar.com/ticket/list_%E5%8C%97%E4%BA%AC.html?keyword=%E5%8C%97%E4%BA%AC&page={0}#from=home_remen&in_track=qunar_djmp_gnmdd_%E5%8C%97%E4%BA%AC'.format(page)
    # https://piao.qunar.com/ticket/list_%E5%8C%97%E4%BA%AC.html?keyword=%E5%8C%97%E4%BA%AC&page=6#from=home_remen&in_track=qunar_djmp_gnmdd_%E5%8C%97%E4%BA%AC
    # https://piao.qunar.com/ticket/list_%E5%8C%97%E4%BA%AC.html?keyword=%E5%8C%97%E4%BA%AC&page=4#from=home_remen&in_track=qunar_djmp_gnmdd_%E5%8C%97%E4%BA%AC
    response=requests.get(url)
    content=response.content.decode('utf-8')
    # with open('where1.html','w',encoding='utf-8') as fp :
    #     fp.write(content)
    tree=etree.HTML(content)
    # 景点名字
    name_list=tree.xpath('//a[@class="name"]/text()')
    # print(name_list)
    # # 图片url
    images_url_list=tree.xpath('//img[@class="img_opacity load"]/@data-original')

    # # 热度
    hot_list=tree.xpath('//span[@class="product_star_level"]/em/@title')
    print(hot_list)
    # # 门票价格
    ticket_price_list=tree.xpath('//span[@class="sight_item_price"]/em/text()')
    # # 月销量
    monthly_count_list=tree.xpath('//td[@class="sight_item_sold-num"]/span/text()')
    # print(monthly_count_list)
    data={}
    for i in range(15):
        data['景点名称']=name_list[i]
        data['图片url']=images_url_list[i]
        data['热度']=hot_list[i]
        data['热度热度']=ticket_price_list[i]
        data['月销量']=monthly_count_list[i]
        data_str = json.dumps(data, ensure_ascii=False)
        with open('where1-150v2.0txt', 'a', encoding='utf-8')as fp:
            fp.write(data_str + '\n')