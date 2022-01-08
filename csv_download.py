from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import os


#ポータルサイトのログイnIDとパスワード
loginID=''
loginPW=''


wd = webdriver.Chrome()
url='https://www.data.jma.go.jp/obd/stats/data/mdrr/docs/csv_dl_format_sndall.html'
wd.get(url)

#ここにログインフォームの要素記述


# リンククリック
elementLINK=wd.find_element_by_xpath("//*[@id=\"main\"]/ul/li/a").click()

#毎朝複数のページを移動して必要なCSVを確保
#リンクの名称は固定されている
#各ページ内のCSVダウンロードリンクは１つのみ（//*[@id=\"main\"]/ul/li/a" 流用可能
elementLINK = wd.find_element_by_partial_link_text('CSVダウンロードについて').click()
elementLINK = wd.find_element_by_partial_link_text('最深積雪').click()
elementLINK=wd.find_element_by_xpath("//*[@id=\"main\"]/ul/li/a").click()
#必要分繰り返し

time.sleep(2)
wd.quit()