# -*- coding:utf-8 -*-

import time

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup

# option
chrome_options = Options()
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--hide-scrollbars')
chrome_options.add_argument("--proxy-server=socks5://127.0.0.1:9050")
chrome_options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36')

CHROME_DRIVER = './chromedriver'
URL = ""

with webdriver.Chrome(CHROME_DRIVER, options=chrome_options) as driver:
    try:
        driver.set_page_load_timeout(600)
        driver.get(URL)
        time.sleep(10)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        main_board = soup.find_all('div', attrs={'class': "post-block bad", "onclick":True})
        number = 0
        for post in main_board:
            number = number + 1
            xpath_id = f"/html/body/div[3]/div[1]/div/div[{str(number)}]"

            try:
                title = post.find("div", {"class": "post-title"}).text.strip()
                victim = title
                victim_url = title
                print(title, victim, victim_url)
            except Exception as e:
                traceback.print_exc()
                pass

            driver.find_element_by_xpath(xpath_id).screenshot(f'./capture/{number}.png')
            print("[+] Screenshot!", flush=True)

    except Exception as e:
        print("{}".format(e))

