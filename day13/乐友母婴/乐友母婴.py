import requests
from lxml import etree
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3732.400 QQBrowser/10.5.3819.400'
}
for i in range(1,3,1):


    url='http://s.leyou.com.cn/search?key=%E8%BF%9B%E5%8F%A3%E5%A5%B6%E7%B2%89&page='+str(i)



    response=requests.get(url,headers=headers)

    concent=response.content.decode('utf-8')

    # with open('乐友.html','w',encoding='utf-8') as fp:
    #     fp.write(concent)
    tree=etree.HTML(concent)
    div_list=tree.xpath('//div[@class="wrapperList"]/div[@class="products"]')
    for div in div_list:
        # 标题
        title=div.xpath('./span[@class="intro"]/a/text()')
        # 价格
        price=div.xpath('./span[@class="disPrice"]/text()')
        print(title[0].strip())
        print(price[0])
        with open('leyou.txt','a',encoding='utf-8') as fp:
            fp.write(title[0].strip()+price[0]+'\n')

# http://s.leyou.com.cn/search?key=%E8%BF%9B%E5%8F%A3%E5%A5%B6%E7%B2%89&page=1&ctgy_code_all=17&sort=&marketing_title=&secondkey=
javascript:pageAction.redirect('ctgy_code_all',encodeURIComponent('17'))