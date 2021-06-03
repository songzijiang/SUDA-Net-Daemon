import time
import json

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

url = 'https://www.wjx.cn/vj/Ocur3x5.aspx'

chrome_options = Options()
# 设置chrome浏览器无界面模式
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

chrome = webdriver.Chrome(
    executable_path='chromedriver91.exe'
    , chrome_options=chrome_options)
chrome.get(url)


def submit(num, n):
    # 选择'普通登录'
    # chrome.find_element_by_xpath('//*[@id="edit_body"]/div[1]/div[3]/div/div[1]/span[1]').click()

    number_input_xpath = "/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='ctl00_ContentPlaceHolder1_JQ1_surveyContent']/fieldset[@id='fieldset1']/div[@id='div1']/div[@id='divquestion1']/textarea[@id='q1']"
    name_input_xpath = "/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='ctl00_ContentPlaceHolder1_JQ1_surveyContent']/fieldset[@id='fieldset1']/div[@id='div2']/div[@id='divquestion2']/textarea[@id='q2']"
    submit_bt_xpath = "/html/body/div[@id='jqContent']/div[@class='box']/div[@id='mainCss']/div[@id='mainInner']/div[@id='box']/div[@class='survey']/div[@id='ctl00_ContentPlaceHolder1_JQ1_question']/div[@id='submit_div']/table[@id='submit_table']/tbody/tr/td[1]/input[@id='submit_button']"

    number_input = chrome.find_element_by_xpath(number_input_xpath)
    name_input = chrome.find_element_by_xpath(name_input_xpath)
    submit_bt = chrome.find_element_by_xpath(submit_bt_xpath)
    number_input.clear()
    name_input.clear()
    number_input.send_keys(num)
    name_input.send_keys(n)

    # chrome.execute_script('arguments[0].click()', submit_bt)
    # ActionChains(driver=chrome).move_to_element(login_bt).click(login_bt)
    # login_bt.click()


if __name__ == '__main__':
    file_path = 'account.json'
    with open(file_path, 'r', encoding='utf8') as f:
        obj = json.load(f)
    account = obj['account']
    password = obj['password']
    number = obj['number']
    name = obj['name']
    submit(number, name)
