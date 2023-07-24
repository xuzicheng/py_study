import urllib.request
import urllib.parse

url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

headers = {
    # 'Accept': ' */*',
    # # 'Accept-Encoding':' gzip, deflate, br',
    # 'Accept-Language': ' zh-CN,zh-TW;q=0.9,zh-HK;q=0.8,zh;q=0.7',
    # 'Acs-Token': ' 1675152364520_1675167937194_4Ao0uv3ztUqZdNUUu843qtRz/oP4v+gZKsMn/pJJXcNXjEByb3OCaM2LkWujmQA4HFVNlZnfpNNm6f8xQFB1FD2JqES/hV/VwuanNA40RPb/y/Hhg+99OJPmSeX+35DdLgzHfzLq4CiU22QEPHiSM/LUM0CRcfIM+l6lJs3Lpxk+gsE3IhxUejpMM0Vmw9yeslAJnJUulDlugNgH2Io/fhS0n4wju4sE5sR+zL3VmBzB5gWS568gKOET/j20K64F+blx0CbrzT3zB7/b2br66f4KfoqJADdHzkuvOxsh+ixdOtiMZ7zO4nbMu5f1pG7E',
    # 'Connection': ' keep-alive',
    # 'Content-Length': ' 132',
    # 'Content-Type': ' application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': ' BIDUPSID=8BFA76A1F13AF2BCF8142E492568EC14; PSTM=1647852584; BAIDUID=A02908AD967075BE05B6636F5EC0F4CC:FG=1; BAIDUID_BFESS=A02908AD967075BE05B6636F5EC0F4CC:FG=1; BAIDU_WISE_UID=wapp_1654239069476_903; ZFY=edyhXFzdPAfpoGUAxa3k:A9YwiedKhukPGmzNduGmZ7Q:C; BDUSS=hxOX5aOTBRenNjMktUYVRmTVF1MkIzfk9JVlo3d1o4OEI2eWF5NFlxbXNld2RqSVFBQUFBJCQAAAAAAAAAAAEAAAD3wLCSv8m28bXE08O7p8P7dG0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKzu32Ks7t9ifl; BDUSS_BFESS=hxOX5aOTBRenNjMktUYVRmTVF1MkIzfk9JVlo3d1o4OEI2eWF5NFlxbXNld2RqSVFBQUFBJCQAAAAAAAAAAAEAAAD3wLCSv8m28bXE08O7p8P7dG0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKzu32Ks7t9ifl; __bid_n=1839e1601deb7fac284207; FEID=v10-e13d2878b793b3f539000e6963583183b6ae06f2; __xaf_fpstarttimer__=1672927781807; __xaf_thstime__=1672927782004; __xaf_fptokentimer__=1672927782005; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1675058456; FPTOKEN=IFa1nV0MtYmiJHZ4pbRL/gbesnwzaZWjhoDgt7ttOHwaFb2DbJyCwibTlHy/uCelUciOgfJo/4vXXk3AeEvf/0pupLifLkZUdcYTS7m9L5E7XeciMxehHV2FmRWYnydH9FUTssC3AhWWJn6inBNaauA5d1grDsBuY6XuMoqafy8kkQjbTqvzzC6ZfE33MYtlvsk0oA/hOyu2H3b/gMetsJZkqX+2WGPGN50YkTZ9BpqHmRMAXuFYFio7vpgW9KxBJIgJdqZKiYYTG7X7dFnaCdJ9dQQ9KoZ2psJpTpYHzCBPKA91CQIbCXGayJjazt0eE/redp7QEPP7B5ml2dA5mbiisInEQOGkikHRUmaEbS4utuApeI2Hu4vzMRVTRfv165itaB8B779niOBCrp/FHA==|RiZb36RpvgMqY0oMxFeaDFGYeen074clWlj97DRICD0=|10|994de9a00f7ee72b654ca31137739ec0; RT="z=1&dm=baidu.com&si=umc4f80x0f7&ss=ldieq6r6&sl=5&tt=37b&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=bn9&ul=csn&hd=ctu"; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1675167909; ab_sr=1.0.1_ZmFiOWFlYTJiNDcyMTJhNDhiMzVjNTAyZjU0MGQxMWRhNjE1ZmJjNDdlZjQ4NzhiZmNmMTFiNGQ4YWJmNWNkODFiNTY2ZjJhZWUzYzRhZjQzZmVkODRkMjgxMTg1NDQzY2IwOTkzYjAzNzMxYjc2NDdkNTc4Mzg2ZjJlMzI2NzAyNGNmYzNkMDQxYTlmN2M1YzcyNmY4ZDY1YzAyZjU5NGYxNmY2YTVhYjc4ZTg0OTg2OWI4Y2FkMWZkMWRmZjMx',
    # 'Host': ' fanyi.baidu.com',
    # 'Origin': ' https://fanyi.baidu.com',
    # 'Referer': ' https://fanyi.baidu.com/',
    # 'sec-ch-ua': ' "Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    # 'sec-ch-ua-mobile': ' ?0',
    # 'sec-ch-ua-platform': ' "macOS"',
    # 'Sec-Fetch-Dest': ' empty',
    # 'Sec-Fetch-Mode': ' cors',
    # 'Sec-Fetch-Site': ' same-origin',
    # 'User-Agent': ' Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    # 'X-Requested-With': ' XMLHttpRequest',
}

data = {
    'from': 'en',
    'to': 'zh',
    'query': 'l',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '501460.214501',
    'token': 'd86b16811497af1dec862f96200a39b4',
    'domain': 'common',
}

# post请求参数进行编码和调用eccode
data = urllib.parse.urlencode(data).encode('utf-8')

# 请求对象定制
request = urllib.request.Request(url=url, headers=headers, data=data)

# 模拟浏览器发送请求
response = urllib.request.urlopen(request)

# 获取响应数据
content = response.read().decode('utf-8')

import json

obj = json.loads(content)

print(obj)
