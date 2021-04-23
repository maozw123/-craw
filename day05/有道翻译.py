import requests
import time
import random
import hashlib

# 学习ji  md5加密的方式
# 'http://fanyi.youdao.com/?keyfrom=dict2.index'
url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
i=input('请输入要翻译的单词')
#需要13位的时间戳
ts=int(time.time()*1000)
#ts拼接10以内随机数，变成14位的字符串
salt=str(ts)+str(random.randint(0,10))
print(ts,len(str(ts)))
print(salt,len(salt))

def create_md5(s):
    md5=hashlib.md5()
    md5.update(bytes(s,encoding='utf-8'))
    result=md5.hexdigest()
    return result

s = "fanyideskweb" + i + salt + "n%A-rKaT5fb[Gy?;N5@Tj"
sign = create_md5(s)
print(sign)

form_data={
    'i': i,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt':salt,
    'sign': sign,
    'ts': str(ts),
    'bv': '667f88db2f26cdd85e1579ec25442cf3',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME'
}
headers={
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Connection':'keep-alive',
    'Content-Length':str(233+len(i)),
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie':'OUTFOX_SEARCH_USER_ID=-2014290802@10.168.8.76; OUTFOX_SEARCH_USER_ID_NCOO=1095735732.7893126; _ntes_nnid=3f88ca2ba35dfe2653f2e8d1b3b3b2f1,1561725334223; _ga=GA1.2.494160936.1562669849; JSESSIONID=abcqgkWNOgv7cd-93AC3w; user-from=http://www.youdao.com/w/?keyfrom=dict2.top; from-page=http://www.youdao.com/w/?keyfrom=dict2.top; ___rl__test__cookies=1571361393615',
    'Host':'fanyi.youdao.com',
    'Origin':'http://fanyi.youdao.com',
    'Referer':'http://fanyi.youdao.com/?keyfrom=dict2.index',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3732.400 QQBrowser/10.5.3819.400',
    'X-Requested-With':'XMLHttpRequest',
}
response=requests.post(url,headers=headers,data=form_data)
print(response.text)

