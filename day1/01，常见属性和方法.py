import requests

# 发起网络请求，得到相应
response = requests.get('http://www.baidu.com')

# 常见属性
print(response.status_code)  #返回状态码
print(response.encoding)    #编码格式
print(response.headers)     #请求头内容
print(response.text)  # 请求回来页面文本内容
# 注意，有时候得到的文本是乱码
print(response.content)
#content得到的是字节型数据  不能显示中文
print(response.content.decode('utf-8'))

#绝大多数情况下text能够正常使用
#但是如果出现乱码，使用content
# text===content.decode(编码)

#content确实能够解决文本问题  但是它的功能不仅限于此，更多用于非文本数据。
print('-------------------------------------')
response=requests.get('http://langlang2017.com/img/logo.png')
# print(response.text)
# print(response.content)
with open('logo.png','wb+') as fp:
    fp.write(response.content)

