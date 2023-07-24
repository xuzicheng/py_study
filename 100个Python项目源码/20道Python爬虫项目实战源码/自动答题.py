"""

[课    题]：Python 爬虫外包项目--自动答题模拟考试

[难度指数]: ☆☆☆(满级难度十颗星)  价值1000外包项目

[讲    师]: 青灯教育--益达

[授课时间]: 19:35

[使用环境]: Anaconda (python3.9) 解释器 识别我们写的代码
配置环境
[开发工具]: pycharm  编辑器

[使用模块]: requests >>> pip install requests   <第三方模块>
           selenium >>> pip install selenium   <第三方模块>
           parsel >>> pip install parsel       <第三方模块>
           time                                <内置模块>




[软件没安装?]
找到给你发上课链接的老师领取
Anaconda / python3.9 / pycharm(专业破解版/社区版) 安装包以及安装视频教程


[听不懂? 没基础?]
屏幕右上角是助教[玲玲老师]的微信 可扫码添加 添加以后可以找到[玲玲老师]领取:
I. 本节课源码 (没基础的同学主要学习编程的思路逻辑, 不建议一起敲代码)
II.领取0基础的视频教程一套 (基础编程 and 爬虫基础)


采集数据 下载
数据的采集  自动化的脚本
selenium 模拟人的行为
selenium --> 浏览器的驱动 ---> 浏览器窗口 下载浏览器的驱动 版本 谷歌 火狐 全局变量  项目环境

打开浏览器的窗口 -> 输入(搜索关键字) --> 读取窗口信息 ---> 下载(答题) ----> 关闭浏览器的窗口

三个班级
① 训练营  2天 某一个特定课题 一周的解答辅导 学习群 9.9 高清录播 5年有效


② 兴趣班  爬虫/数据分析  做兼职  学习周期 3-4个月 高清录播  终身有效  解答周期是一年 提供外包指导 外包的平台
    3880 可以找到我们玲玲老师 办理免息的分期 3 6 9 12  学的方向去找工作 也是可以的
③ 就业班  7个月  爬虫 数据分析 网页开发 人工智能 自动化办公  直接就业 8k-15k 解答服务是2年  可以免费重修
录播终身有效的 提供外包指导 外包的平台 就业指导 简历修改 就业推荐  8080 3 6 9 12 18

一周3节课 135 或 246  晚上8点-晚上10点 有问题当堂解决
每节课都会布置作业 7点半-8点 讲解作业 提交到老师的邮箱  集中解决


"""

# 导入浏览器对象
from selenium import webdriver
# 导入时间模块
import time
# 导入元素定位功能
from selenium.webdriver.common.by import By
# driver.find_element_by_css_selector() 4 一定会报错 弃用 3
# 导入数据请求模块
import requests
# 数据解析模块
import parsel


# 实例化一个浏览器对象
driver = webdriver.Chrome()

# 打开浏览器的窗口
driver.get('https://www.jsyks.com/kmy-mnks')
# 强制等待
time.sleep(2)
# 最大化浏览器的窗口
driver.maximize_window()
# 隐式等待  智能
driver.implicitly_wait(10)

# elements 返回的是一个列表对象
lis = driver.find_elements(By.CSS_SELECTOR, '.Content>li')
# print(len(lis))
# print(lis)
for li in lis:
    time.sleep(0.2)  # 优先考虑使用随机数
    rid = li.get_attribute('c')
    # print(rid)
    url = f'https://tiba.jsyks.com/Post/{rid}.htm'
    # 获取到响应体对象的文本数据
    response = requests.get(url=url).text
    # 转对象
    selector = parsel.Selector(response)
    answer = selector.css('#question u::text').get()
    # print(answer)
    # 重新赋值
    if answer == '对':
        answer = '正确'
    elif answer == '错':
        answer = '错误'
    # else:  不确定的情况
    # print(answer)
    bs = li.find_elements(By.CSS_SELECTOR, 'B')
    for b in bs:
        # 获取选项的内容
        choose = b.text
    #     print('题目的选项是', choose)
    # print('正确答案是', answer)
        # 可能错题
        # if answer in choose:
        #     # 正确答案的点击操作
        #     b.click()
        if len(choose) > 2:
            choose = choose[0]
        if answer == choose:
            b.click()

# 提交试卷
driver.find_element(By.CSS_SELECTOR, '.btnJJ').click()






# 添加阻塞
input()

# 关闭浏览器
driver.quit()