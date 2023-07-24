import jsonpath

import urllib.request

url = 'https://dianying.taobao.com/cityAction.json?city=110100&_ksTS=1678978903641_19&jsoncallback=jsonp20&action=cityAction&n_s=new&event_submit_doLocate=true'

headrs = {
    # 'authority': ' dianying.taobao.com',
    # 'method': ' GET',
    # 'path': ' /cityAction.json?city=110100&_ksTS=1678978903641_19&jsoncallback=jsonp20&action=cityAction&n_s=new&event_submit_doLocate=true',
    # 'scheme': ' https',
    # 'accept': ' text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    # # 'accept-encoding': ' gzip, deflate, br',
    # 'accept-language': ' zh-CN,zh-TW;q=0.9,zh-HK;q=0.8,zh;q=0.7',
    'cookie': ' thw=cn; cna=NTm4Gva6uQACAXeAefsRhckg; miid=7697934131658040788; t=c9d6b22b663181d9fbcfd08233f348fc; sgcookie=E100KV5Czfn%2BhyXUI%2FBrOV7sJwmQcxVp743dchzApOdFw7%2BuqWrvsygYFpEmN2zEdkZGx%2Fq1FXc3Slx6348zvsDUYAt8MQPxyIkjwfuM7NLB2ow%3D; tracknick=%5Cu4EFB%5Cu51ED%5Cu5149%5Cu5F71%5Cu63A0%5Cu8FC7%5Cu65F6%5Cu9488; _cc_=UtASsssmfA%3D%3D; cookie2=1c99005c5573a9307c96dbad047ecf50; v=0; _tb_token_=e631abb113763; xlly_s=1; _m_h5_tk=44230e5ddaaed499c3b96b39bfb8ceb1_1678988922548; _m_h5_tk_enc=588d3c29c90178025e1f58c8eb3f9f94; tb_city=110100; tb_cityName="sbG+qQ=="; isg=BOrqRYT4era_GPAFXOcnTcyUO1aMW261xrUHPXSinT3Ip4hhXOoVxbCWNtO7DuZN; tfstk=cetlBnidKsN6rWopGQsSj7CO50hAZheVwBRW0xwQ7ALdGN-VibU47sTEosmxzy1..; l=fBOttN8PLRPxhjZ-BO5Ihurza77TmIObzRFzaNbMiIEGa6TPTFOQ1NCsn2pw7dtxgTfVjetyIZTzrdeJ8uzLSx9ZrVSzKtyuJlp6ObpU-L5..',
    'referer': 'https://dianying.taobao.com/',
    # 'sec-ch-ua': ' "Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    # 'sec-ch-ua-mobile': ' ?0',
    # 'sec-ch-ua-platform': ' "macOS"',
    # 'sec-fetch-dest': ' empty',
    # 'sec-fetch-mode': ' cors',
    # 'sec-fetch-site': ' same-origin',
    # 'user-agent': ' Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    # 'x-requested-with': ' XMLHttpRequest',
}

request = urllib.request.Request(url=url, headers=headrs)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
content = content.split('(')[1].split(')')[0]

with open('021-解析-jsonpath淘票票.json','w',encoding='utf-8') as fp:
    fp.write(content)

import json
obj =json.load(open('021-解析-jsonpath淘票票.json'))
city_list=jsonpath.jsonpath(obj, '$..name')
print(city_list)