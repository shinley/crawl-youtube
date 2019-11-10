# encoding=UTF-8

# 爬取视频和字幕
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains

option = webdriver.ChromeOptions()
# option.add_argument('--headless')
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-shm-usage')

option.add_argument('--user-data-dir=/Users/shinley/Library/Application Support/Google/Chrome')



url = "https://www.baidu.com"
browser = webdriver.Chrome(chrome_options=option)
browser.get(url)
time.sleep(3)

browser.execute_script("window.open('https://www.163.com', '_blank');")
time.sleep(2)

handles = browser.window_handles
browser.switch_to.window(handles[0])

browser.close()

time.sleep(2)