import urllib.request

# 个人信息页面是utf-8 但是还报错了编码错误因为并没有进入到个人信息页面 历是跳转到了登陆页面
# 那么登防页面不是utf-8 所以报错

# 什么情况下访问不成功？
# 因为请求头的信息不够 所以访问不成功

url = 'https://weibo.com/p/1005056154874287/info?mod=pedit'

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'cookie': 'SINAGLOBAL=2210854678521.4478.1649294696478; PC_TOKEN=4ba08ee0c1; login_sid_t=82c252c0232823c2e29992144060847d; cross_origin_proto=SSL; WBStorage=4d96c54e|undefined; _s_tentry=www.bing.com; UOR=,,www.bing.com; Apache=771958765404.0994.1675427866711; ULV=1675427866715:4:1:1:771958765404.0994.1675427866711:1662865327388; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWrfYoBEYWJIge18dvRMOVa5JpX5o275NHD95QceK-X1hMXeonNWs4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNSo2fShnNShzRS7tt; SSOLoginState=1675427894; SUB=_2A25O2XARDeRhGeBP7lYZ9yrOwzuIHXVtr-bZrDV8PUNbmtAKLVXRkW9NRV03LJiSbe4DDsR7NpGOacpy482EuetT; ALF=1706963903; wvr=6; wb_view_log_6154874287=1440*9002; webim_unReadCount=%7B%22time%22%3A1675428227741%2C%22dm_pub_total%22%3A2%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A2%2C%22msgbox%22%3A0%7D'}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

with open('weibo.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
