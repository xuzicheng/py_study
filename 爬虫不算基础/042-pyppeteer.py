import asyncio

import pyppeteer
from pyppeteer import launch
from pyquery import PyQuery as pq


async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://dynamic2.scrape.center/')
    await page.waitForSelector('.item .name')
    doc = pq(await page.content())
    names = []
    for item in doc('.item .name').items():
        names.append(item.text())

    print('Names:', names)
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())

# 这段 Python 代码使用 Pyppeteer 库来启动一个 Headless Chrome 浏览器实例，然后通过它来爬取一个动态生成的网页 https://dynamic2.scrape.center/。具体来说，代码中：
#
# 首先通过 launch() 方法启动一个 Headless Chrome 浏览器实例；
# 然后通过 browser.newPage() 方法创建一个新的页面对象；
# 接着通过 page.goto() 方法让页面跳转到目标 URL，等待页面加载完成；
# 继而通过 page.waitForSelector() 方法等待页面上指定 CSS 选择器所代表的元素加载完成；
# 最后通过 page.content() 方法获取页面的 HTML 内容，并使用 PyQuery（pq）进行解析和操作，从中提取出所有商品的名字，并打印输出；
# 最后通过 browser.close() 方法关闭浏览器实例，释放资源。
# 由于使用了异步编程，因此主函数中使用了 asyncio.get_event_loop().run_until_complete() 来运行整个协程，使得代码能够按照顺序逐步执行。
