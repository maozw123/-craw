import time, math, hashlib,requests,json
from lxml import etree
from fake_useragent import UserAgent
def jinri():
    t = math.floor(time.time())  # 获取当前时间戳的前十位
    print(t)
    print(str(hex(t)))
    e = str(hex(t)).upper()  # 转十六进制并把字母变成大写
    print(e)
    md5 = hashlib.md5()
    md5.update(bytes(str(t), encoding='utf-8'))
    i = md5.hexdigest().upper()  #md5加密并转大写
    print(type(i))
    print('i',i)
    print(len(i))

    if len(i)!=8:
        as1="479BB4B7254C150"
        cp="7E0AC8874BB0985"
    n=i[0:5]
    print('n',n)
    s=i[-5:]
    print('s',s)
    o=''
    a=0
    '''
    for (var n = i.slice(0, 5), s = i.slice( - 5), o = "", a = 0; 5 > a; a++) o += n[a] + e[a];
            for (var r = "", l = 0; 5 > l; l++) r += e[l + 3] + s[l];
            return {
                as: "A1" + o + e.slice( - 3),
                cp: e.slice(0, 3) + r + "E1"
    '''

    while a<5 :
        o += n[a] + e[a]
        a+=1
    print(a)
    r = ""
    l = 0

    while l<5:
        r += e[l + 3] + s[l]
        l+=1
    as1= "A1" + o + e[-3:]
    cp= e[0:3] + r + "E1"
    print('as1',as1)
    print('cp',cp)
    return as1,cp
as1,cp=jinri()
print(as1,cp)
# url='https://www.toutiao.com/api/pc/feed/?category=news_sports&utm_source=toutiao&widen=1&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true&as={0}&cp={1}&_signature=1oJPsAAgEBncOiHuqHRaU9aCTqAAIti'.format(as1,cp)
#
# url2='https://www.toutiao.com/api/pc/feed/?category=news_sports&utm_source=toutiao&widen=1&max_behot_time={0}&max_behot_time_tmp={0}&tadrequire=true&as=A1D52DFDEB9A18F&cp=5DDBBAD1C81F1E1&_signature=sbqE9AAgEBa7AuqqUbWEfLG6heAAOxv'.format(t)

# 'https://www.toutiao.com/api/pc/feed/?min_behot_time=0&category=__all__&utm_source=toutiao&widen=1&tadrequire=true&as=A1F5DD5D3C07C64&cp=5DDC87ECE6B47E1&_signature=UzxctAAgEBRZhDLq96uf6lM8XKAAA7h'
url='https://www.toutiao.com/api/pc/feed/?min_behot_time=0&category=__all__&utm_source=toutiao&widen=1&tadrequire=true&as={0}&cp={1}&_signature=60v7TAAgEBPh85USJPF9jOtL-1AALab'.format(as1,cp)
ur1='https://www.toutiao.com/api/pc/feed/?min_behot_time=0&category=__all__&utm_source=toutiao&widen=1&tadrequire=true&as=A1C5ADFDDB3C071&cp=5DDBAC90B7E1EE1&_signature=2h3KngAgEB7QpaTAPlP8TdodyoAAIfO'
ua=UserAgent()
headers={
    'user-agent':ua.random
}

response=requests.get(url,headers=headers)
content=response.json()
# print(content)
data=content["data"]
print(data)
for i in data:
    title=i['title']
    print(title)

# content=response.content.decode('GB2312')
# print(content)
# url2='https://www.toutiao.com/api/pc/feed/?max_behot_time=1574680609&category=__all__&utm_source=toutiao&widen=1&tadrequire=true&as={0}&cp={1}&_signature=K52pmAAgEBMhJcfG8Ig7ZSudqYAAHZN'.format(as1,cp)
# print(url)
# print(url2)
