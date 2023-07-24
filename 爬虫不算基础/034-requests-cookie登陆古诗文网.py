# 通过登陆进入到主页面

# __VIEWSTATE: cLkE9TAf6a1g4s2TpaFtPTXeSJw+/b5hafuT37U9d2OxAZ+mlPExEqhmPdQ69DTV8AbDvqw2JtpPi6LlCAaxX0DRntxbOxbVO+GKivvz+oTclnAdSlXku5Q7dFXIfCVneif9P4bJWFYusqj40S9ZgMJVsqc=
# __VIEWSTATEGENERATOR: C93BE1AE
# from: http://so.gushiwen.cn/user/collect.aspx
# email: 502659139@qq.com
# pwd: asdasd
# code: igqw
# denglu: 登录


# 观察到__VIEWSTATE  __VIEWSTATEGENERATOR  code 是变量
#   view在源码里面


import requests

# 登陆页面url地址
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
#  获取页面源码
resposne = requests.get(url=url, headers=headers)
content = resposne.text

# 解析 __VIEWSTATE  __VIEWSTATEGENERATOR
from bs4 import BeautifulSoup

soup = BeautifulSoup(content, 'lxml')

# 获取__VIEWSTATE
viewstate = soup.select('#__VIEWSTATE')[0].attrs.get('value')

vIEWSTATEGENERATOR = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')
# print(viewstate)
# print(vIEWSTATEGENERATOR)

# 获取验证码图片
code = soup.select('#imgCode')[0].attrs.get('src')
# print(code)
code_url = 'https://so.gushiwen.cn/' + code
# print(code_url)


# requests里面有个方法，session,通过ession返回值就能使请求变成一个对象,
session = requests.session()
# 验证码url的内容
response_code = session.get(code_url)
# 要使用二进制数据，因为我们要使用的是图片的下载，
content_code = response_code.content
# wb,将二进制数据写入到文件
with open('code.jpg', 'wb') as fp:
    fp.write(content_code)

code_name = input('请输入验证码')

# 点击登陆
url_post = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'

data_post = {
    '__VIEWSTATE': viewstate,
    '__VIEWSTATEGENERATOR': vIEWSTATEGENERATOR,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '502659139@qq.com',
    'pwd': 'zse123579',
    'code': code_name,
    'denglu': '登陆',
}

responsec_post = session.post(url=url, headers=headers, data=data_post)

content_post = responsec_post.text
with open('gushiwen.html', 'w', encoding='utf-8') as fp:
    fp.write(content_post)
