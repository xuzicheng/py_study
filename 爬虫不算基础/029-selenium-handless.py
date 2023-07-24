# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable‐gpu')
# # 设置为自己chrome浏览器.exe的系统路径
# path = r'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
# chrome_options.binary_location = path
# browser = webdriver.Chrome(chrome_options=chrome_options)
#
# browser.get('https://www.baidu.com')
# # browser.save_screenshot('baidu.jpg')
#
# # browser.save_screenshot('baidu.png')


# 封装handless
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def share_browser():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable‐gpu')
    # 设置为自己chrome浏览器.exe的系统路径
    path = r'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
    chrome_options.binary_location = path
    browser = webdriver.Chrome(chrome_options=chrome_options)
    return browser


browser = share_browser()

url = 'https://www.baidu.com'

browser.get(url)
