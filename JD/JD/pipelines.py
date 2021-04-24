# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import pymongo
import redis
class JdPipeline(object):
    def process_item(self, item, spider):
        conn=pymysql.connect('127.0.0.1','root','','sqider_db',charset='utf8')
        cursor=conn.cursor()
        # print('连接到数据库')
        sql='insert into jd_phone(title,detail_url,price_url,x_price,y_price,spid) values(%s,%s,%s,%s,%s,%s)'
        data=(item['title'],item['detail_url'],item['price_url'],item['x_price'],item['y_price'],item['spid'])
        cursor.execute(sql,data)
        conn.commit()

        cursor.close()
        conn.close()
        # print('保存完成')
        return item
#保存到mysqlshujuku


# 保存到mongodb数据库

# 保存到redis数据库

