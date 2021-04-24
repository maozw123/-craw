# 主要负责数据库相关操作
import pymysql
import redis
from settings import REDIS_PORT, REDIS_HOST


# 关系型数据库
class DBManager(object):

    # 初始化方法
    def __init__(self):
        try:
            self.conn = pymysql.connect('127.0.0.1', 'root', '', 'news', charset='utf8')
            self.cursor = self.conn.cursor()
        except:
            print('数据库连接异常')

    # 用来保存数据方法
    def save_item(self, item):
        # sql语法
        sql = 'insert into shangwubu(title,url,data_time) values (%s,%s,%s)on duplicate key update title=values(title),data_time=values(data_time)'
        # 准备数据
        data = (item.title, item.url, item.data_time)
        # print(data)
        # 执行
        self.cursor.execute(sql, data)
        # 提交
        self.conn.commit()

    # 对象回收
    def __del__(self):
        self.cursor.close()
        self.conn.close()


# 非关系型数据库
class RedisManager(object):
    def __init__(self):
        self.r = redis.Redis(REDIS_HOST, REDIS_PORT)

    def save_item(self, item):
        # data={
        #     'title':item.title,
        #     'url':item.url,
        #     'data_time':item.data_time
        # }

        # self.r.set(item.sign,str(data))
        self.r.set(item.sign, str(item.__dict__))
