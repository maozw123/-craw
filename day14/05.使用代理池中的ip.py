import requests
from fake_useragent import UserAgent

url='http://baidu.com'

ua=UserAgent()

headers={
    'user-agent':ua.random
}


response=requests.get('http://127.0..01:5555/random')
print(response.text)

proxies={
    'http':'http://{0}'.format(response.text)
}

response=requests.request('get',url,proxies=proxies)

with open('baidu.html','w',encoding='utf-8')as fp:
    fp.write(response.text)
