import requests
url='http://www.renren.com/861796782'
headers={
    'Cookie':'anonymid=k1r884qk35786; depovince=BJ; _r01_=1; JSESSIONID=abcUwZS-rMlN6-30Ipn3w; ick_login=2460d791-c5d6-49ad-a15e-b5b1a8185e67; jebe_key=5c548e81-d6c4-42d1-9a2e-dab50958f568%7C13bb55cf37bb82e89740b29392843602%7C1571106767742%7C1%7C1571106771315; jebecookies=798b24f7-154f-440c-b95f-a016f0cad7da|||||; _de=4DCF95644B70C67FD0B19DBE341197DE; p=76acba4b72ca5702a809ad0786fed6e22; ap=861796782; first_login_flag=1; ln_uact=13619566823; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=5008f1f8cd17476f10266358c4a2c3492; societyguester=5008f1f8cd17476f10266358c4a2c3492; id=861796782; xnsid=3212ce96; ver=7.0; loginfrom=null; wp_fold=0; jebe_key=5c548e81-d6c4-42d1-9a2e-dab50958f568%7C180e36f401e6974b3d58ab3dc6bc5120%7C1571118264945%7C1%7C1571118268476',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3732.400 QQBrowser/10.5.3819.400'
}
responses=requests.get(url,headers=headers)
content=responses.content.decode('utf-8')

with open('kaixin1.html','w',encoding='utf-8') as fp :
    fp.write(content)