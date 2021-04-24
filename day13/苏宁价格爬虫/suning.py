import requests

# url='https://search.suning.com/%E5%A5%B6%E7%B2%89/?safp=d488778a.682.1.3'
url='https://product.suning.com/0070993498/11406574088.html?adtype=1&safp=d488778a.13701.productWrap.2&safc=prd.2.3030066616'

headers={
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3732.400 QQBrowser/10.5.3819.400'
}

response=requests.get(url,headers=headers)

concent=response.content.decode('utf-8')

with open('su1.html','w',encoding='utf-8') as fp:
    fp.write(concent)
#
# https://ds.suning.com/ds/generalForTile/000000000126520498____R9006182_000278188,000000000124230659____R9006182_000278174,000000000132542469____R9006182_00027E889,000000011189198491____R9000373_000198183,000000011072615005__2_0070206966_R9006426_000256O21-010-2-0000000000-1--ds0000000006895.jsonp?callback=ds0000000006895
# https://ds.sunin/00000000g.com/ds/generalForTile0126520498____R9006182_000278188.jsonp?callback=ds0000000006895