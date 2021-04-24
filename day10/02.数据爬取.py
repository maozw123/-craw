import requests
import jsonpath
import pymongo

url='https://careers.tencent.com/tencentcareer/api/post/Query?&pageIndex=1&pageSize=4079'
headers={
    'user-agent':'sasdafa'
}
response=requests.get(url,headers=headers)
data=response.json()
job_list=jsonpath.jsonpath(data,'$..Posts.*')

client=pymongo.MongoClient()
db=client['tencent']
for job in job_list:
    db['jobs'].insert(dict(job))



# import requests
# import jsonpath
# import pymongo
#
# def mongodb_init():
#     client = pymongo.MongoClient()
#     db = client['Tencent']
#     return db
#
# def save_job(db,job):
#     db['jobs'].insert(job)
#
# if __name__ == '__main__':
#     # client = pymongo.MongoClient()
#     url = "https://careers.tencent.com/tencentcareer/api/post/Query?&pageIndex=1&pageSize=4079"
#     headers = {
#         'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
#     }
#     response = requests.get(url, headers=headers)
#     data = response.json()
#     jon_list = jsonpath.jsonpath(data, '$..Posts.*')
#
#     db = mongodb_init()
#     for job in jon_list:
#         save_job(db,job)