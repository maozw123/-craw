# -*- coding: utf-8 -*-
import scrapy


class NbaSpider(scrapy.Spider):
    name = 'nba'
    allowed_domains = ['hupu.com']
    start_urls = ['https://voice.hupu.com/nba/1']

    def parse(self, response):
        # with open('hupunba1.html','w',encoding='utf-8')as fp:
        #     fp.write(response.text)
        li_list=response.xpath('//div[@class="news-list"]/ul/li')
        for li in li_list:
            href=li.xpath('./div[@class="list-hd"]/h4/a/@href').extract()[0]
            title=li.xpath('./div[@class="list-hd"]/h4/a/text()').extract()[0].strip()
            print(href)
            print(title)

            yield scrapy.Request(url=href,callback=self.detail_parse)

    def detail_parse(self, response):
        src=response.xpath('//div[@class="artical-importantPic"]/img/@src').extract()[0]
        print('src', src)
        p_list=response.xpath('//div[@class="artical-main-content"]/p')
        for p in p_list:
            a=p.xpath('./span/text()')
            print(a)

