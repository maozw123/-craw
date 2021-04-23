name = input('请输入贴吧名称：')
import requests

url='http://tieba.baidu.com/f?kw='+name
response=requests.get(url)

content=response.content.decode('utf-8')

file_name=name+'.html'
with open(file_name,'w',encoding='utf-8') as fp:
    fp.write(content)