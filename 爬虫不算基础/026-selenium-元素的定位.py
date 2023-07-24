from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service(path='chromedriver.app')
driver = webdriver.Chrome(service=s)

url = 'https://www.baidu.com/'
driver.get(url)

# 元素定位
# 根据id查找
# button=driver.find_element('id','su')
# print(button)


# 根据标签属性值查找
# button=driver.find_element('name','wd')
# print(button)


# 根据xpath语句获取对象
# button =driver.find_element(by='xpath',value='//input[@id="su"]')
# print(button)


# 根据标签名字获取
# button =driver.find_element(by='tag name',value='input')
# print(button)

# 根据bs4语法获取
# button =driver.find_element(by='css selector',value='#su')
# print(button)

# 网页信息
# button =driver.find_element(by='link text',value='推荐')
# print(button)

input()
