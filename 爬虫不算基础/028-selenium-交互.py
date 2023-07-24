from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 创建浏览器对象
s = Service(path='chromedriver.app')
driver = webdriver.Chrome(service=s)

# url
url = 'https://www.baidu.com/'
driver.get(url)

import time

time.sleep(2)

# 获取本文对象

i = driver.find_element(by='id', value='kw')

# 输入周杰伦
i.send_keys('周杰伦')
time.sleep(2)

# 获取百度一下按钮
button = driver.find_element(by='id', value='su')

# 点击
button.click()
time.sleep(2)

# 滑倒底部
js_buttom = 'document.documentElement.scrollTop=100000'
driver.execute_script(js_buttom)
time.sleep(2)

# 获取下一页按钮
next = driver.find_element(by='xpath', value='//a[@class="n"]')

# 点击下一页
next.click()
time.sleep(2)

# 回到上一页
driver.back()
time.sleep(2)

# 回去
driver.forward()
time.sleep(3)

# 退出
driver.quit()

input()
