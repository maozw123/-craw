import pymongo

#1.创建一个客户端对象--连接
#格式 pymongo.MongoClient(host='主机地址',port='27017')
client=pymongo.MongoClient()

#2.连接数据库（数据库不需要提前创建）
# 格式：客户端对象['数据库名']
db=client['newtestdb']

# 3.常用操作：插入
# 格式：数据库对象['表名'].insert(对象)
# db['class0701'].insert({'name':'xiaomao','age':'20','sex':'男'})

# (2)查找
# 格式：数据库对象['表名'].find(对象)
info=db['class0701'].find_one({'name':'xiaomao'})#查找一条
# db['class0701'].find_and_modify()
print(type(info),info)