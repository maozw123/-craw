#自定义的中间件
from scrapy import signals
from selenium import webdriver
from scrapy.http import HtmlResponse

class BossDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        print('~~~~~~~~~~~~~~~~~~~中间件~~~~~~~~~~~~~~~~~~')
        driver=webdriver.PhantomJS(executable_path=r'C:\Users\Administrator\Desktop\新建文件夹\phantomjs-2.1.1-windows\bin\phantomjs.exe')
        driver.get(request.url)
        html=driver.page_source
        driver.save_screenshot('boss.png')
        driver.quit()
        # html = 'abcd'
        return HtmlResponse(url=request.url,encoding='utf-8',body=html,request=request)


    # def process_response(self, request, response, spider):
    #     # Called with the response returned from the downloader.
    #
    #     # Must either;
    #     # - return a Response object
    #     # - return a Request object
    #     # - or raise IgnoreRequest
    #     return response

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)



