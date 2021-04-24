# # -*- coding: utf-8 -*-
import scrapy
import re,json
#
#
# class ZhSpider(scrapy.Spider):
#     name = 'zh'
#     allowed_domains = ['zhihu.com']
#     # start_urls = ['https://www.zhihu.com/question/353007860/answer/877455889']
#     # 爬取张佳炜公众号的详情
#     start_urls = ['https://www.zhihu.com/people/zhang-jia-wei/following']
#
#     def parse(self, response):
#         print(response.statu_code)
#         with open('zjw.html','w',encoding='utf-8') as fp:
#             fp.write(response.text)

class ZhihuSpider(scrapy.Spider):
    name = 'Zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['https://www.zhihu.com/people/zhang-jia-wei/following']
    # start_urls = ['https://www.zhihu.com/hot']

    def parse(self, response):
        all_data = response.body_as_unicode()
        print(all_data)
        with open('热榜.html', 'w', encoding='utf-8') as fp:
                fp.write(response.text)
 # 起始位置
 #    def start_requests(self):
 #        for url in self.start_urls:
 #            print(url.format("zhang-jia-wei"))
            # yield scrapy.Request(url.format("zhang-jia-wei"), callback=self.parse)

 #    def parse(self, response):
 #
 #        print("正在获取 {} 信息".format(response.url))
 #        all_data = response.body_as_unicode()
 #
 #        select = Selector(response)
 #
 #        # 所有知乎用户都具备的信息
 #        username = select.xpath("//span[@class='ProfileHeader-name']/text()").extract_first()       # 获取用户昵称
 #        sex = select.xpath("//div[@class='ProfileHeader-iconWrapper']/svg/@class").extract()
 #        if len(sex) > 0:
 #            sex = 1 if str(sex[0]).find("male") else 0
 #        else:
 #            sex = -1
 #        answers = select.xpath("//li[@aria-controls='Profile-answers']/a/span/text()").extract_first()
 #        asks = select.xpath("//li[@aria-controls='Profile-asks']/a/span/text()").extract_first()
 #        posts = select.xpath("//li[@aria-controls='Profile-posts']/a/span/text()").extract_first()
 #        columns = select.xpath("//li[@aria-controls='Profile-columns']/a/span/text()").extract_first()
 #        pins = select.xpath("//li[@aria-controls='Profile-pins']/a/span/text()").extract_first()
 #        # 用户有可能设置了隐私，必须登录之后看到，或者记录cookie！
 #        follwers = select.xpath("//strong[@class='NumberBoard-itemValue']/@title").extract()
 #
 #        item = ZhihuItem()
 #        item["username"] = username
 #        item["sex"] = sex
 #        item["answers"] = answers
 #        item["asks"] = asks
 #        item["posts"] = posts
 #        item["columns"] = columns
 #        item["pins"] = pins
 #        item["follwering"] = follwers[0] if len(follwers) > 0 else 0
 #        item["follwers"] = follwers[1] if len(follwers) > 0 else 0
 #
 #        yield item
 #
 #        # 获取第一页关注者列表
 #        pattern = re.compile('<script id=\"js-initialData\" type=\"text/json\">(.*?)<\/script>')
 #        json_data = pattern.search(all_data).group(1)
 #        if json_data:
 #            users = json.loads(json_data)["initialState"]["entities"]["users"]
 #        for user in users:
 #            yield scrapy.Request(self.start_urls[0].format(user),callback=self.parse, dont_filter=False)
