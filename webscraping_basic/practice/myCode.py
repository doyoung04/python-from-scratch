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

""" 8 """
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=675554"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
cartoons = soup.find_all("td", attrs={"class":"title"})
# title = cartoons[0].a.get_text()
# link = cartoons[0].a["href"]
# print(title)
# print("https://comic.naver.com" + link)
# # title = cartoons[1].a.get_text()
# # print(title)

# 만화 제목 + 링크 가져오기
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     print(title, link)

# 평점 구하기
total_rates = 0
cartoons = soup.find_all("div", attrs={"class":"rating_type"})
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)
    total_rates += float(rate)
print("전체 점수 :", total_rates)
print("평균 점수 :", total_rates / len(cartoons))