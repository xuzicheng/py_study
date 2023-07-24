# 1:请求对象定制
# 2：获取网页源码
# 3：下载

# 下载前十页图片
# https://sc.chinaz.com/tupian/qinglvtupian.html
# https://sc.chinaz.com/tupian/qinglvtupian_2.html
# https://sc.chinaz.com/tupian/qinglvtupian_3.html

import urllib.request
from lxml import etree


def create_request(page):
    if (page == 1):
        url = 'https://sc.chinaz.com/tupian/qinglvtupian.html'
    else:
        url = 'https://sc.chinaz.com/tupian/meinvxiezhen_' + str(page) + '.html'

    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def down_load(content):
    tree = etree.HTML(content)
    # 下载图片
    # urllib.request.urlretrieve('图片地址','文件名字')
    name_list = tree.xpath('//div[@class="tupian-list com-img-txt-list masonry"]//div/img/@alt')
    src_list = tree.xpath('//div[@class="tupian-list com-img-txt-list masonry"]//div/img/@data-original')
    for i in range(len(name_list)):
        name = name_list[i]
        src = src_list[i]
        url = 'https:' + src
        urllib.request.urlretrieve(url=url, filename=name + '.jpg')


if __name__ == '__main__':
    start_page = int(input('请输入起始页码'))
    end_page = int(input('请输入结束页码'))

    for page in range(start_page, end_page + 1):
        # 请求对象定制
        request = create_request(page)
        content = get_content(request)
        down_load(content)
