import requests

proxies = {
    'http': 'http://120.83.111.5:9999',
    'https': 'https://27.152.90.157:9999'
}

url = 'http://www.baidu.com'
# response=requests.get(url,proxies=proxies)
response = requests.request('get', url, proxies=proxies)
print(response.text)
