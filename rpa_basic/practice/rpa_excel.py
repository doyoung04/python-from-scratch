# """ 1 """
# from openpyxl import Workbook

# wb = Workbook() # 새 워크북 생성
# ws = wb.active  # 현재 활성화된 sheet 가져옴
# ws.title = "SheetTitle" # sheet 의 이름을 변경
# wb.save("sample01.xlsx")
# wb.close()

# """ 2 """
# from openpyxl import Workbook

# wb = Workbook() # 새 워크북 생성

# ws = wb.create_sheet()  # 새로운 시트를 기본 이름으로 생성
# ws.title = "MySheet" # 시트 이름 변경
# ws.sheet_properties.tabColor = "ff66ff" # RGB 형태로 시트 탭 색상 변경

# ws1 = wb.create_sheet("YourSheet")  # 새로운 시트를 설정한 이름으로 생성
# # 현재 순서: Sheet, MySheet, YourSheet
# ws2 = wb.create_sheet("NewSheet", 2) # 2번째 인덱스에 시트 생성, My Your 사이

# """
# 작업할 때 
# ws1 = ... 이렇게 작업할 수도 있지만
# wb["NewSheet"] = ... 이렇게 작업할 수도 있다
# """

# print(wb.sheetnames)

# new_ws = wb["NewSheet"]
# new_ws["A1"] = "Test"
# target = wb.copy_worksheet(new_ws)
# target.title = "Copied Sheet"

# print(wb.sheetnames)

# wb.save("sample02.xlsx")
# wb.close()

# """ 3 """
# from openpyxl import Workbook

# wb = Workbook() # 새 워크북 생성
# ws = wb.active
# ws.title = "SheetTitle"

# ws["A1"] = 1 # A1 셀에 1 값을 입력
# ws["A2"] = 2
# ws["A3"] = 3

# ws["B1"] = 4
# ws["B2"] = 5
# ws["B3"] = 6

# print(ws["A1"]) # A1 셀의 정보를 출력
# print(ws["B3"].value)
# print(ws["B3"].row)
# print(ws["B3"].column)
# print(ws["A10"].value)

# ws.cell(row=3, column=3, value=7)
# print(ws["C3"].value)

# ws.cell(4, 4, 8) # row, column, value 순서
# print(ws["D4"].value)

# ws.cell(4, 1, None) # row, column, value 순서
# print(ws["A4"].value)

# from random import *
# index = 1
# for x in range(1, 11): # 10개 row
#     for y in range(1, 11): # 10개 column
#         ws.cell(row=x, column=y, value=(randint(0, 100)))
#         ws.cell(row=x, column=y, value=index)
#         index += 1

# wb.save("sample03.xlsx")

# """ 4 """
# from openpyxl import load_workbook
# wb = load_workbook("sample03.xlsx")
# ws = wb.active

# # cell 데이터 불러오기
# for x in range(1, 11):
#     for y in range(1, 11):
#         print(ws.cell(row=x, column=y).value, end=" ")
#     print()

# # cell 개수를 모를 때
# for x in range(1, ws.max_row+1):
#     for y in range(1, ws.max_column+1):
#         print(ws.cell(row=x, column=y).value, end=" ")
#     print()

""" 5 """
from openpyxl import Workbook
from random import *
wb = Workbook()
ws = wb.active # 활성화된 거 가져오기

# 1줄 씩 데이터 넣기
ws.append(["번호", "영어", "수학"]) # A, B, C
for i in range(1, 11): # 10개 데이터
    ws.append([i, randint(0, 100), randint(0, 100)])

col_B = ws["B"] # column B 영어
# print(col_B)
# for cell in col_B:
#     print(cell.value)

col_range = ws["B:C"] # B부터 C까지
# for cols in col_range:
#     for cell in cols:
#         print(cell.value)

row_title = ws[1] # 1번째 row
# for cell in row_title:
#     print(cell.value)

row_range = ws[2:6] # 2번째 줄부터 6번째 줄까지 가지고 오기 2, 3, 4, 5, 6(6도 포함)
# for rows in row_range:
#     for cell in rows:
#         print(cell.value, end=" ")
#     print()

from openpyxl.utils.cell import coordinate_from_string

row_range = ws[2:ws.max_row] # 2번째 줄부터 마지막 줄까지
# for rows in row_range:
#     for cell in rows:
#         # print(cell.value, end=" ")
#         # print(cell.coordinate, end=" ") # cell 번호 출력
#         xy = coordinate_from_string(cell.coordinate)
#         # print(xy, end=" ")
#         print(xy[0], xy[1], end=" ")
#     print()

# # 전체 rows
# print(tuple(ws.rows))
# for row in tuple(ws.rows):
#     print(row[2].value)

# # 전체 columns
# print(tuple(ws.columns))
# for column in tuple(ws.columns):
#     print(column[0].value)

# for row in ws.iter_rows(): # 전체 row
#     print(row[2].value)

# for column in ws.iter_cols(): # 전체 column
#     print(column[0].value)

# # 2번째 줄부터 11번째 줄까지, 2번째 열부터 3번째 열까지
# for row in ws.iter_rows(min_row=2, max_row=11, min_col=2, max_col=3):
#     # print(row[0].value, row[1].value) # 수학, 영어
#     print(row)

# for col in ws.iter_cols(min_row=1, max_row=5, min_col=1, max_col=3):
#     print(col)

wb.save("sample05.xlsx")