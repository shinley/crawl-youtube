# encoding=UTF-8

# 爬取视频和字幕

from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
from lxml import etree

option = webdriver.ChromeOptions()
# option.add_argument('--headless')
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-shm-usage')

option.add_argument('--user-data-dir=/Users/shinley/Library/Application Support/Google/Chrome')


with open('video_url.txt', 'r') as video_url:
    while True:
        line = video_url.readline()
        if not line:
            break

        url = "https://www.youtube.com" + line
        browser = webdriver.Chrome(chrome_options=option)
        browser.get(url)

        time.sleep(3)

        while True:
            try:
                dl_btn = browser.find_elements_by_class_name('sf-quick-dl-btn')[0]
                selecter = browser.find_element_by_id('captions_selector')
                Select(selecter).select_by_index("1") # 选中第2个(索引为1)自动下载
            except Exception as e:
                time.sleep(3)
                continue

            if not dl_btn:
                continue
            dl_btn.click()          # 单击下载视频

            time.sleep(300)
            break
