# 함수
from tkinter.tix import Balloon


# def open():
#     print("new account")

# open()

# def deposit(balance,money): # 입금
#     print("입급이 완료되었습니다. 잔액은{0} 원입니다.".format(balance+money))
#     return balance+money

# def withdraw(balance,money): # 출금
#     if balance >= money: # 잔액이 출금보다 많으면
#         print("출금이 완료되었습니다. 잔액은 {0} 원 입니다.".format(balance-money))
#         return balance-money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0} 원 입니다.".format(balance))
#         return balance

# def withdrawNight(balance,money): # 저녁에 출금
#     commission = 100 # 수수료 100원
#     return commission, balance-money-commission



# balance = 0 # 잔액
# balance = deposit(balance,1000) 
# # balance = withdraw(balance,2000)
# # balance = withdraw(balance,500)
# commission, balance= withdrawNight(balance, 500)
# print("수수료는 {0}원이며, 잔액은 {1} 원 입니다.".format(commission, balance))

#-------------기본값--------------
# def profile(name,age,langage):
#     print("Name: {0} \t Age: {1} \t Langage: {2}"\
#         .format(name,age,langage))

# profile("봄", 20, "파이썬")
# profile("여름", 22, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업.

# def profile(name, age=17, langage="파이썬"):
#     print("Name: {0} \t Age: {1} \t Langage: {2}"\
#         .format(name,age,langage))

# profile("봄")
# profile("여름")

#----------키워드 값-----------
# def profile(name, age, langage):
#     print(name, age, langage)

# profile(name="봄", langage="파이썬", age=20)
# profile(langage="자바", age=22, name="여름")

# ------------가변인자---------------
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("Name : {0}\t Age : {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

# def profile(name, age, *language):
#     print("Name : {0}\t Age : {1}\t".format(name, age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()

# profile("봄",20, "Python","Java","C","C++","C#","JavaScript")
# profile("여름",22, "Kotlin","Swift")

# ------------지역변수와 전역변수------------
# gun=10 # 전역

# def checkpoint(soldiers): #경계근무
#     global gun # 전역 공간에 있는 gun 변수 사용
#     # gun = 20 # 지역
#     gun = gun-soldiers 
#     print("[함수 내] 남은 총 : {0}".format(gun))

# def checkpointReturn(gun, soldiers):
#     gun=gun-soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun

# print("전체 총 : {0}".format(gun))
# # checkpoint(2) # 2명이 경계 근무 나감
# gun = checkpointReturn(gun,2)
# print("남은 총:{0}".format(gun))

# Question
# def std_weight(height,gender): # 키 m 단위 (실수) 170cm = 1.7m , 성별 = "남자"/"여자" 
#     if gender == "남자":
#         return height*height*22
#     elif gender == "여자":
#         return height*height*21

# height = 175 # cm 단위
# gender = "남자"
# weight=round(std_weight(height / 100, gender), 2)
# print("키 {0}cm {1}의 표준 체중은 {2} 입니다.".format(height, gender, weight))

