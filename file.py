# score_file=open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file2 = open("score.txt", "a", encoding="utf8")
# score_file2.write("과학 : 80")
# score_file2.write("\n코딩 : 100")

# score_file3 = open("score.txt", "r", encoding="utf8")
# print(score_file3.read())
# score_file3.close()

# score_file4 = open("score.txt", "r", encoding="utf8")
# print(score_file4.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file4.readline(), end="")
# print(score_file4.readline(), end="")
# print(score_file4.readline(), end="")
# score_file4.close()

# score_file5 = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file5.readline()
#     if not line:
#         break
#     print(line,end="")
# score_file5.close()

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines() # list 형태로 저장
# for line in lines:
#     print(line, end="")

# score_file.close()

# ------------------------pickle---------------------------
# import pickle
# profile_file = open("profile.pickle", "wb") # b = 바이너리 타입 wb= 쓰기
# profile = {"이름":"박명수", "나이":30, "취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile 에 있는 정보를 file 에 저장
# profile_file.close()

# profile_file = open("profile.pickle", "rb") # rb= 읽기
# profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

# ----------------with---------------
# import pickle

# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())

# Question

# for i in range(1,51):
#     with open(str(i) + "week.txt", "w", encoding="utf8") as report_file:
#         report_file.write("-{0} 주차 주간보고-".format(i))
#         report_file.write("\n부서 : SI")
#         report_file.write("\n이름 : nanme")
#         report_file.write("\n업무요약 : SI")



