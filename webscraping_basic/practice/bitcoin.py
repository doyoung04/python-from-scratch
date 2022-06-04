from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_until(xpath_str):
    WebDriverWait(browser, 30).until(EC.presence_of_all_elements_located((By.XPATH, xpath_str)))

options = webdriver.ChromeOptions()
# options.headless = True
options.add_argument("window-size=2056x1329")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36")

browser = webdriver.Chrome("/Users/KDY/Workspace/python/python-from-scratch/webscraping_basic/practice/chromedriver", options=options)
# browser.maximize_window()

url = "https://upbit.com/exchange?code=CRIX.UPBIT.KRW-BTC"
browser.get(url)

wait_until("//em[text() = 'KRW']")
bitcoin_value = browser.find_element(By.XPATH, "//*[@id='UpbitLayout']/div[3]/div/section[1]/article[1]/div/span[1]/div[1]/span[1]/strong")
print(bitcoin_value)
browser.quit()