import requests
import json

#1.将对象---字符串
data = {'name':'lori','age':21,'guoji':'中国'}
data_str =json.dumps(data,ensure_ascii=False)
json.dump(data,open('data.txt','w',encoding='utf-8'))
print(data_str)
#主要原因，dump将对象转换成json字符串的时候，默认采用的ascii
#想显示正常的汉字，默认ensure_ascii=False


#2.将字符串---对象（字典、列表）
data_str = '{"guoji": "中国", "name": "lori", "age": 21}'
obj = json.loads(data_str)
print(type(obj),obj['guoji'])

fp = open('data.txt','r',encoding='utf-8')
obj2 = json.load(fp)
print(type(obj2),obj2['guoji'])

