from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--proxy-server=socks5://127.0.0.1:9050")
driver = webdriver.Chrome(executable_path='./chromedriver',options=chrome_options)

#Search
driver.get('https://ipinfo.io/json')
html = driver.page_source
print(html)
