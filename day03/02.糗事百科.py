import requests
from lxml import etree

# for page in range(1,2,1):
#     url='http://www.lovehhy.net/Yulu/Detail/ALL/'+str(page)
#     response=requests.get(url)
#     # content=response.content.decode('utf-8')
#     content=response.text
    # with open('qiushi'+str(page)+'.html','w',encoding='utf-8') as fp:
    #     fp.write(content)
    # tree=etree.HTML(content)
    #标题
    # result=tree.xpath('.//div[@class="cat_llb"]/text()')
    # result=tree.xpath('.//a/[@class="catname""]/text()')
    # for i in result:
    #     print(i)
fp=open('qiushi1.html','r',encoding='utf-8')
content=fp.read()
tree=etree.HTML(content)

    #内容

    #类型

    #时间日期