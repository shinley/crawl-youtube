# encoding=UTF-8

# 爬取视频和字幕

from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
# option.add_argument('--headless')
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-shm-usage')

option.add_argument('--user-data-dir=/Users/shinley/Library/Application Support/Google/Chrome')


with open('video_url.txt', 'r') as video_url:
    browser = webdriver.Chrome(chrome_options=option)
    while True:
        line = video_url.readline()
        if not line:
            break

        url = "https://www.youtube.com" + line
        # browser.execute_script("window.open('" + url.strip() + "', '_blank');")
        browser.set_page_load_timeout(20)
        browser.set_script_timeout(20)
        try:
            browser.get(url)
        except TimeoutError as e:
            browser.refresh()
        time.sleep(3)

        # handles = browser.window_handles
        # browser.switch_to.window(handles[0])
        # browser.close()
        # browser.switch_to.window(handles[0])
        retries = 0
        while True:
            retries = retries + 1
            try:
                ui.WebDriverWait(browser, 60).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="savefrom__yt_btn"]/a')))
                dl_btn = browser.find_elements_by_class_name('sf-quick-dl-btn')[0]
                a_ele = browser.find_element_by_xpath('//*[@id="savefrom__yt_btn"]/a')
                href = a_ele.get_attribute('href')
                name = a_ele.get_attribute('download')
                print(href)
                print(name)
                # selecter = browser.find_element_by_id('captions_selector')
                time.sleep(5)
            except Exception as e:
                if retries >= 3:
                    print(line)
                    break
                browser.refresh()  # 刷新页面
                time.sleep(3)
                continue

            dl_btn.click()                         # 单击下载视频
            time.sleep(120)
            break

    browser.quit()
