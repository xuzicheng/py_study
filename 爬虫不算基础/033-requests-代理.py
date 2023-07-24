import requests

url = 'https://fanyi.baidu.com/'

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

data = {
    'kw': 'ip'
}

proxy = {
    'http': '121.13.252.58：41564'
}

response = requests.get(url=url, params=data, headers=headers, proxies=proxy)

content = response.text

with open('daili2.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
