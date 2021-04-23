# name = input('请输入贴吧名称：')
# import requests
#
# for n in range(1, 6, 1):
#     pn = (n - 1) * 50
#     # http: // tieba.baidu.com / f?kw = python & ie = utf - 8 & pn = 30
#     # url = 'http://tieba.baidu.com/f?kw='+name+'&pn ='+str(pn)
#     url = 'http://tieba.baidu.com/f?kw=python&pn =' + str(pn)
#     response = requests.get(url)
#     content = response.content.decode('utf-8')
#     file_name = name + str(n) + '.html'
#     with open(file_name, 'w', encoding='utf-8') as fp:
#         fp.write(content)

name = input('请输入贴吧名称：')
import requests

url = 'http://tieba.baidu.com/f'
for n in range(1, 6, 1):
    pn = (n - 1) * 50
    canshu={'kw':name,'pn':pn}
    response = requests.get(url,canshu)
    content = response.content.decode('utf-8')
    # file_name = name + str(n) + '.html'
    # with open(file_name, 'w', encoding='utf-8') as fp:
    #     fp.write(content)


# https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&ch=11&tn=98010089_dg&wd=python&oq=%25E7%2599%25BE%25E5%25BA%25A6&rsv_pq=e584d1990000a69b&rsv_t=b48feJ9g86AKs%2FgLsDWB%2FxK1zLamxaEv2cFEqxoT6yVZwoW76Ieg8pKN9%2Fq0Ijy8j6A&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=9&rsv_sug1=8&rsv_sug7=100&rsv_sug2=0&inputT=7313&rsv_sug4=8047&rsv_sug=1
# https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&ch=11&tn=98010089_dg&wd=java&oq=python