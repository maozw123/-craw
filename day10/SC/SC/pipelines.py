# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
# class ScPipeline(object):
#     def __init__(self):
#         self.client=pymongo.MongoClient()
#         self.db=self.client['SC']
#
#     def process_item(self, item, spider):
#         self.db['cars'].insert(dict(item))
#         return item
class ErshouchePipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient(
            host='10.10.14.241',
            port=27017,
            document_class=dict,
        )
        self.db = self.client['SC']

    def process_item(self, item, spider):
        print('1111111111111111111111111111')
        self.db['cars'].insert_one(dict(item))
        return item