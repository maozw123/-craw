import re
import requests

# 发起网络请求
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3732.400 QQBrowser/10.5.3819.400',
    'Accept-Language': 'zh-CN,zh;q=0.9'
}
url = 'https://maoyan.com/board'
response = requests.get(url, headers=headers)
content = response.content.decode('utf-8')
with open('maoyan.html', 'w', encoding='utf-8') as fp:
    fp.write(content)

# 使用正则进行数据提取

# pattern=re.compile(r'title="(.*?)"')
# # result=pattern.findall(content)
# # print(result)

pattern = re.compile(r'<dd>.*?</dd>', re.S)
result = pattern.findall(content)
print(len(result))

for movie_info in result:
    # 电影名称
    name_pattern = re.compile(r'<a href="/films/\d+" title="(.*?)"')
    name_result = name_pattern.findall(movie_info)
    # print(name_result[0])

    # 主演
    star_patten = re.compile(r'<p class="star">(.*?)</p>', re.S)
    star_result = star_patten.findall(movie_info)
    star = star_result[0].strip()
    # print(name_result[0],star)

    # 上映时间
    time_patten = re.compile(r'<p class="releasetime">(.*?)</p>')
    time_result = time_patten.findall(movie_info)
    # print(name_result[0],star,time_result)
    # 图片地址
    images_patten = re.compile(r'<img data-src="(.*?)"')
    images_result = images_patten.findall(movie_info)
    # print(name_result[0],star,time_result,images_result[0])

    # 排名
    index_patten = re.compile(r'<i class="board-index board-index-\d+">(.*?)</i>')
    index_result = index_patten.findall(movie_info)
    print(name_result[0], star, time_result, images_result[0], index_result[0])
    info =index_result[0]+'--'+ name_result[0] +'--'+time_result[0]+ '\n'
    with open('maoyan.txt', 'a', encoding='gbk') as fp:
        fp.write(info)
