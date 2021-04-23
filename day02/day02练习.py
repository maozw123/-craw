# import requests
#
# url = 'http://www.renren.com/861796782'
# headers={
#     'Cookie':'anonymid=k1r884qk35786; depovince=BJ; _r01_=1; jebe_key=5c548e81-d6c4-42d1-9a2e-dab50958f568%7C13bb55cf37bb82e89740b29392843602%7C1571106767742%7C1%7C1571106771315; ln_uact=13619566823; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; _de=4DCF95644B70C67FD0B19DBE341197DE; jebecookies=156510fc-b5c4-4f10-86de-4b974c93e55d|||||; JSESSIONID=abcyrWE5CPttahuFSep3w; ick_login=fe766cea-13ba-471a-813a-ea65d2ea57a0; p=5c5f8fbb84c7baf808129827e2ab96aa2; first_login_flag=1; t=c07598482ea7cff6e9c6e2cf20a8353b2; societyguester=c07598482ea7cff6e9c6e2cf20a8353b2; id=861796782; xnsid=30ed1cde; ver=7.0; loginfrom=null; wp_fold=0; XNESSESSIONID=291b161a8443; jebe_key=5c548e81-d6c4-42d1-9a2e-dab50958f568%7C180e36f401e6974b3d58ab3dc6bc5120%7C1571137541610%7C1%7C1571137545389',
#     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3732.400 QQBrowser/10.5.3819.400'
# }
# responses = requests.get(url,headers=headers)
# content=responses.content.decode('utf-8')
#
# with open('kaixin1.html','w',encoding='utf-8') as fp:
#     fp.write(content)


# import requests
# login_url='http://www.renren.com/PLogin.do'
#
# from_data={
#     'email':'13619566823',
#     'password':'12110816zxc'
# }
#
# session=requests.session()
# response=session.post(login_url,from_data)
# content=response.content.decode('utf-8')
# with open('renren2.html','w',encoding='utf-8') as fp:
#     fp.write(content)


# url='http://www.renren.com/861796782'
# responses=session.get(url)
# content=responses.content.decode('utf-8')
#
# with open('renren3.html','w',encoding='utf-8') as fp :
#     fp.write(content)

# 正则

# import re
#
# pattern=re.compile(r'a\.c')
#
# result=pattern.findall('a.c')
# print(result)


# import re
#
# pattern=re.compile(r'a[*]c')
#
# result=pattern.findall('a*c')
# print(result)


# import re
#
# pattern=re.compile(r'a\dc')
#
# result=pattern.findall('a3ca4c')
# result2=pattern.match('aa3ca4c')  #从起始位置开始查找，一次匹配
# result3=pattern.search('aa3ca4c') #从任何位置开始查找，一次匹配
#
# #捕获异常
# try:
#     print(result)
#     print(result2.group())
#     print(result3.group())
# except:
#     pass

# import re
#
# pattern=re.compile(r'a\wc')
# #  \w匹配数字字母下划线
#
# result=pattern.findall('a_c')
# print(result)


# import re
#
# pattern=re.compile(r'ab{,4}c')
#
# result=pattern.findall('abbbc')
# print(result)

# import re
#
# pattern=re.compile(r'a\b!bc')
#
# result=pattern.findall('a4bc')
# print(result)

# import re
#
# pattern=re.compile(r'abc|asd')
#
# # result=pattern.findall('abcasd')
# result=pattern.findall('asdabc')
# print(result)

import re
import requests

url = 'https://maoyan.com/films'
headers={
    "Cookie":'uuid_n_v=v1; uuid=33B7C650EF1E11E9B74ACFE5F544E767F54F6373D1B44D6AA71B8632A0E0CB4F; _csrf=0dddee0cc8b181445e48ab1e8db0dac57460e4938f003126098b8c217be3f2a4; _lxsdk_cuid=16dce56dbc1c8-00a4e103d451e-47744e16-100200-16dce56dbc3c8; _lxsdk=33B7C650EF1E11E9B74ACFE5F544E767F54F6373D1B44D6AA71B8632A0E0CB4F; _lx_utm=utm_source%3Dwww.sogou%26utm_medium%3Dorganic; __mta=121592887.1571124862388.1571141708891.1571141710558.8; _lxsdk_s=16dcf57c312-9de-c45-6ec%7C%7C16',
    "User-Agent":'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3732.400 QQBrowser/10.5.3819.400'
}
response = requests.get(url,headers=headers)
content = response.content.decode('utf-8')

with open('maoyan.html', 'w', encoding='utf-8')as fp:
    fp.write(content)

# pattern=re.compile(r'  <dd>(.*?)<dd>',re.S)
# result=pattern.findall(content)
# print(len(result))
# print(result)
# for movie_info in result:
#     name_pattern=re.compile(r'<div class="channel-detail movie-item-title" title="(.*?)">')
#     name_result=name_pattern.findall(movie_info)
#     print(name_result)
#
#     info=name_result[0]+'\n'
#     with open('maoyan1.txt',mode='a',encoding='gbk') as fp:
#         fp.write(info)