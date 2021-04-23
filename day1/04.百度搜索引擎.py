name = input('请输入名称：')
import requests
# https://www.baidu.com/s?&wd=python
canshu={
    'wd':name,
}
headers={
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3732.400 QQBrowser/10.5.3819.400',
}
url='http://www.baidu.com/s?'
response=requests.get(url,canshu,headers=headers)

content=response.content.decode('utf-8')

file_name=name+'.html'
with open(file_name,'w',encoding='utf-8') as fp:
    fp.write(content)
# print(response.url)
# print(response.content)