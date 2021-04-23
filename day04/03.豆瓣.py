import requests
from lxml import etree
import re


url='https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action='

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3732.400 QQBrowser/10.5.3819.400'
}
# https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=60&limit=20
content=requests.get(url,headers=headers).content.decode('utf-8')
tree=etree.HTML(content)
href_type_list=tree.xpath('//div[@class="types"]/span/a/@href')
print(href_type_list)
movie_set=set()
for href_type in href_type_list:
    print(href_type)
    pattern=re.compile(r'\d+')
    result = pattern.search(href_type)
# #     #电影类型编号
#     print(result.group())
    data_url='https://movie.douban.com/j/chart/top_list_count?type={0}&interval_id=100%3A90'.format(result.group())
    # print(data_url)
    #每个电影类型的电影数量total
    data_count=requests.get(data_url,headers=headers).json()
    print(data_count['total'])
    movie_name_url='https://movie.douban.com/j/chart/top_list?type={0}&interval_id=100%3A90&action=&start=0&limit={1}'.format(result.group(),data_count['total'])
    # print(movie_name_url)
    data_movie_count_list=requests.get(movie_name_url,headers=headers).json()
    # print(data_movie_count_list)
    for movie in data_movie_count_list:
        title=movie['title']
        movie_set.add(title)
for i in movie_set:
    with open('doubanmovie_list1.txt', 'a', encoding='utf-8') as fp:
        fp.write(i+'\n')
            #保存之后考虑数据去重问题
# with open ('douban.html','w',encoding='utf-8') as fp:
#     fp.write(content)

# import math
# for n in range(1,math.ceil(653/20)+1,1):
#     star=(n-1)*20
#     url='https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start={0}&limit=20'.format(star)
#     print(url)
    # data=requests.get(url,headers=headers).json()
    # for movie in data:
    #     title=movie['title']
    #     with open('doubanmovie.txt','a',encoding='utf-8') as fp:
    #         fp.write(title+'\n')
# url='https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=653'
# data=requests.get(url,headers=headers).json()
# for movie in data:
#         title=movie['title']
#         with open('doubanmovie1.txt','a',encoding='utf-8') as fp:
#             fp.write(title+'\n')
#
# https://movie.douban.com/j/chart/top_list_count?type=11&interval_id=100%3A90
# https://movie.douban.com/j/chart/top_list_count?type=24&interval_id=100%3A90
# https://movie.douban.com/j/chart/top_list_count?type=5&interval_id=100%3A90

