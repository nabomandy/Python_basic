# 리스트 []

# 지하철 칸별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)

# 정형돈씨를 유재석 / 조세호 사이에 태워 봄
subway.insert(1, "정형돈")
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

# 순서 뒤집기 가능
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear
print(num_list)

# 다양한 자료형 함께 사용
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)


# 사전 ================
cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# print(cabinet[5]) #값이 없으므로 에러가 나서 스탑
# print(cabinet.get(5)) #None이라고 적히고 계속 진행
# print(cabinet.get(5, "사용 가능")) #5라는 값이 없으면 None이 아니라 "사용 가능"이 나온다.
# print("hi")

# print(3 in cabinet) # 값이 있는지 확인 ,True
# print(5 in cabinet) # False

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear() # 모든 값 삭제
print(cabinet)


# 튜플 ==============
# 리스트와 달리 내용 변경이나 추가가 되지 않는다. 리스트보다 빠름.
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스") # 값 추가나 변경 불가

# name = "김종국"
# age = "20"
# hobby = "코딩"
# print(name, age, hobby)

name, age, hobby = ("김종국", 20, "코딩") #투플을 이용한 방식, 한번에 값을 선언
print(name, age ,hobby)


# 세트 ===============
# 집합(set)
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3} #set에서는 값만 나열
print(my_set) # {1, 2, 3}

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 출력 (java와 python 을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java 도 할 수 있거나 python 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java 할 수 있지만 python은 할 수 없는 갭라자)
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print([python])

# java를 잊었어요
java.remove("김태호")
print(java)


# 자료구조의 변경
# 커피숍
menu = {"커피", "우유", "주스"} #{}를 이용했기 때문에 set #{'우유', '주스', '커피'} <class 'set'>
print(menu, type(menu))

menu = list(menu) #['우유', '주스', '커피'] <class 'list'>
print(menu, type(menu))

menu = tuple(menu) #('우유', '주스', '커피') <class 'tuple'>
print(menu, type(menu))

menu = set(menu)
print(menu)


# Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.

# 조건1 : 편의상 댓글은 20명이 작성하였고, 아이디는 1~20 이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle 과 sample을 활용

# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2,3,4]
# -- 축하합니다 --

# (활용예제)
# from random import *
# lst = [1, 2, 3, 4, 5]
# # print(lst)
# # shuffle(lst)
# # print(lst)
# print(sample(lst, 1))

from random import *
users = range(1, 21) #range 함수, 1~20까지 숫자를 생성
print(type(users)) #<class 'range'>, list에서 쓰는 함수를 쓰기 위해 변환해야 한다.
users = list(users); 
print(type(users))

print(users)
shuffle(users)
print(users)

winners = sample(users, 4) # 4명 중에서 1명은 치킨, 3명은 커피

print("# -- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다 --")