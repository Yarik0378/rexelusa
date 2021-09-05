import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from scrape_page import read_html
import time
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()

options.add_argument("start-maximized")

driver = webdriver.Chrome(chrome_options=options)

wait = WebDriverWait(driver, 8)

email = 'mamiwep480@mtlcz.com'

password = '2tuGbumJikydcyX'


def drv_pg():
    try:
        driver.execute_script(
            'var elems = document.getElementsByClassName("v-btn v-btn--icon v-btn--round theme--light '
            'v-size--default"); elems[1].click();')
        time.sleep(1)
        driver.execute_script(
            'var elems = document.getElementsByClassName("v-btn v-btn--icon v-btn--round theme--light '
            'v-size--default");elems[2].click();')
    except:
        pass
    return driver.page_source


def get_html(link):
    driver.get(link)
    return driver.page_source


def logination():
    driver.get(
        'https://auth.rexelusa.com/login?returnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fprotocol%3Doauth2%26response_type%3Dcode%26access_type%3Doffline%26client_id%3Dstorefront-web-v2%26redirect_uri%3Dhttps%253A%252F%252Fwww.rexelusa.com%252Fcallback%26scope%3Dsf.web%2520offline_access%26state%3D_UVQGIVLvtX6-yxnclfcM%26code_challenge_method%3DS256%26banner%3DREXEL%26code_challenge%3D4WTc-tGmrIxql0BTWvj5sOl0C5COWTt6WPVv4YO4kSU')
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "input[type='email']")))
    driver.find_element_by_css_selector("input[type='email']").send_keys(email)
    driver.find_element_by_css_selector("button[type='button']").click()
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "input[type='password']")))
    driver.find_element_by_css_selector("input[type='password']").send_keys(password)
    try:
        for i in range(5):
            driver.find_element_by_css_selector(
                "button[class='px-10 v-btn v-btn--is-elevated v-btn--has-bg v-btn--tile theme--light v-size--large primary']").click()
            # driver.find_elements_by_css_selector(".v-btn__content']")[1].click()
            time.sleep(1)
    except:
        pass
    driver.get('https://www.rexelusa.com/p/36229/hubbell-raco/4-square-box-welded-metallic-2-1-8-deep/050169902325/232')
    driver.find_element_by_css_selector('div[class="v-list py-0 mr-4 v-sheet theme--dark v-list--dense accent"]').click()
    wait.until(ec.visibility_of_element_located(
        (By.CSS_SELECTOR, "div[class='v-list py-0 mr-4 v-sheet theme--dark v-list--dense accent']")))


def get_img():
    img = ''
    driver.find_element_by_css_selector('div.product-gallery.col.col-5 div div ~ div img').click()
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "div.v-image.v-responsive.theme--light")))
    x = 1
    while True:
        try:
            html = BeautifulSoup(driver.page_source, 'lxml')
            img += html.select_one('div.v-image.v-responsive.theme--light a').get('href') + ' \n '
            driver.find_elements_by_css_selector('.row.row--dense.justify-center div.col.col-auto')[x].click()
            x += 1
        except:
            break
    return img


def main():
    logination()
    while True:
        link = input('Please enter your link: ')
        html = get_html(link)
        substitutes = drv_pg()
        img_s = get_img()
        read_html(html, substitutes, img_s)


if __name__ == '__main__':
    main()
