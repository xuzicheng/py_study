"""
[使用模块]: requests >>> pip install requests        <第三方模块>
           parsel >>> pip install parsel            <第三方模块>
           prettytable >>> pip install prettytable  <第三方模块>
"""
import requests  # 第三方的模块
import parsel  # 第三方的模块
import os  # 内置模块 文件或文件夹
import prettytable as pt

filename = '小说\\'
if not os.path.exists(filename):
    os.mkdir(filename)

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}

def get_main(rid):
    link = f'https://www.bqg70.com/book/{rid}/'

    html_data = requests.get(url=link, headers=headers).text
    # print(html_data)
    selector_2 = parsel.Selector(html_data)
    divs = selector_2.css('.listmain dd')
    for div in divs:
        title = div.css('a::text').get()
        href = div.css('a::attr(href)').get()
        url = 'https://www.bqg70.com' + href
        try:
            response = requests.get(url=url, headers=headers)
            selector = parsel.Selector(response.text)
            # getall 返回的是一个列表 []
            book = selector.css('#chaptercontent::text').getall()
            book = '\n'.join(book)
            # 数据保存
            with open(filename + title + '.txt', mode='a', encoding='utf-8') as f:
                f.write(book)
                print('正在下载章节:  ', title)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    word = input('请输入你要下载的小说的名字: ')
    url = f'https://www.bqg70.com/s?q={word}'
    html_data_ = requests.get(url=url, headers=headers).text
    # print(html_data_)
    selector_3 = parsel.Selector(html_data_)
    lis = selector_3.css('.bookbox')
    book_list = []
    num = 0
    tb = pt.PrettyTable()
    tb.field_names = ['编号', '书名', '作者', 'ID']
    for li in lis:
        rid = li.css('.bookname>a::attr(href)').get().split('/')[-2]
        book_name = li.css('.bookname>a::text').get()
        author = li.css('.author::text').get().replace('作者：', '')
        # print(rid, book_name, author)
        d = {
            '书名': book_name,
            '作者': author,
            'ID': rid
        }
        book_list.append(d)
        tb.add_row([num, book_name, author, rid])
        num += 1

    print(tb)
    key_word = input('请输入你要下载的小说编号: ')
    book_id = book_list[int(key_word)]['ID']
    get_main(book_id)