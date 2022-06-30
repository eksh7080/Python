#숫자 처리 함수
# print(abs(-5)) #절댓값
# print(pow(4,2)) #4의 2승 
# print(max(5,12)) #12 최댓값 반환
# print(min(5,12)) #5 최소값 반환
# print(round(3.14)) #반올림
# print(round(4.99))

# from math import *
# print(floor(4.99)) # 내림
# print(ceil(3.14)) # 올림
# print(sqrt(16)) # 제곱근

#랜덤함수
# from random import *
# print(random()) # 0.0~1.0 미만의 임의의 값 생성
# print(random()*10) # 0.0~10.0 미만의 임의의 값 생성
# print(int(random()*10)) # 0~10 미만의 임의의 값 생성
# print(int(random()*10)+1) # 1~10 이하의 임의의 값 생성
# print(int(random()*45)+1) # 1~45 이하의 임의의 값 생성
# print(randrange(1,46)) # 1~46 미만의 임의의 값 생성
# print(randint(1,45)) # 1~45 이하의 임의의 값 생성

# n=randrange(4,28)
# print(n)
# print("오프라인 스터디 모임 날짜는 매월",str(n),"일로 선정되었습니다.")

# sentence = "나는 소년입니다."
# print(sentence)

# s2="파이썬은 쉬워요"
# print(s2)

# s3="""
# 나는 소년이고
# 파이썬은 쉬워요
# """
# print(s3)

# jumin = "990122-131313"
# print("성별:", jumin[7])
# print("Year:", jumin[0:2]) # 0부터 2 직전까지 가져옴
# print("Month:", jumin[2:4])
# print("Day:", jumin[4:6])
# print("생년월일:", jumin[:6]) # 처음부터 6 직전까지
# print("뒤 7자리:", jumin[7:])
# print("뒤 7자리 (뒤에부터):", jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지

# 문자열 처리 함수
# p = "python is Amazing"
# print(p.lower())
# print(p.upper())
# print(p[0].isupper())
# print(len(p))
# print(p.replace("python","java"))

# index= p.index("n")
# print(index)
# index = p.index("n",index+1)
# print(index)

# print(p.find("n")) # 원하는 값이 없을땐 -1 반환
# # print(p.index("java")) # 얘는 에러 내버림
# print(p.count("n")) # n이 몇 번 나왔는지 알려줌

# 문자열 포맷
# print("나는 %d살 입니다." % 20) # d 는 정수값만 가능
# print("나는 %s을 좋아해요" % "파이썬") # s는 문자열
# print("Apple은 %c로 시작해요" %"A") # c는 한 글자만 받는다

# %s
# print("나는 %s살입니다."%20)
# print("나는 %s색과 %s색을 좋아해요." %("파란","빨간"))

# 방법
# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요".format("파란","빨간"))
# print("나는 {0}색과 {1}색을 좋아해요".format("파란","빨간"))
# print("나는 {1}색과 {0}색을 좋아해요".format("파란","빨간"))

# 방법2
# print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20, color="빨간"))
# print("나는 {age}살이며, {color}색을 좋아해요".format( color="빨간",age = 20))

# 방법3 (ver3.6이상)
# age=20
# color="빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")

# 탈출문자
# print("백문이 불여일견 \n 백견이 불여일타") # \n : 줄바꿈
# print("저는 '다노' 입니다.")
# print('저는 "다노" 입니다.')
# print("저는 \"다노\" 입니다.")

# \\ : 문장 내에서 \
# print(" c:\\Users\\LEE\\Desktop\\Python")

# \r : 커서를 맨 앞으로 이동
# print("Red Apple\rPine")

# \b : 백스페이스 (한 글자 삭제)
# print("Redd\bApple")

# \t : 탭

# Question
# ex = "http://naver.com"
# exc = ex.replace("http://","") 
# exc = exc[:exc.index(".")] 
# print(exc)
# pwd=exc[:3]+str(len(exc))+str(ex.count("e"))+"!"
# print("{0} 의 비밀번호는 {1} 입니다.".format(ex,pwd))

# 리스트 []

# 지하철 칸별로 10명,20,30

# subway = [10,20,30]
# print(subway)

# subway =["유재석","조세호"]
# print(subway)

# 조세호씨가 몇 번째 칸에 타고 있는가?
# print(subway.index("조세호"))

# 하하가 다음 정류장에서 다음 칸에 탐
# subway.append("하하") # append는 맨 뒤에 붙음
# print(subway)

# 정형돈씨를 유재석 / 조세호 사이에 태워봄
# subway.insert(1,"정형돈")
# print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# print(subway.pop()) # pop은 뒤에서부터 꺼냄
# print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# 같은 이름의 사람이 몇 명인지 확인
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# 정렬도 가능
# num=[5,4,3,2,1]
# num.sort()
# print(num)

# 순서 뒤집기도 가능
# num.reverse()
# print(num)

# 모두 지우기
# num.clear()
# print(num)

# 다양한 자료형 함께 사용
# num1=[5,2,3,4,1]
# mix = ["유",20,True] # 다양한 자료형 사용 가능

# 리스트 확장
# num1.extend(mix)
# print(num1)

# 딕셔너리
# cabinet = {3:"세상에",100:"마상에"}
# print(cabinet[100],cabinet[3])
# print(cabinet.get(3))
# print(cabinet.get(5),"\n","can do it")
# print(3 in cabinet) # 안에 있는지 확인하는 것
# print(5 in cabinet)

# cap ={"A-3":"세상이","B-19":"마상이"}
# print(cap["A-3"])
# print(cap["B-19"])

# 새 손님
# print(cap)
# cap["A-3"]="이상해"
# cap["C-3"]="파이리"
# print(cap)

# 간 손님
# del cap["A-3"]
# print(cap)

# key들만 출력
# print(cap.keys())

# value만 출력
# print(cap.values())

# key,value 쌍으로 출력
# print(cap.items())

# 목욕탕 폐점
# cap.clear()
# print(cap)

# ---------------튜플--------------
# m=("돼지고기너비튀김","돼지고기치즈너비튀김")
# print(m[0],m[1])

# m.add() 기능 제공 안함 // 변경 추가 불가능

# name="꼬부기"
# age=20
# hobby="축구"
# print(name,age,hobby)

# (name,age,hobby) = ("꼬부기",20,"축구")
# print(name,age,hobby)

# 집합 (set) = 중복 안됨 , 순서없음
# sseet={1,2,3,3,3}
# print(sseet)

# java={"리자몽","이상해꽃","거북왕"}
# python = set(["리자몽","풀잎"])

# 교집합 (java와 python 을 모두 할 수 있는 개발자)
# print(java & python)
# print(java.intersection(python))

# 합집합 (java 를 할 수 있거나 python을 할 수 있는 개발자)
# print(java|python)
# print(java.union(python))

# 차집합 (java는 할 수 있지만 python 은 할 줄 모르는 개발자)
# print(java - python)
# print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
# python.add("햇빛")
# print(python)

# java 를 잊었어요
# java.remove("리자몽")
# print(java)

# ---------------자료구조의 변경---------------
# m1= {"coffee","milk","beer"}
# print(m1,type(m1))

# m1=list(m1)
# print(m1,type(m1))

# m1 = tuple(m1)
# print(m1,type(m1))

# m1=set(m1)
# print(m1,type(m1))

#--------------------Question-------------------
from random import*

# ID=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
ID=range(1,21)
ID=list(ID)
shuffle(ID)
winner=sample(ID,4)
print("-- 당첨자 발표 --")
print("치킨 당첨자: {0}".format(winner[0]))
print("커피 당첨자: {0}".format(winner[1:]))
print("-- 축하합니다 --")
