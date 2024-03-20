import automate
#要素がない場合のエラーハンドリング
from selenium.common.exceptions import NoSuchElementException

#くじURLリスト
kujiUrlList = [
    'https://kuji.rakuten.co.jp/7393386d27',
    'https://books.rakuten.co.jp/event/luckly-kuji/?scid=wi_grp_gmx_bks_rjl',
    'https://kuji.rakuten.co.jp/889373540e',
    'https://hoken.rakuten.co.jp/redirect/luckykuji.html?scid=wi_kuji_list',
    'https://dining.rakuten.co.jp/campaign/kuji/?scid=wi_grp_gmx_rkg_rjl',
    'https://recipe.rakuten.co.jp/sp1/kuji/top/?scid=we_rcp_kujilist',
    'https://dream.rakuten.co.jp/luckykuji/?scid=wi_grp_gmx_drm_kuji_list',
    'https://kuji.rakuten.co.jp/4351057845/?scid=wi_grp_gmx_too_rjl',
    'https://kuji.rakuten.co.jp/6e7329f994',
    'https://kuji.rakuten.co.jp/18584163d',
    'https://kuji.rakuten.co.jp/c8437c01c5',
    'https://kuji.rakuten.co.jp/46211bf9dd',
    'https://r10.to/hVMGy4',
    'https://kuji.rakuten.co.jp/26e390eccf?scid=wwkuji_rakuma_luckylottery',
    'https://kuji.rakuten.co.jp/5f93b1fd01',
    'https://kuji.rakuten.co.jp/3373caeddb'
]

#useID
userID = 'YourUserID'
#pass
password = 'YourPassword'

#指定のURLのくじを引く関数
def openKujiBrowser(selenium, url):
    try:
        #指定URLにアクセス
        selenium.access(url)
        #ページ読み込みの為遅延させる
        selenium.stop(5)
        #くじ開始ボタンの要素をセット
        selenium.find_element_xpath("//*[@id='entry']")
        #くじ開始ボタンをクリック
        selenium.click()
        #くじの実行時間の為に遅延させる
        selenium.stop(20)
        #ポップアップ広告を閉じる
        selenium.close_popup_ad()
    #要素がない場合のエラーハンドリング
    except NoSuchElementException:
        print("くじを引くための要素が見つかりませんでした")
        selenium.stop(1)

#seleniumに関するinstance生成を行う
selenium = automate.Selenium()
#楽天ログインページに移動
selenium.access('https://grp01.id.rakuten.co.jp/rms/nid/vc?__event=login&service_id=top')
#ページ読み込みの為遅延させる
selenium.stop(5)


#楽天にログイン
try:
    #userIDの要素をセット
    selenium.find_element('loginInner_u')
    #userIDに値を格納
    selenium.set_value(userID)
    #passの要素をセット
    selenium.find_element('loginInner_p')
    #passの値をセット
    selenium.set_value(password)
    #ログインボタンの要素をセット
    selenium.find_element_css_name('input.loginButton[type="submit"][value="ログイン"]')
    #ログインボタンをクリック
    selenium.click()
except NoSuchElementException:
    print("ログイン要素が見つかりませんでした")
#ページ読み込みの為遅延させる
selenium.stop(5)
#くじのURLリストを開く
for url in kujiUrlList:
    openKujiBrowser(selenium, url)

#処理終了
selenium.quit()
print("終了しました")
