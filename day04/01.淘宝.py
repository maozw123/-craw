import requests
import re
import json
from lxml import etree


url='https://www.taobao.com/market/3c/shouji.php?spm=a21bo.7723600.8557.2.56f85ec9Foq6kb'

headers={
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3732.400 QQBrowser/10.5.3819.400'
}
response=requests.get(url,headers=headers)

content=response.content.decode('gbk')

# with open('taobao.html','w',encoding='gbk') as fp:
# #     fp.write(content)

#数据提取
#正则定义规则
pattern=re.compile(r'<script class="J_ContextData" type="text/template">(.*?)</script>',re.S)
#匹配
result=pattern.search(content,80000,91164)
# print(result.span())
data=result.group(1).strip()

data_str=json.dumps(data,ensure_ascii=False)
print(data_str)
with open('shouji.txt','w',encoding='utf-8',) as fp:
    fp.write(data_str)