# 主要负责数据模型的管理

class News(object):

    # 初始化方法
    def __init__(self,title,url,data_time):
        self.title =title
        self.url =url
        self.data_time =data_time
        #每个数据对象签名
        self.sign=''
