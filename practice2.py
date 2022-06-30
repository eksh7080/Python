# ------------If문--------------
# weather = input("오늘 날씨는 어때요? ")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물이 필요 없습니다.")

# temp = int(input("기온은 어때요?"))
# if 30<=temp:
#     print("So Hot. Do not away outside")
# elif 10<=temp and temp<30:
#     print("good weather")
# elif 0<=temp and temp<10:
#     print("take a outer")
# else:
#     print("So Cold. Do not away outside")

# -----------------for문----------------
# for waitingNum in [0,1,2,3,4]:
#     print("대기번호:{0}".format(waitingNum))

# starbucks =["아이언맨","토르","그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))

#----------------while문----------------
# customer ="thor"
# index =5
# while index>=1:
#     print("{0}, 커피가 준비 되었습니다. {1}번 남았습니다.".format(customer,index))
#     index-=1
#     if index==0:
#         print("솔드아웃")

# cus = "ironman"
# while True:
#     print("{0}, 커피가 준비 되었습니다. 호출 {1}회".format(cus,index))
#     index+=1
#     if index==20:
#         break

# custo = "captin"
# person = "unknown"
# while person !=custo:
#     print("{0}, 커피가 준비 되었습니다.".format(custo))
#     person = input("이름이 어떻게 되세요?")

# -------------break,continue-------------
# absent=[2,5] # 결석
# no_book =[7] # 책을 깜빡함
# for student in range(1,11): # 1,2,3,4,5,6,7,8,9,10
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}은 교무실로 따라와".format(student))
#         break
#     print("{0}, 책을 읽어봐".format(student))

# -------- 한 줄 for문-----------
# 출석번호가 1,2,3,4 앞에 100을 붙이기로 함 ==> 101,102,103,104
# students=[1,2,3,4,5]
# students=[i+100 for i in students]
# print(students)

# 학생 이름을 길이로 변환
# stu=["Iron man","Thor","Captin"]
# stu =[len(i) for i in stu]
# print(stu)

# 학생 이름을 대문자로 변환
# stud=["Iron man","Thor","Captin"]
# stud=[i.upper() for i in stud]
# print(stud)

# Question

from random import*
sum=0 # 총 탑승 승객 수

for customer in range(1,51): # 1~50 승객 수
    time = randrange(5,51) # 5~50분 소요시간
    if 5<= time <=15: 
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(customer,time))
        sum+=1  # 카운트 증가
    else:
        print("[] {0}번째 손님 (소요시간 : {1}분)".format(customer,time))
    
print("총 탑승 승객 : {0} 분".format(sum))    
    
