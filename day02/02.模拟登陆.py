import requests
login_url='http://www.renren.com/PLogin.do'
form_data={
    'email':'13619566823',
    'password':'12110816zxc'
}
session=requests.session()
response=session.post(login_url,form_data)
content=response.content.decode('utf-8')
with open('kaixin3.html','w',encoding='utf-8') as fp :
    fp.write(content)

url='http://www.renren.com/861796782'
responses=session.get(url)
content=responses.content.decode('utf-8')
with open('kaixin4.html','w',encoding='utf-8') as fp :
    fp.write(content)