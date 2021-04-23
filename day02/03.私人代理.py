import requests



proxy = {'http':'用户名：密码@ip:端口'}

requests.get('http://www.baidu.com',proxies=proxy)



