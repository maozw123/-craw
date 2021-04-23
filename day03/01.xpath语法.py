import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3732.400 QQBrowser/10.5.3819.400',
    'Accept-Language': 'zh-CN,zh;q=0.9'
}
response=requests.get('https://maoyan.com/board',headers=headers)
concent=response.content.decode('utf-8')

with open('maoyan5.html','w',encoding='utf-8') as fp:
    fp.write(concent)
#使用xpath提取数据
# 步骤1，导包
from lxml import etree
# 步骤2，将请求回来的页面内容（字符串对象）生成节点数
tree=etree.HTML(concent)

# 步骤3，使用xpath语法进行数据提取
# result=tree.xpath('路径')
# eg:查找title标签

result=tree.xpath('//title')
# print(result)

result=tree.xpath('//a')

#查找每一个电影节点---<dd>...</dd>
result=tree.xpath('//dd')

for movie in result:
    #表示从当前节点开始查找所有的a标签
    # a_list=movie.xpath('.//a')

    #选取属性
    # a_href_list = movie.xpath('.//a/@href')
    a_title_list = movie.xpath('.//a/@title')

    #取值

    a_text_list=movie.xpath('.//p/a/text()')
    #主演
    # p_star_list=movie.xpath('.//div/p[2]/text()')
    # p_star_list=movie.xpath('.//p[@class="star"]/text()')
    # p_star_list=movie.xpath('.//p[2]/text()')
    #评分
    p_score_list=movie.xpath('.//p[last()]/i/text()')

    # p_text_list=movie.xpath('.//p[position()>2]/text()')

    #主演，日期
    p_star_list = movie.xpath('.//p[@class="star"]/text()')
    p_time_list = movie.xpath('.//p[@class="releasetime"]/text()')
    print(a_title_list[0],p_star_list[0].strip(),p_time_list[0])

# print(len(result),type(result))
