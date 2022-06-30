# sep
# import sys
# print("Python","Java", sep=" vs ", end="?")
# print("무엇이 더 재밌을까요?")
# print("Python","Java", file=sys.stdout) # 표준 출력
# print("Python","Java", file=sys.stderr) # 에러를 확인

# 시험 성적
# scor={"수학":0, "영어":50, "코딩":100}
# for subject, score in scor.items():
    # print(subject, score)
    # print(subject.ljust(4), str(score).rjust(4), sep=":") 
    # ljust = 8공간 확보하고 왼쪽 정렬 // rjust = 4개의 공간 확보하고 오른쪽 정렬

# 은행 대기순번표
# 001, 002, 003, ...
# for num in range(1, 21):
    # print("대기번호 : " + str(num).zfill(3)) # zfill 3개만큼의 공간을 확보하고 0을 채워넣음

# answer=input("아무 값이나 입력하세요 :") # 항상 문자열로 저장됨
# print(type(answer))
# print("입력하신 값은 " + answer + "입니다.")

# ----------다양한 출력 포맷------------

# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총10자리 공간을 확보
print("{0: >10}".format(500))

# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_<+10}".format(500))

# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(100000000000000))

# 3자리 마다 콤마를 찍어주기 +- 부호도 붙이기
print("{0:+,}".format(100000000000000))
print("{0:-,}".format(100000000000000))

# 3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기
# 돈이 많으면 행복하니까 빈 자리는 ^로 채워주기
print("{0:^<+30,}".format(100000000000000000))

# 소수점 출력
print("{0:f}".format(5/3))

# 소수점 특정 자리수 까지만 표시 (소수점 3째 자리에서 반올림)
print("{0:.2f}".format(5/3))
