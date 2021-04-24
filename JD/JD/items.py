# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JdItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field() #标题
    spid=scrapy.Field()   #id单号
    detail_url=scrapy.Field()  #详情页url---获取更多内容
    price_url=scrapy.Field()   #获取价格的url
    y_price=scrapy.Field()     #获取现价
    x_price=scrapy.Field()    #获取原价