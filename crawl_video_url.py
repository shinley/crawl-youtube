# encoding=UTF-8
from selenium import webdriver
import time
from lxml import etree

option = webdriver.ChromeOptions()
option.add_argument('--headless')
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-shm-usage')

# option.binary_location = '/opt/google/chrome/google-chrome'
# option.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/google chrome'

option.add_argument("--proxy-server=http://127.0.0.1:7890")
# url = 'http://quote.eastmoney.com/concept/sz000735.html'
url = 'https://www.youtube.com/user/theteachervanessa/videos'
# url = 'https://www.baidu.com'
browser = webdriver.Chrome(chrome_options=option)
browser.get(url)
time.sleep(3)
# soup = BeautifulSoup(driver.page_source, 'lxml')

# 获取页面初始高度
js = 'return action=document.getElementsByTagName("ytd-app")[0].scrollHeight'
height = browser.execute_script(js)

# 将滚动条调整至页面底部
browser.execute_script('window.scrollTo(0, document.getElementsByTagName("ytd-app")[0].scrollHeight)')
time.sleep(5)

# 重试次数
num = 0

#定义初始时间戳（秒）
t1 = int(time.time())

#定义循环标识，用于终止while循环
status = True

print("#############循环下拉############")

while status:
    browser.execute_script('window.scrollTo(0, document.getElementsByTagName("ytd-app")[0].scrollHeight)')
    new_height = browser.execute_script(js)
    time.sleep(3)
    if new_height > height:
        # 重置初始页面高度
        height = new_height
        continue
    else:
        if num < 3:  # 当超过30秒页面高度仍然没有更新时，进入重试逻辑，重试3次，每次等待30秒
            time.sleep(3)
            num = num + 1
            continue
        else:  # 超时并超过重试次数，程序结束跳出循环，并认为页面已经加载完毕！
            print("滚动条已经处于页面最下方！")
            status = False
            # 滚动条调整至页面顶部
            # browser.execute_script('window.scrollTo(0, 0)')
            break
    print("第 " +str(num)+ "次")

# 打印页面源码
content = browser.page_source
print(content)
html = etree.HTML(content)
html_data = html.xpath('//*[@id="details"]//*[@id="video-title"]//text()')

with open('video_name.txt', 'w') as f:
    for data in html_data:
        f.writelines(data + "\n")

url_data = html.xpath('//*[@id="details"]//*[@id="video-title"]/@href')
with open('video_url.txt', 'w') as f:
    for ud in url_data:
        f.writelines(ud + "\n")

