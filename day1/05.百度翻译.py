import requests
url='https://fanyi.baidu.com/sug'
keyword=input('请输入:')


form_data={'kw':keyword}

response=requests.post(url,form_data)
print(response.headers)
# print(response.text)
# print(response.content.decode('utf-8'))
# print(type(response.json()))
data=response.json()
print(data)
print(data['data'])
for item in data['data']:
    words=item['k']
    description=item['v']
    print(words,':',description)