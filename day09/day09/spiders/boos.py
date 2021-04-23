# -*- coding: utf-8 -*-
import scrapy



class BoosSpider(scrapy.Spider):
    name = 'boos'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/job_detail/?query=python&']

    def parse(self, response):
        with open('boss.html','w',encoding='utf-8')as fp:
            fp.write(response.text)
