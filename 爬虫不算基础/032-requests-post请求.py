import requests

url = 'https://fanyi.baidu.com/sug'

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

data = {
    'kw': 'eye'
}

response = requests.post(url=url, data=data, headers=headers)
content = response.text

obj = response.json()

print(obj)
