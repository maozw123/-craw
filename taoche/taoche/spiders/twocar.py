# -*- coding: utf-8 -*-
import scrapy


class TwocarSpider(scrapy.Spider):
    name = 'twocar'
    allowed_domains = ['taoche.com']
    start_urls = ['http://taoche.com/']

    def parse(self, response):
        pass
