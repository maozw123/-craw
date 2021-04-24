# # -*- coding: utf-8 -*-
#
# # Define here the models for your scraped items
# #
# # See documentation in:
# # https://docs.scrapy.org/en/latest/topics/items.html
#
import scrapy
#
#
# # class ScItem(scrapy.Item):
# #     # define the fields for your item here like:
# #     # name = scrapy.Field()
# #     pass
#
# class CarItem(scrapy.Item):
#     # define the fields for your item here like:
#     c_title = scrapy.Field()  #
#     c_url = scrapy.Field()  #
#     c_year = scrapy.Field()  #
#     c_distance = scrapy.Field()  #
#     c_location = scrapy.Field()  #
#     c_price = scrapy.Field()  # 售价
#     c_ori_price = scrapy.Field()  # 原价
#     c_crawl_time = scrapy.Field()  # 爬取时间
#
#
#     #详情页数据
#     pinpai = scrapy.Field()  # 品牌
#     xinghao = scrapy.Field()  # 型号
#     fadongji = scrapy.Field()  #
#     qudong = scrapy.Field()  #
#     jibie = scrapy.Field()  #
#     pailiang = scrapy.Field()  #
#     youhao = scrapy.Field()  #
#     ckg = scrapy.Field()  #
#     cheshenglx = scrapy.Field()  #
#     houbeirongji = scrapy.Field()  #
class ErshoucheItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ID = scrapy.Field()
    ErShouChe_Name = scrapy.Field()             # 车的名字
    ErShouChe_original_price = scrapy.Field()   # 车的原价
    ErShouChe_present_price = scrapy.Field()    # 车的现价
    ErShouChe_location = scrapy.Field()         # 车的位置
    ErShouChe_distance = scrapy.Field()         # 行驶里程
    ErShouChe_year = scrapy.Field()             # 买车年限
    ErShouChe_detail_href = scrapy.Field()      # 详情链接

    ErShouChe_spider_time = scrapy.Field()      # 爬取时间

    # 详情页数据
    ErShouChe_PinPai = scrapy.Field()           # 车的品牌
    ErShouChe_XingHao = scrapy.Field()          # 车的型号
    ErShouChe_PaiLiang = scrapy.Field()         # 车的排量
    ErShouChe_YouHao = scrapy.Field()           # 车的油耗
    ErShouChe_FaDong = scrapy.Field()           # 车发动机
    ErShouChe_QuDong = scrapy.Field()           # 车的驱动
    ErShouChe_JiBie = scrapy.Field()            # 车辆级别
    ErShouChe_CKG = scrapy.Field()              # 车长宽高
    ErShouChe_CSLX = scrapy.Field()             # 车身类型
    ErShouChe_HBX = scrapy.Field()

    IP = scrapy.Field()# 车后备箱
    Name= scrapy.Field()# 车后备箱
