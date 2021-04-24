from fake_useragent import UserAgent


# 使用第三方库来创建请求头

ua=UserAgent()

# print(ua.ie)
# print(ua.opera)
# 随机
print(ua.random)

headers={
    'user-agent':ua.random
}
print(headers)