'''链家的房产数据
https://bj.fang.lianjia.com/loupan/
要求：
1.必抓：图片、楼盘名称、建筑面积、均价
2.选抓：区域、商圈、户型
将每一套楼盘放在一个字典中'''


import requests
import json
from lxml import etree
from selenium import webdriver

driver=webdriver.PhantomJS(executable_path=r'C:\Users\Administrator\Desktop\新建文件夹\phantomjs-2.1.1-windows\bin\phantomjs.exe')
for page in range(1,20,1):
    url='https://bj.fang.lianjia.com/loupan/bp0ep2000pg{0}/'.format(page)
    driver.get(url)
    # print(url)
    # with open('lianjia.html','w',encoding='utf-8') as fp:
    #     fp.write(driver.page_source)
    # driver.save_screenshot('lianjia.png')

    tree=etree.HTML(driver.page_source)
    info_list=tree.xpath('//ul[@class="resblock-list-wrapper"]')
    # print(info_list)
    for i in info_list:

    # 楼盘名
        building=tree.xpath('//div[@class="resblock-name"]/a/text()')
        # print(building)

    # 图片
        images_list=tree.xpath('//a[@class="resblock-img-wrapper "]/img[@class="lj-lazy"]/@data-original')
        # print(images_list)
        #建筑面积
        area_list=tree.xpath('//div[@class="resblock-area"]/span/text()')
        # print(area_list)
        # 均价
        # price_list=tree.xpath('//div[@class="main-price"]/span/text()')
        # print(price_list)
        data={}
        for a in range(0,10,1):
            data['建筑名称']=building[a]
            print(data)
            data['建筑图片']=images_list[a]
            # data['建筑面积']=area_list[a]
            data_str = json.dumps(data, ensure_ascii=False)
            with open('lianjia.txt', 'a', encoding='utf-8')as fp:
                fp.write(data_str+'\n')
            # json.dump(data, open('lianjia.txt', 'w', encoding='utf-8'))
            # print(data_str)


    # # a=tree.xpath('//a[@class="resblock-room"]/span/text()')
    # # print(a)
    #
    # # 保存字典中
    # building_info={}
    # # for building in building_list:
    # #     building_info=building_list["name":building]

