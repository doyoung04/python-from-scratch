# """ 1~3 """
# import requests

# res = requests.get("https://www.google.com")
# res.raise_for_status() # 문제가 생기면 에러를 뱉고 프로그램 종료, 보통 두 줄을 쌍으로 사용
# # print(res.status_code) # 200이면 정상, 403이면 권한 없음

# # if res.status_code == requests.codes.ok:
# #     print("정상입니다.")
# # else:
# #     print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")

# print(len(res.text))
# # print(res.text)

# with open("mygoogle.html", "w", encoding="utf8") as f:  
#     f.write(res.text)

# """ 4 """
# import re
# # ca?e
# p = re.compile("ca.e")
# # . (ca.e): 하나의 문자를 의미 > care, cafe, case (o) | caffe (x)
# # ^ (^de) : 문자열의 시작 > desk, destination (o) | fade (x)
# # $ (se$) : 문자열의 끝 > case, base (o) | face (x)

# # m = p.match("case")
# # # m = p.match("casse")
# # # print(m.group()) # 매치되지 않으면 에러가 발생
# # if m:
# #     print(m.group())
# # else:
# #     print("매칭되지 않음")

# def print_match(m):
#     if m:
#         print(m.group()) # 일치하는 문자열 반환
#         print(m.string)  # 입력받은 문자열 반환
#         print(m.start()) # 일치하는 문자열의 시작 index
#         print(m.end())   # 일치하는 문자열의 끝 index
#         print(m.span())  # 일치하는 문자열의 시작/끝 index
#     else:
#         print("매칭되지 않음")

# # m = p.match("case")
# # print_match(m)

# # m = p.match("careless") # match: 주어진 문자열의 처음부터 일치하는지 확인
# # print_match(m)

# # m = p.search("good care") # search: 주어진 문자열 중 일치하는게 있는지 확인
# # print_match(m)

# lst = p.findall("good care cafe") # findall: 일치하는 모든 것을 리스트 형태로 반환
# print(lst)

# """ 5 """
# import requests
# url = "https://nadocoding.tistory.com"
# headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36"}
# res = requests.get(url, headers=headers)
# res.raise_for_status()
# with open("nadocoding.html", "w", encoding="utf8") as f:  
#     f.write(res.text)

# """ 6 """
# import requests
# from bs4 import BeautifulSoup

# url = "https://comic.naver.com/webtoon/weekday"
# res = requests.get(url)
# res.raise_for_status()

# soup = BeautifulSoup(res.text, "lxml")
# # print(soup.title)
# # print(soup.title.get_text())
# # print(soup.a) # soup 객체에서 첫 번째 a을 출력
# # print(soup.a.attrs) # a element의 속성 정보를 출력
# # print(soup.a["href"]) # a element의 href 속성 값을 출력

# # soup.find("a", attrs={"class":"Nbtn_upload"}) # a element에서 class가 Nbtn_upload인 것만 찾음
# # print(soup.find("a", attrs={"class":"Nbtn_upload"}))
# # print(soup.find(attrs={"class":"Nbtn_upload"})) # 웹툰 올리기 태그가 하나밖에 없기 때문에 가능

# # print(soup.find("li", attrs={"class":"rank01"}))
# # rank1 = soup.find("li", attrs={"class":"rank01"})
# # print(rank1.a)

# # print(rank1.a.get_text())
# # print(rank1.next_sibling)
# # rank2 = rank1.next_sibling.next_sibling
# # rank3 = rank2.next_sibling.next_sibling
# # print(rank3.a.get_text())
# # rank2 = rank3.previous_sibling.previous_sibling
# # print(rank2.a.get_text())
# # print(rank1.parent)

# # rank2 = rank1.find_next_sibling("li") # rank1 기준으로 다음 항목을 찾는데 li인 것만 찾음
# # print(rank2.a.get_text())
# # rank3 = rank2.find_next_sibling("li")
# # print(rank3.a.get_text())
# # rank2 = rank3.find_previous_sibling("li")
# # print(rank2.a.get_text())

# # print(rank1.find_next_siblings("li")) # rank1 기준으로 모든 형제들을 찾는데 li인 것만 찾음

# webtoon = soup.find("a", text="연애혁명-393. 어른준비 part 1")
# print(webtoon)

# """ 7 """
# import requests
# from bs4 import BeautifulSoup

# url = "https://comic.naver.com/webtoon/weekday"
# res = requests.get(url)
# res.raise_for_status()

# soup = BeautifulSoup(res.text, "lxml")

# # 네이버 웹툰 전체 목록 가져오기
# cartoons = soup.find_all("a", attrs={"class":"title"})
# # class 속성이 title인 모든 "a" element를 반환
# for cartoon in cartoons:
#     print(cartoon.get_text())

# """ 8 """
# import requests
# from bs4 import BeautifulSoup

# url = "https://comic.naver.com/webtoon/list?titleId=675554"
# res = requests.get(url)
# res.raise_for_status()

# soup = BeautifulSoup(res.text, "lxml")
# cartoons = soup.find_all("td", attrs={"class":"title"})
# # title = cartoons[0].a.get_text()
# # link = cartoons[0].a["href"]
# # print(title)
# # print("https://comic.naver.com" + link)
# # # title = cartoons[1].a.get_text()
# # # print(title)

# # 만화 제목 + 링크 가져오기
# # for cartoon in cartoons:
# #     title = cartoon.a.get_text()
# #     link = "https://comic.naver.com" + cartoon.a["href"]
# #     print(title, link)

# # 평점 구하기
# total_rates = 0
# cartoons = soup.find_all("div", attrs={"class":"rating_type"})
# for cartoon in cartoons:
#     rate = cartoon.find("strong").get_text()
#     print(rate)
#     total_rates += float(rate)
# print("전체 점수 :", total_rates)
# print("평균 점수 :", total_rates / len(cartoons))

# """ 9 """
# import requests
# import re
# from bs4 import BeautifulSoup

# url = "https://www.coupang.com/np/search?rocketAll=false&q=%EB%85%B8%ED%8A%B8%EB%B6%81&brand=&offerCondition=&filter=&availableDeliveryFilter=&filterType=&isPriceRange=false&priceRange=&minPrice=&maxPrice=&page=1&trcid=&traid=&filterSetByUser=true&channel=user&backgroundColor=&searchProductCount=5834663&component=&rating=0&sorter=scoreDesc&listSize=36"
# headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}
# res = requests.get(url, headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")

# # "li" tag 중 class 정보가 search-product으로 시작하는 모든 li element을 가져옴
# items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
# # print(items[0].find("div", attrs={"class":"name"}).get_text())

# for item in items:

#     # 광고 제품은 제외
#     ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
#     if ad_badge:
#         # print("     광고 상품 제외합니다")
#         continue

#     name = item.find("div", attrs={"class":"name"}).get_text()
#     # Apple 제품 제외
#     if "Apple" in name:
#         # print("     Apple 상품 제외합니다")
#         continue

#     price = item.find("strong", attrs={"class":"price-value"}).get_text()
    
#     # 리뷰 100개 이상, 평점 4.5 이상 되는 것만 조회
#     rate = item.find("em", attrs={"class":"rating"})
#     if rate:
#         rate = rate.get_text()
#     else:
#         # print("     평점 없는 상품 제외합니다.")
#         continue
    
#     rate_cnt = item.find("span", attrs={"class":"rating-total-count"})
#     if rate_cnt:
#         rate_cnt = rate_cnt.get_text() # ex : (26) 괄호 포함
#         rate_cnt = rate_cnt[1:-1] # 괄호 제외
#     else:
#         # print("     평점 수 없는 상품 제외합니다.")
#         continue

#     if float(rate) >= 4.5 and int(rate_cnt) >= 100:
#         print(name[:16], price, rate, rate_cnt)

# """ 10 """
# import requests
# import re
# from bs4 import BeautifulSoup

# headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}

# for i in range(1, 6):
#     url = "https://www.coupang.com/np/search?rocketAll=false&q=%EB%85%B8%ED%8A%B8%EB%B6%81&brand=&offerCondition=&filter=&availableDeliveryFilter=&filterType=&isPriceRange=false&priceRange=&minPrice=&maxPrice=&page={}&trcid=&traid=&filterSetByUser=true&channel=user&backgroundColor=&searchProductCount=5834663&component=&rating=0&sorter=scoreDesc&listSize=36".format(i)
#     res = requests.get(url, headers=headers)
#     res.raise_for_status()
#     soup = BeautifulSoup(res.text, "lxml")
#     items = soup.find_all("li", attrs={"class":re.compile("^search-product")})

#     for item in items:
#         # 광고 제품은 제외
#         ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
#         if ad_badge:
#             continue

#         name = item.find("div", attrs={"class":"name"}).get_text()
#         # Apple 제품 제외
#         if "Apple" in name:
#             continue

#         price = item.find("strong", attrs={"class":"price-value"}).get_text()
        
#         # 리뷰 500개 이상, 평점 5.0 이상 되는 것만 조회
#         rate = item.find("em", attrs={"class":"rating"})
#         if rate:
#             rate = rate.get_text()
#         else:
#             continue
        
#         rate_cnt = item.find("span", attrs={"class":"rating-total-count"})
#         if rate_cnt:
#             rate_cnt = rate_cnt.get_text()[1:-1] # ex : (26) 괄호 포함, [1:-1]: 괄호 제외
#         else:
#             continue
        
#         link = item.find("a", attrs={"class":"search-product-link"})["href"]
        
#         if float(rate) >= 5.0 and int(rate_cnt) >= 500:
#             # print(name[:16], price, rate, rate_cnt)
#             print(f"제품명 : {name}")
#             print(f"가격 : {price}")
#             print(f"평점 : {rate}점 ({rate_cnt})개")
#             print("바로가기 : {}".format("https://www.coupang.com" + link))
#             print("="*80)

# """ 11 """
# import os
# import requests
# from bs4 import BeautifulSoup

# os.mkdir("movie")

# for year in range(2015, 2020):
#     url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
#     res = requests.get(url)
#     res.raise_for_status()
#     soup = BeautifulSoup(res.text, "lxml")
#     images = soup.find_all("img", attrs={"class":"thumb_img"})

#     for idx, image in enumerate(images):
#         image_url = image["src"]
#         if image_url.startswith("//"):
#             image_url = "https:" + image_url

#         print(image["src"])
#         image_res = requests.get(image_url)
#         image_res.raise_for_status()

#         with open("movie/movie_{}_{}.jpg".format(year, idx+1), "wb") as f:
#             f.write(image_res.content)

#         if idx >= 4: # 상위 5개까지만 출력
#             break

# """ 12 """
# import csv
# from pyparsing import col
# import requests
# from bs4 import BeautifulSoup

# url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

# filename = "시가총액1-200.csv"
# f = open(filename, "w", encoding="utf-8-sig", newline="")
# writer = csv.writer(f)

# # title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split("\t")
# # writer.writerow(title)

# for page in range(1, 5):
#     res = requests.get(url+str(page))
#     res.raise_for_status()
#     soup = BeautifulSoup(res.text, "lxml")

#     if page == 1:
#         data_title = soup.find("table", attrs={"class":"type_2"}).find("thead").find_all("th")
#         title = [i.get_text() for i in data_title]
#         writer.writerow(title)

#     data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
#     for row in data_rows:
#         columns = row.find_all("td")
#         if len(columns) <= 1: # 의미 없는 데이터 skip
#             continue
#         data = [column.get_text().strip() for column in columns] # strip(): 양쪽 공백 제거
#         # print(data)
#         writer.writerow(data)

# """ 13 """
# from concurrent.futures import BrokenExecutor
# from selenium import webdriver
# import time

# browser = webdriver.Chrome("/Users/KDY/Workspace/python/python-from-scratch/webscraping_basic/practice/chromedriver")

# # 1. 네이버 이동
# browser.get("https://www.naver.com/")

# # 2. 로그인 버튼 클릭
# elem = browser.find_element_by_class_name("link_login")
# elem.click()

# # 3. id, pw 입력
# browser.find_element_by_id("id").send_keys("naver_id")
# browser.find_element_by_id("pw").send_keys("password")

# # 4. 로그인 버튼 클릭
# browser.find_element_by_id("log.login").click()
# time.sleep(1)

# # 5. id 새로 입력
# browser.find_element_by_id("id").clear()
# browser.find_element_by_id("id").send_keys("my_id")
# browser.find_element_by_id("pw").send_keys("password")

# # 6. html 정보 출력
# print(browser.page_source)

# # 7. 브라우저 종료
# browser.quit()

# """ 14 """
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# browser = webdriver.Chrome("/Users/KDY/Workspace/python/python-from-scratch/webscraping_basic/practice/chromedriver")
# # browser.maximize_window()

# url = "https://flight.naver.com/"
# browser.get(url)

# try:
#     # elem = browser.find_element_by_xpath('\
#     #     //*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]')
#     # print(elem.text)
#     # elem.click()
    
#     browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()
    
#     print("\ndone\n")
    
#     browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[1]').click()# [0] -> 이번 달
#     browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[2]').click()# [0] -> 이번 달
    
# finally:
#     time.sleep(5)
#     browser.quit()

# """ 17 """
# from selenium import webdriver

# options = webdriver.ChromeOptions()
# options.headless = True
# options.add_argument("window-size=2056x1329")

# browser = webdriver.Chrome(options=options)
# browser.maximize_window()

# url = "..."

# browser.get_screenshot_as_file("file_name.png")

# """ 18 """
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# options = webdriver.ChromeOptions()
# options.headless = True
# options.add_argument("window-size=2056x1329")
# options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36")

# browser = webdriver.Chrome("/Users/KDY/Workspace/python/python-from-scratch/webscraping_basic/practice/chromedriver", options=options)
# browser.maximize_window()

# url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
# browser.get(url)

# # detected_value = browser.find_element_by_id("detected_value")
# detected_value = browser.find_element(By.ID, "detected_value")
# print("\n"+detected_value.text+"\n")
# print("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36"==detected_value.text)
# browser.quit()