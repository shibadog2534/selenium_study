from selenium import webdriver
from selenium.webdriver.chrome.options import Options


#ヘッドレス（GUIの非表示）
#options=Options()
#options.add_argument('--headless')

#wb = webdriver.Chrome(options=options)
wd = webdriver.Chrome()
url='https://www.yahoo.co.jp/'
wd.get(url)

elementTEXTBOX=wd.find_element_by_name("p")
elementTEXTBOX.send_keys("ラーメン")
#以下の書き方でも可能
#elementTEXTBOX=wd.find_element_by_name("p").send_keys("ラーメン")


#検索ボタンにIDやNameが振られていない場合はxpathで指定できる
#ソース特定後に右クリからxpathをコピー
elementBTN=wd.find_element_by_xpath("//*[@id=\"ContentWrapper\"]/header/section[1]/div/form/fieldset/span/button/span/span")
elementBTN.click()
#以下の書き方でも可能
#elementBTN=wd.find_element_by_xpath("//*[@id=\"ContentWrapper\"]/header/section[1]/div/form/fieldset/span/button/span/span").click()


