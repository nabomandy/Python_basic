# 입출력

# print("Python", "Java", "JavaScript", sep=" vs ")
# print("Python", "Java", "JavaScript", sep = ",", end="a? ")
# print("무엇이 더 재밌을까요?")

# import sys
# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)

# 시험 성적
# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":")

# 은행 대기순번표
# 001, 002, 003, ...
# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3))

# answer = input("아무 값이나 입력하세요 : ") #input으로 값을 받으면 항상 문자열로 인식된다.
# print(type(answer))
# print("입력하신 값은 " + answer + "입니다.") 


# 다양한 출력 포맷

# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500))
# # 양수일 땐 +로 표시, 음수일 땐 -로 표시
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))
# # 왼쪽 정렬하고, 빈칸으로 _로 채움
# print("{0:_<+10}".format(500))
# # 3자리 마다 콤마를 찍어주기
# print("{0:,}".format(100000000000))
# # 3자리 마다 콤마를 찍어주기, +- 부호도 붙이기
# print("{0:+,}".format(100000000000))
# print("{0:+,}".format(-100000000000))
# # 3자리마다 콤마를 찍어주기, 부호도 붙이고, 자릿수도 확보하기 
# # 돈이 많으면 행복하니까 빈 자리는 ^로 채워주기
# print("{0:^<+30,}".format(100000000000000000))
# # 소수점 출력
# print("{0:f}".format(5/3))
# # 소수점 특정 자리수 까지만 표시 (소수점 3째자리에서 반올림)
# print("{0:.2f}".format(5/3))


# # 파일 입출력
# score_file = open("score.txt","w",encoding="UTF-8") # w는 write를 의미
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close

# score_file = open("score.txt", "a", encoding="UTF-8") # a는 append
# score_file.write("과학 : 80") # score_file.write로 하면 줄마꿈이 따로 없다. 그래서 명시
# score_file.write("\n코딩 : 100")

from os import close, pread
import pickle


# score_file = open("score.txt", "r", encoding="UTF-8") # 한번에 모든 내용 불러오기
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="UTF-8") 
# print(score_file.readline()) # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="") # end="" 줄바꿈 안하려고 추가
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# score_file = open("score.txt", "r", encoding="UTF-8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="") # end="" 줄바꿈 안하려고 추가
# score_file.close()

# score_file = open("score.txt", "r", encoding="UTF-8")
# lines = score_file.readlines() # list 형태로 모든 라인을 저장
# for line in lines:
#     print(line, end="")

# score_file.close


# 피클
# import pickle
# profile_file = open("profile.pickle", "wb") #wb에서 b는 바이너리. pickle은 바이너리를 꼭 포함해야 한다. 인코딩은 별로도 설정할 필요는 없다.
# profile = {"이름":"박명수", "나이":30, "취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile 에 있는 정보를 file에  저장
# profile_file.close

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()


# # with
# import pickle

# with open("profile.pickle", "rb") as profile_file: # 따로 close 해줄 필요 없이, with 문이 종료되면서 자동으로 된다.
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="UTF-8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")
    
# with open("study.txt", "r", encoding="UTF-8") as study_file:
#     print(study_file.read())
    
    
# Quiz) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# - X 주차 주간보고 -
# 부서 :
# 이름 :
# 업무 요약 :
    
# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

# 조건 : 파일명은 '1주차.txt', '2주차.txt', ... 와 같이 만듭니다.

for i in range(1,51):
    with open(str(i) + "주차.txt", "w", encoding="UTF-8") as report_file:
        report_file.write("- {0} 주차 주간보고 -".format(i))
        report_file.write("\n부서 :")
        report_file.write("\n이름 :")
        report_file.write("\n업무 요약 :")