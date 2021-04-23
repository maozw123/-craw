import requests
from lxml import etree

url = 'https://music.163.com/discover/artist'
headers = {
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': '_ntes_nnid=c64b67d9afbc9ddce1a39248cc30972d,1565261126117; _ntes_nuid=c64b67d9afbc9ddce1a39248cc30972d; ntes_kaola_ad=1; WM_TID=qo1llSQ0mnNBFVUUFFdp8YH7Ebaj7WIY; ntes_kaola_ad=1; _iuqxldmzr_=32; JSESSIONID-WYYY=tcWRzNCyYG5QmeEGZ3g%2B3%2BkS6tdoPDSGggy3tIEQ1O91IAjYmrkiMmY%5CP4gZxyOzX9EB7CNyXj7FK3HtrXXwE8vGz8EjeSalRIF1mCnyd8TM93T2OdUnvx9SgzwHBm9FN7Aj9ZfdAb0VvtaYuzSaRShYCY8V%5CrVRgRjbIv1Gg75K5W%2Fu%3A1571211214965; WM_NI=Oy3%2BdsM4YbsAmObrxXgY3Hm6pecKMZtwfYWZ1MCkMRWv%2Fw%2FmhBRPlgdqB%2BLhK7J9Lz8YDUsCWq6kQUjyLl0wjMSl%2Bnz2jJO%2BOfu44PIFS3tGwVpRl2s7yovy91ktjt1eNVk%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eea9e6709beea8dab87c8b9e8fa3c85f879a9baeb880e986aa87c5709c9b00ccfb2af0fea7c3b92a8da7fdcce7798fec9783f24baf91ae93fb54a587fda9f03eb4bbadacd052b8a9aabad652f3938d8cd05a95aae198ae67ac9e9eb1ef6da8af8ecccf6489e986dacf72fc878cb6f24995affa8cd45faaa7848db37daa939d8daa66baeea6abce218dbabbd5b75c8b9a9dd4f74db58ac0b3ef3ab1e9b790f573fbefa595e980f3bb82b7ea37e2a3; MUSIC_U=43dbe34da1dd076b9e9a7a263c4313e12f8cba0b05f4a1599696144248efca0585fb74e5884360417e651dc6973f045541049cea1c6bb9b6; __remember_me=true; __csrf=a3b337840837d53718ff5ec64514efd5',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3732.400 QQBrowser/10.5.3819.400'

}
response = requests.get(url, headers=headers)
content = response.content.decode('utf-8')
with open('wangyiyun.html', 'w', encoding='utf-8') as fp:
    fp.write(content)

# 数据解析
# 歌手分组
tree = etree.HTML(content)
href_list = tree.xpath('//div[@class="blk"]/ul/li/a/@href')
# print(href_list)

# 爬取每一个分组的歌手
for href in href_list:
    new_url = 'https://music.163.com' + href
    # print(new_url)
    sub_content = requests.get(new_url, headers=headers).content.decode('utf-8')

    tree=etree.HTML(sub_content)
    # singer_name=tree.xpath('//ul[@id="m-artist-box"]/li/p/a[@class="nm nm-icn f-thide s-fc0"]/text() | //ul[@id="m-artist-box"]/li/a[@class="nm nm-icn f-thide s-fc0"]/text() ')
    singer_name=tree.xpath('//ul[@id="m-artist-box"]/li/p/a[1]/text() | //ul[@id="m-artist-box"]/li/a[1]/text() ')
    # print(len(singer_name))
    print(singer_name)


    #
