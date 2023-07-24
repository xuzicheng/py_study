# 导入
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 2:创建浏览器对象

# path='chromedriver.app'

s = Service(path='chromedriver.app')

driver = webdriver.Chrome(service=s)

# 3:访问网站

url = 'https://www.jd.com/'


driver.get(url)


content=driver.page_source
print(content)

input()