# import requests
# response=requests.get('http://www.baidu.com')
# # print(response.text)
# # print(response.status_code)
# # print(response.url)
# # print(response.request)
# # print(response.content)
# # print(response.content.decode())
# print(response.headers)

# import requests
#
# name=input('请输入贴吧名：')
# # http://tieba.baidu.com/f?&kw=python
# url='http://tieba.baidu.com/f?&kw='+name
# response=requests.get(url)
# # print(response.url)
# content=response.content.decode('utf-8')
# flie_name=name+'.html'
# with open(flie_name,'w',encoding='utf-8') as fp:
#     fp.write(content)
# import requests
#
# # http://tieba.baidu.com/f?kw=python&pn=250
# url='http://tieba.baidu.com/f'
# name=input('请输入贴吧名：')
# for n in range(1,6,1):
#     pn=(n-1)*50
#     canshu={
#         'kw':name,
#         'pn':pn
#     }
#     response=requests.get(url,canshu)
#     # print(response.url)
#     content=response.content.decode('utf-8')
#     file_name=name+str(n)+'.html'
#     with open(file_name,'w',encoding='utf-8') as fp:
#         fp.write(content)

# import requests
# # https://www.baidu.com/s?&wd=baidu
# name=input('请输入要搜索的内容')
# url='http://www.baidu.com/s?'
# canshu={
#     'wd':name
# }
# response=requests.get(url,canshu)
# # print(response.url)
# content=response.content.decode('utf-8')
# with open('baidu.html','w',encoding='utf-8') as fp:
#     fp.write(content)

import requests
url='https://fanyi.baidu.com/sug'
keyword=input('请输入:')


form_data={'kw':keyword}

response=requests.post(url,form_data)
print(response.headers)
# print(response.text)
# print(response.content.decode('utf-8'))
# print(type(response.json()))
data=response.json()
print(data)
print(data['data'])
for item in data['data']:
    words=item['k']
    description=item['v']
    print(words,':',description)