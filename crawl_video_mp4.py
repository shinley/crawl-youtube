# encoding=UTF-8

# 爬取视频和字幕

from selenium import webdriver
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
                # dl_btn = browser.find_element_by_class_name('.sf-quick-dl-btn')[0]
                dl_btn = browser.find_elements_by_class_name('sf-quick-dl-btn')[0]
            except Exception as e:
                time.sleep(3)
                continue

            if not dl_btn:
                continue
            dl_btn.click()
            time.sleep(300)
            break
