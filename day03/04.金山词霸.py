# www.iciba.com

import requests
from lxml import etree
word=input('请输入你要翻译的单词：')
url='http://www.iciba.com/'+word
headers={
    'Cookie':'iciba_u_rand=44305e1e0627367024adc003b8ada5fa%4027.155.93.84; iciba_u_rand_t=1571223991; is_new_index=1; UM_distinctid=16dd43f748d9c-05fb566fc698fc-5b123211-100200-16dd43f748e65b; __gads=ID=ea1a05b3f9d41ffa:T=1571224085:S=ALNI_MbFtcQOljdarDQbBK_i3qSMVqFa8w; CNZZDATA1257391275=1257409460-1571218689-%7C1571224091; cbdownload_num=1; cbdownload_time=download; search-history=rg; CNZZDATA1256556802=1114093804-1571229859-http%253A%252F%252Fwww.iciba.com%252F%7C1571229859; c_word_history=rg',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}

response=requests.get(url,headers=headers)
content=response.content.decode('utf-8')

# with open(word+'.html','w',encoding='utf-8') as fp:
#     fp.write(content)
tree=etree.HTML(content)
jieshi_list=tree.xpath('//ul[@class="base-list switch_part"]/li/span/text() | //ul[@class="base-list switch_part"]/li/p/span/text() ')
# print(len(jieshi_list))
print(jieshi_list)
