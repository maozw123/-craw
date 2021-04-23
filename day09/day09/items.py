# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Day09Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class JobItem(scrapy.Item):
    # define the fields for your item here like:
    company_name = scrapy.Field() #公司名字
    salary = scrapy.Field()  #职位薪资
    job_name = scrapy.Field() #职位名字
    job_url = scrapy.Field() #职位链接
