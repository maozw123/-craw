import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
}

def two_request(new_url):
    print(new_url)
    # two_response = requests.get(url=new_url,headers=headers,verify=False)
    # two_soup = BeautifulSoup(two_response.text,'lxml')
    #需要什么加什么
def first_resquest(first_response):
    soup = BeautifulSoup(first_response.text,'lxml')
    first_body = soup.select('.u-items-list > .f-rt-list > ul > li > a')
    for num in first_body:
        new_url = 'https:' + str(num['href'])
        #发起二次请求
        two_request(new_url)

def main():
    url = 'https://pindao.suning.com/city/caidian.html?safp=d488778a.homepage1.99345513004.6'
    #第一次请求，获得请求
    first_response = requests.get(url=url,headers=headers,verify=False)
    first_resquest(first_response)

if __name__ == '__main__':
    main()
