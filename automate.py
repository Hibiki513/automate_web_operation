import time
from selenium import webdriver
#最新のchromeのversionに合わせる為
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class Selenium:
    driver = None
    element = None

    def __init__(self):
        options = webdriver.ChromeOptions()
        #ブラウザを開くことなくバックグラウンドで実行する
        #options.add_argument('--headless')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        #ブラウジングするwindow幅を設定する
        self.driver.set_window_size(1000,740)

    def access(self,url):
        self.driver.get(url)

    def find_element(self,name):
        self.element = self.driver.find_element(By.ID,name)

    def find_element_css_name(self,name):
        self.element = self.driver.find_element(By.CSS_SELECTOR, name)
    
    def find_element_xpath(self,name):
        self.element = self.driver.find_element(By.XPATH, name)
    
    def set_value(self,value):
        self.element.send_keys(value)

    def click(self):
        try:
            self.element.click()
        except Exception as e:
            print("要素をクリックできませんでした", e)

    def stop(self,num):
        time.sleep(num)

    def quit(self):
            self.driver.quit()

    #ポップアップ広告を閉じる
    def close_popup_ad(self):
        try:
            popup_close_button = self.driver.find_element(By.CLASS_NAME)
            popup_close_button.click()
            self.stop(2)
        except:
            pass