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

""" 5 """