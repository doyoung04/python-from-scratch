import time
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}
url = "https://www.google.com/finance/quote/NVDA:NASDAQ?sa=X&ved=2ahUKEwjWj_r06533AhVvpVYBHU1uBCQQ3ecFegQIIxAa"
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")
price_old = soup.find("div", attrs={"class":"YMlKec fxKbKc"})

while True:
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    price_new = soup.find("div", attrs={"class":"YMlKec fxKbKc"})
    
    if price_old == price_new:
        time.sleep(1)
    else:
        now = time.localtime()
        print("%02d:%02d:%02d" % (now.tm_hour, now.tm_min, now.tm_sec), price_new.get_text())
        price_old = price_new
