""" dict. """
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# print(cabinet[5]) # Error
print(cabinet.get(5, "사용 가능")) # None
print("hi")

print(cabinet.get(5))

print(3 in cabinet) # True
print(5 in cabinet) # False

print(cabinet)
cabinet[3] = "김종국"
cabinet[20] = "조세호"

print(cabinet)

del cabinet[3]
print(cabinet)

print(cabinet.keys())

print(cabinet.values())

print(cabinet.items())

cabinet.clear()
print(cabinet)


""" set """
from tkinter.ttk import Style


java = {"a", "b", "c"}
python = set(["a", "d"])

# 교집합
print(java & python)
print(java.intersection(python))

# 합집합
print(java | python)
print(java.union(python))

# 차집합
print(java - python)
print(java.difference(python))

# 파이썬 추가
python.add("e")
print(python)

# 자바 까먹음
java.remove("c")
print(java)


students = [1, 2, 3, 4, 5]
students = [i+100 for i in students]
print(students)


import pickle
profile_file = open("profile.pickle", "wb")
profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile을 file에 저장
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)
print(profile)
profile_file.close()

import pickle
with open("profile.pickle", "rb") as profile_file:
    # "profile.pickle"을 열어서 profile_file변수에 저장, with 안에서 close 할 필요 없음
    print(pickle.load(profile_file))

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

wraith1 = Unit("레이스", 80, 5)
print("유닛 이름: {0}, 공격력: {1}".format(wraith1.name, wraith1.damage))

wraith2 = Unit("레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))

# if wraith1.clocking == True:
#     print("{0}는 현재 클로킹 상태입니다.".format(wraith1.name)) #1은 클로킹이 없어서 안됨

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp

class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location):
        print("{0}: {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))
    
    def damaged(self, damage):
        print("{0}: {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0}: 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0}: 파괴되었습니다.".format(self.name))

firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

firebat1.damaged(25) # hp 50 > 25
firebat1.damaged(25) # hp 25 > 0

""" 상속 """
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class AttackUnit(Unit): # Unit을 상속, damage만 추가할 예정
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp) # 상속
        self.damage = damage # 추가할 내용
    
    def attack(self, location):
        print("{0}: {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))
    
    def damaged(self, damage):
        print("{0}: {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0}: 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0}: 파괴되었습니다.".format(self.name))

firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

firebat1.damaged(25) # hp 50 > 25
firebat1.damaged(25) # hp 25 > 0

""" 다중 상속, 부모 클래스를 2개 이상 상속 """
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class AttackUnit(Unit): # Unit을 상속, damage만 추가할 예정
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp) # 상속
        self.damage = damage # 추가할 내용
    
    def attack(self, location):
        print("{0}: {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))
    
    def damaged(self, damage):
        print("{0}: {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0}: 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0}: 파괴되었습니다.".format(self.name))

class Flyable: # 날아다니는 애
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0}: {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable): # 공격 유닛 + 날아다니는 애
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")
valkyrie.attack("5시")
valkyrie.damaged(100)
valkyrie.damaged(100)

""" 메소드 오버라이딩 """
# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed

#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0}: {1} 방향으로 이동합니다. [속도 {2}]"\
#             .format(self.name, location, self.speed))

# class AttackUnit(Unit): # Unit을 상속, damage만 추가할 예정
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed) # 상속
#         self.damage = damage # 추가할 내용
    
#     def attack(self, location):
#         print("{0}: {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
#             .format(self.name, location, self.damage))
    
#     def damaged(self, damage):
#         print("{0}: {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0}: 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0}: 파괴되었습니다.".format(self.name))

# class Flyable: # 날아다니는 애
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0}: {1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name, location, self.flying_speed))

# class FlyableAttackUnit(AttackUnit, Flyable): # 공격 유닛 + 날아다니는 애
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
#         Flyable.__init__(self, flying_speed)

# vulture = AttackUnit("벌쳐", 80, 10, 20)
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시")
# # 지상 유닛은 move, 공중 유닛은 fly을 사용해야함 -> 귀찮음

class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0}: {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))

class AttackUnit(Unit): # Unit을 상속, damage만 추가할 예정
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed) # 상속
        self.damage = damage # 추가할 내용
    
    def attack(self, location):
        print("{0}: {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))
    
    def damaged(self, damage):
        print("{0}: {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0}: 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0}: 파괴되었습니다.".format(self.name))

class Flyable: # 날아다니는 애
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0}: {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable): # 공격 유닛 + 날아다니는 애
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
        Flyable.__init__(self, flying_speed)

    def move(self, location): # move을 새롭게 재정의
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

vulture = AttackUnit("벌쳐", 80, 10, 20)
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시")
battlecruiser.move("9시")

""" 예외 처리 """
try:
    nums = []
    nums.append(int(input("enter: ")))
    nums.append(int(input("enter: ")))
    # nums.append((int(nums[0]/nums[1])))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("error")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("알 수 없는 에러가 발생하였습니다.")
    print(err)

""" 에러 발생 """
try:
    print("한 자리 숫자 나누기 전용 계산기 입니다.")
    num1 = int(input("enter: "))
    num2 = int(input("enter: "))
    if num1 >= 10 or num2 >= 10:
        raise ValueError
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")

""" 사용자 정의 에러 """
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기 입니다.")
    num1 = int(input("enter: "))
    num2 = int(input("enter: "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값: {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)

""" finally """
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기 입니다.")
    num1 = int(input("enter: "))
    num2 = int(input("enter: "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값: {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)
finally: # 어쨌든 출력
    print("계산기를 이용해주셔서 감사합니다.")

import os
print(os.getcwd())

folder = "sample_dir"

if os.path.exists(folder):
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)
    print(folder, "폴더를 삭제하였습니다.")
else:
    os.makedirs(folder)
    print(folder, "폴더를 생성하였습니다.")

import os
print(os.listdir())

import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
print(datetime.date.today())

today = datetime.date.today()
td = datetime.timedelta(days=100)
print(today+td)

print("Hello world!")