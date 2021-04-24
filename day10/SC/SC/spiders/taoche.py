# -*- coding: utf-8 -*-
import time
import scrapy
# from SC.items import CarItem
from SC.items import ErshoucheItem
from urllib.parse import urljoin
from scrapy_redis.spiders import RedisSpider


# class TaocheSpider(RedisSpider):
#     name = 'taoche'
#     # allowed_domains = ['taoche.com']
#     # start_urls = []
#     redis_key = 'maoyan:start_urls'
#     with open(r'E:\python\Crawler\day10\SC\city.txt', 'r') as fp:
#         city_list = fp.readlines()
#
#     with open(r'E:\python\Crawler\day10\SC\taoche1.txt', 'r') as fp:
#         pinpai_list = fp.readlines()
#     #数据去重
#     city_list = list(set(city_list))
#     pinpai_list = list(set(pinpai_list))
#
#     for city in city_list:
#         for pinpai in pinpai_list:
#             # url='https://beijing.taoche.com/brillianceauto/'
#             url = 'https://{0}.taoche.com{1}'.format(city.strip(), pinpai.strip())
#             start_urls.append(url)
#
#     # start_urls = ['https://beijing.taoche.com/audi/']
#
#     def getValueFromList(self,obj_list):
#         if len(obj_list)==0:
#             return ''
#         else:
#             return obj_list[0]
#
#     def parse(self, response):
#         total_page=response.xpath('//div[@class="paging-box the-pages"]/div/a[last()-1]/text()').extract()
#         # print(total_page)
#         total=self.getValueFromList(total_page)
#         total=int(total)if total else 0
#         for page in range(1,total+1,1):
#             # https: // beijing.taoche.com / audi /?page = 6
#             persent_page_url=response.url+'?page='+str(page)
#             print(persent_page_url)
#             yield scrapy.Request(url=persent_page_url,callback=self.list_parse)
#     def list_parse(self, response):
#
#
#     #
#         car_list=response.xpath('//ul[@class="gongge_ul"]/li')
#         for car in car_list:
#             title=car.xpath('./div[@class="gongge_main"]/a/span/text()').extract()[0]
#             href=car.xpath('./div[@class="gongge_main"]/a/@href').extract()[0]
#             full_url=urljoin(response.url,href)
#             year=car.xpath('./div[@class="gongge_main"]/p/i[1]/text()').extract()[0]
#             distance=car.xpath('./div[@class="gongge_main"]/p/i[2]/text()').extract()[0]
#             location=car.xpath('./div[@class="gongge_main"]/p/i[2]/text()').extract()[0]
#             price=car.xpath('./div[@class="gongge_main"]/div[@class="price"]/i[2]/text()').extract()[0]
#             ori_price=car.xpath('./div[@class="gongge_main"]/div[@class="price"]/i[3]/text()').extract()[0]
#             # 创建数据模型，保存数据
#             item=CarItem()
#             item['c_title']=title
#             item['c_url']=full_url
#             item['c_year']=year
#             item['c_distance']=distance
#             item['c_location']=location
#             item['c_price']=price
#             item['c_ori_price']=ori_price
#             item['c_crawl_time']=time.strftime("%Y/%m/%d  %I:%M:%S")
#             print(item)
#             #设置爬取数据为当前时间
#
#             yield scrapy.Request(url=full_url,callback=self.detail_parse,meta={'item':item})
#
#     def detail_parse(self, response):
#         # 现将item数据模型获取到
#         item=response.request.meta['item']
#         canshu_list=response.xpath('//div[@class="col-xs-6 parameter-configure-list"]/ul/li')
#         pinpai_xinghao=canshu_list[0].xpath('./span/a/text()').extract()
#         pinpai=pinpai_xinghao[0]
#         xinghao=pinpai_xinghao[1]
#         fadongji=canshu_list[2].xpath('./span/text()').extract()[0]
#         qudong=canshu_list[3].xpath('./span/text()').extract()[0]
#         # # print(qudong,'`````````````````````')
#         jibie=canshu_list[4].xpath('./span/a/text()').extract()[0]
#         pailiang=canshu_list[5].xpath('./span/a/text()').extract()[0]
#         youhao = canshu_list[6].xpath('./span/text()').extract()[0]
#         ckg = canshu_list[7].xpath('./span/text()').extract()[0]
#         cheshenglx = canshu_list[8].xpath('./span/text()').extract()[0]
#         houbeirongji = canshu_list[9].xpath('./span/text()').extract()[0]
#
#         item['pinpai']=pinpai
#         item['xinghao']=xinghao
#         item['fadongji']=fadongji
#         item['qudong']=qudong
#         item['jibie']=jibie
#         item['pailiang']=pailiang
#         item['youhao']=youhao
#         item['ckg']=ckg
#         item['cheshenglx']=cheshenglx
#         item['houbeirongji']=houbeirongji
#
#         yield item
class TaocheSpider(RedisSpider):
    name = 'TaoChe'
    redis_key = 'taoche:start_urls'



    # 求页面总页数，根据html上代码页码数的倒数第二个a标签所得
    def getValueFromList(self, obj_list):
        if not obj_list:
            print('&&&&&&&&&&&&&', len(obj_list))
            return ''
        else:
            return obj_list[0]

    # 解析数据
    def parse(self, response):
        page_list = response.xpath(r'//div[@class="paging-box the-pages"]/div/a[last() - 1]/text()').extract()
        # print(len(page_list))
        total = self.getValueFromList(page_list)
        # print('@@@@@@@@@@@', total)
        total = int(total) if total else 0
        for page in range(1, total + 1, 1):
            # print('444444444444444')
            page_url = response.url + '?page=' + str(page)
            # print('3333333333333333333')
            yield scrapy.Request(url=page_url, callback=self.list_parse)

    def list_parse(self, response):
        # print('222222222222222222222')
        li_list = response.xpath(r'//ul[@class="gongge_ul"]/li')
        # 每一个li都是一个车的数据
        for li in li_list:
            ErShouChe_Name = li.xpath(r'./div[2]/a/span/text()').extract()[0]
            detail_href = li.xpath(r'./div[2]/a/@href').extract()[0]
            ErShouChe_detail_href = urljoin(response.url, detail_href)
            ErShouChe_original_price = li.xpath(r'./div[2]/div[1]/i[3]/text()').extract()[0]
            ErShouChe_present_price = li.xpath(r'./div[2]/div[1]/i[2]/text()').extract()[0]
            ErShouChe_location = li.xpath(r'./div[2]/p[1]/i[3]/a/text()').extract()[0]
            ErShouChe_distance = li.xpath(r'./div[2]/p[1]/i[2]/text()').extract()[0]
            ErShouChe_year = li.xpath(r'./div[2]/p[1]/i[1]/text()').extract()[0]
            ErShouChe_spider_time = time.strftime('%Y-%m-%d %H:%M:%S')

            item = ErshoucheItem()
            item['ErShouChe_Name'] = ErShouChe_Name
            item['ErShouChe_detail_href'] = ErShouChe_detail_href
            item['ErShouChe_original_price'] = ErShouChe_original_price
            item['ErShouChe_present_price'] = ErShouChe_present_price
            item['ErShouChe_location'] = ErShouChe_location
            item['ErShouChe_distance'] = ErShouChe_distance
            item['ErShouChe_year'] = ErShouChe_year
            item['ErShouChe_spider_time'] = ErShouChe_spider_time

            yield scrapy.Request(url=ErShouChe_detail_href, callback=self.detail_parse, meta={'data': item})

    def detail_parse(self, response):
        # print('*********************111111111111111111******************')
        item = response.request.meta['data']
        # print(response.url)
        li_list = response.xpath(r'//div[@class="col-xs-6 parameter-configure-list"]/ul/li')
        # print(len(li_list))
        ErShouChe_PinPai = li_list[0].xpath(r'./span/a/text()').extract()[0]                             # 车的品牌
        print('11')
        ErShouChe_XingHao = li_list[0].xpath(r'./span/a/text()').extract()[1]                          # 车的型号
        # print('22222222222')
        ErShouChe_FaDong = li_list[2].xpath(r'./span/text()').extract()[0]                          # 车发动机
        # print('333333333333')
        ErShouChe_QuDong = li_list[3].xpath(r'./span/text()').extract()[0]                          # 车的驱动
        # print('444444444444444')
        ErShouChe_JiBie = li_list[4].xpath(r'./span/a/text()').extract()[0]                         # 车辆级别
        # print('5555555555555')
        ErShouChe_PaiLiang = li_list[5].xpath(r'./span/a/text()').extract()[0]                      # 车的排量
        # print('66666666666')
        ErShouChe_YouHao = li_list[6].xpath(r'./span/text()').extract()[0]                          # 车的油耗
        # print('777777777777')
        ErShouChe_CKG = li_list[7].xpath(r'./span/text()').extract()[0]                             # 车长宽高
        # print('8888888888')
        ErShouChe_CSLX = li_list[8].xpath(r'./span/text()').extract()[0]                            # 车身类型
        # print('9999999999')
        ErShouChe_HBX = li_list[9].xpath(r'./span/text()').extract()[0]                             # 车后备箱

        # 数据模型赋值
        item['ErShouChe_PinPai'] = ErShouChe_PinPai
        item['ErShouChe_XingHao'] = ErShouChe_XingHao
        item['ErShouChe_PaiLiang'] = ErShouChe_PaiLiang
        item['ErShouChe_YouHao'] = ErShouChe_YouHao
        item['ErShouChe_FaDong'] = ErShouChe_FaDong
        item['ErShouChe_QuDong'] = ErShouChe_QuDong
        item['ErShouChe_JiBie'] = ErShouChe_JiBie
        item['ErShouChe_CKG'] = ErShouChe_CKG
        item['ErShouChe_CSLX'] = ErShouChe_CSLX
        item['ErShouChe_HBX'] = ErShouChe_HBX
        item['IP']='10.10.14.241'
        item['Name']='毛志文'



        yield item