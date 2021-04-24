# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urljoin
import json
import requests
from ..items import JdItem


# '''
# https://list.jd.com/list.html?cat=9987,653,655
# # 华为手机
# https://list.jd.com/list.html?cat=9987,653,655&ev=exbrand%5F8557&sort=sort_rank_asc&trans=1&JL=3_%E5%93%81%E7%89%8C_%E5%8D%8E%E4%B8%BA%EF%BC%88HUAWEI%EF%BC%89#J_crumbsBar
#
#
# '''
class JdSpider(scrapy.Spider):
    name = 'jd'
    # allowed_domains = ['jd.com']
    start_urls = [
        'https://list.jd.com/list.html?cat=9987,653,655&ev=exbrand%5F8557&sort=sort_rank_asc&trans=1&JL=3_%E5%93%81%E7%89%8C_%E5%8D%8E%E4%B8%BA%EF%BC%88HUAWEI%EF%BC%89#J_crumbsBar']

    def parse(self, response):
        # with open('jdhuawei01.html','w',encoding='utf-8') as fp:
        #     fp.write(response.text)
        li_list = response.xpath('//li[@class="gl-item"]')
        # print(li_list)
        # print(len(li_list))
        for li in li_list:
            # 获取标题
            title = li.xpath('./div/div[@class="p-name"]/a/em/text()').extract()[0].strip()
            print(title)
            # 获取详情页url
            href = li.xpath('./div/div/a/@href').extract()[0]
            detail_url = urljoin(response.url, href)
            # print(detail_url)
            # 商品id
            spid = li.xpath('./div/@data-sku').extract()[0]
            # print(id)
            # 获取json数据的url
            price_url = 'https://p.3.cn/prices/mgets?skuIds=J_' + spid
            print(price_url)
            # with open('jdurl2.txt','a',encoding='utf-8') as fp:
            #     fp.write(price_url+'\n')
            a = requests.get(price_url).json()
            #         # 获取原价
            y_price = a[0]['op']
            print(y_price)
            #         # 获取现价
            x_price = a[0]['p']
            print(x_price)
            item = JdItem()
            item['title']=title
            item['detail_url'] = detail_url
            item['price_url'] = price_url
            item['x_price'] = x_price
            item['y_price'] = y_price
            item['spid'] = spid
            yield item

            # with open('E:\python\Crawler\爬虫练习\JD\jdurl2.txt', 'r', encoding='utf-8') as fp:
            #     detail = fp.readlines()
            #     for i in detail:
            #         url = i.strip()
            #         print(url)
            #         a = requests.get(url).json()
            #         # 获取原价
            #         print(a[0]['op'])
            #         # 获取现价
            #         print(a[0]['p'])

            # yield scrapy.Request(url=detail_url, callback=self.detail_parse,dont_filter=False)
            # 二级页跳转到京东外面的url，
    #         yield scrapy.Request(url=price_url, callback=self.detail_parse,dont_filter=False)
    #
    # def detail_parse(self, response):
    #     pr=response.text
    #     print(pr)
    #     print('1111111111')


'''
https://cd.jd.com/promotion/v2?callback=jQuery9729939&skuId=100003688077&area=1_72_2799_0&shopId=1000000157&venderId=1000000157&cat=670%2C671%2C1105
https://cd.jd.com/promotion/v2?callback=jQuery874755&skuId=100003150683&area=1_72_2799_0&shopId=1000000157&venderId=1000000157&cat=670%2C671%2C1105
https://cd.jd.com/promotion/v2?callback=jQuery6999029&skuId=100008535982&area=1_72_2799_0&shopId=1000000157&venderId=1000000157&cat=670%2C671%2C672

'''
