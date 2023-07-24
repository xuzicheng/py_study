from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service(path='chromedriver.app')
driver = webdriver.Chrome(service=s)

url = 'https://www.baidu.com/'
driver.get(url)

i = driver.find_element(by='id', value='su')
# 获取标签属性
print(i.get_attribute('class'))
# 获取标签名字
print(i.tag_name)
print(i.text)
input()
