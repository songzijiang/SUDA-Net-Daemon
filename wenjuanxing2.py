import asyncio
from pyppeteer import launch
from pyppeteer_stealth import stealth
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import re
import time
url = "https://www.wjx.cn/vj/Ocur3x5.aspx"  #测试网址

name = "问卷星"
number = "11012011966"

async def run():
    driver = await launch({

        # 谷歌浏览器的安装路径
        'executablePath': r'C:\Program Files\Google\Chrome\Application\chrome.exe',
        # Pyppeteer 默认使用的是无头浏览器
        'headless': False,
        # 设置Windows-size和Viewport大小来实现网页完整显示
        'args': ['--no-sandbox', '--window-size=1024,768', '--disable-infobars'],
        'dumpio': True,
    })

    # 用 newPage 方法相当于浏览器中新建了一个选项卡,同时新建了一个Page对象
    page = await driver.newPage()
    #简称换头
    await page.setUserAgent(
        UserAgent().random)

    await page.setViewport({
   'width': 1024, 'height': 768})
    # 反爬虫跳入网页
    await stealth(page)
    await page.goto(url)   #问卷星网址

    page_text = await page.content()  # 获取网页源码

    ''' 下面的都是对文本的判断，大佬们直接忽略自己写就行了。 '''

    Soup = BeautifulSoup(page_text, 'lxml')
    list_judge_email = []  # 位置
    list_ques = Soup.find_all(text=re.compile("姓名"))
    list_ques.extend(Soup.find_all(text=re.compile("学号")))
    print(list_ques)

    for i in list_ques:

        if len(i) > 20:        #有某些含有qq字眼但是却不是问题，直接排除
            continue
        print(i + "----------------")
        if '姓名' in i:
            da_name = 'q' + i[0]
        if 'qq' in i or 'QQ' in i:
            da_qq = 'q' + i[0]

    #定义在函数体内运行结束会直接退出浏览器，所以需要延时让我们完成时间段的选择，并提交
    time.sleep(200)

asyncio.get_event_loop().run_until_complete(run())