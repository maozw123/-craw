import re,requests
from lxml import etree

from fake_useragent import UserAgent
ua=UserAgent()
headers = {'User-Agent':ua.random}

# url='https://www.toutiao.com/'

# 首页推荐的url
url='https://www.toutiao.com/api/pc/feed/?min_behot_time=0&category=__all__&utm_source=toutiao&widen=1&tadrequire=true&as=A1A5DDED6BA37D2&cp=5DDB13A70DE2CE1&_signature=GHLdIAAgEBsSyrN-MliJvRhy3TAAEWu'

# 每次加载九条数据，第一次接口为



'''
https://www.toutiao.com/api/pc/feed/?category=news_sports&utm_source=toutiao&widen=1&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true&as=A1558D7D9B96964&cp=5DDB562996A4CE1&_signature=ootgDAAgEB-oMw5SnKxqs6KLYRAAP9f

category: news_sports
utm_source: toutiao
widen: 1
max_behot_time: 0
max_behot_time_tmp: 0
tadrequire: true
as: A1558D7D9B96964
cp: 5DDB562996A4CE1
_signature: ootgDAAgEB-oMw5SnKxqs6KLYRAAP9f
_signature: ootgDAAgEB-oMw5SnKwXe6KLYRAAP9f
https://www.toutiao.com/api/pc/feed/?category=news_sports&utm_source=toutiao&widen=1&max_behot_time=1574660435&max_behot_time_tmp=1574660435&tadrequire=true&as=A1253D9DCBD69EE&cp=5DDBB629AE5E0E1&_signature=ootgDAAgEB-oMw5SnKwXe6KLYRAAP9f
category: news_sports
utm_source: toutiao
widen: 1
max_behot_time: 1574660435
max_behot_time_tmp: 1574660435
tadrequire: true
as: A1253D9DCBD69EE
cp: 5DDBB629AE5E0E1
_signature: ootgDAAgEB-oMw5SnKwXe6KLYRAAP9f

https://www.toutiao.com/api/pc/feed/?category=news_sports&utm_source=toutiao&widen=1&max_behot_time=1574658634&max_behot_time_tmp=1574658634&tadrequire=true&as=A135FD6DAB26A07&cp=5DDBC67AE0B7DE1&_signature=ootgDAAgEB-oMw5SnKx7S6KLYRAAP9f

category: news_sports
utm_source: toutiao
widen: 1
max_behot_time: 1574658634
max_behot_time_tmp: 1574658634
tadrequire: true
as: A135FD6DAB26A07
cp: 5DDBC67AE0B7DE1
_signature: ootgDAAgEB-oMw5SnKx7S6KLYRAAP9f
https://www.toutiao.com/api/pc/feed/?category=news_sports&utm_source=toutiao&widen=1&max_behot_time=1574656534&max_behot_time_tmp=1574656534&tadrequire=true&as=A1757D2D0B46A34&cp=5DDB46BA4344FE1&_signature=ootgDAAgEB-oMw5SnKzlbqKLYRAAP9f

category: news_sports
utm_source: toutiao
widen: 1
max_behot_time: 1574656534
max_behot_time_tmp: 1574656534
tadrequire: true
as: A1757D2D0B46A34
cp: 5DDB46BA4344FE1
_signature: ootgDAAgEB-oMw5SnKzlbqKLYRAAP9f
'''
response=requests.get(url,headers=headers)
content=response.content.decode('utf-8')
# print(response.text)
with open('jrtt.html','w',encoding='utf-8') as fp:
    fp.write(content)
