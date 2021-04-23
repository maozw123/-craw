#步骤1：导包
import time
from selenium import webdriver
from scrapy.http import HtmlResponse
#步骤2：使用webdriver创建一个无界面浏览器对象
driver=webdriver.PhantomJS(executable_path=r'C:\Users\Administrator\Desktop\新建文件夹\phantomjs-2.1.1-windows\bin\phantomjs.exe')

url='http://www.baidu.com'
# 发起网络请求
driver.get(url)


# print(dirver.page_source)
# 保存当前页面的截屏
# driver.save_screenshot('baidu.png')

#获取当前页面的title
# print(driver.title)

#对页面元素进行操作
driver.find_element_by_id('kw').send_keys('python')
# # driver.find_element_by_class_name()#使用class查找
# # driver.find_element_by_name()
# # driver.find_element_by_xpath()#直接使用xpath
#
#
# #获取按钮，然后模拟单击操作
# driver.find_element_by_id('su').click()
# #阻塞
# time.sleep(2)
# # 保存当前页面的截屏
# driver.save_screenshot('baidu.png')
#
# driver.find_element_by_link_text('下一页>').click()
# time.sleep(2)
# # 保存当前页面的截屏
# driver.save_screenshot('baidu1.png')

#获取当前页面的cookie
print(driver.get_cookies())
print(driver.get_window_size())

# 热键的控制
from selenium.webdriver.common.keys import Keys
# eg:实现Ctrl+a   全选输入框内容
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')


driver.save_screenshot('ctrl+a.png')

# 模拟点击操作
# driver.find_element_by_id('su').click()#点击
# driver.find_element_by_id('su').submit()#提交

#清除功能
driver.find_element_by_id('kw').clear()

#获取当前页面的url
print(driver.current_url)

# 一般情况不要使用time.sleep(n)进行阻塞，原因是阻塞时间没法准确的确定
driver.find_element_by_id('su').click()

#需求：等页面加载完成后在进行下一步的操作
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
try:
    WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.ID,'content_left')))
    driver.save_screenshot('baidu-searched.png')
except:
    pass
finally:
    driver.quit()#退出

# 更强大的功能--模拟鼠标的动作--有空研究
