# 모듈 : 필요한 것들끼리 부품처럼 잘 만들어진 파일
# 모듈은 쓰려는 파일과 같은 경로에 있거나 파이썬 라이브러리들이 모여있는 폴더에 있어야 사용 가능
#theater_module.py

# import theater_module #.py는 필요 없다.
# theater_module.price(3) # 3명이서 영화보러 갔을 때 가격
# theater_module.price_morning(4) # 4명이서 조조 할인 영화보러 갔을 때 가격
# theater_module.price_soldier(5) # 5명의 군인이 영화보러 갔을 때

# import theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import *
# # from random import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning  # 필요한 것만 가져다가 사용할 때
# price(5)
# price_morning(6)
# # price_soldier(7)

# from theater_module import price_soldier as price
# price(5) # 실제로는 price_soldier 이다.
 
 
#  # 패키지
# import travel.thailand # import 패키지.모듈
# # import travel.thailand.ThailandPackage 는 사용 불가
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage # 이렇게는 사용 가능
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()


# # __all__
# #from random import *
# from travel import *  # 실제로는 개발자가 이 문법상에서 공개 범위를 설정해줘야 한다. 패키지 중에서 공개를 원하는 것만 공개하게 설정. __init__.py에 가볼 것.
# # trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

# # 패키지, 모듈 위치

# from travel import *

# import inspect # 이 모듈이 어디에 위치에 있는지 확인하는
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))



# # pip install
# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())


# # 내장 함수
# # input : 사용자 입력을 받는 함수
# language = input("무슨 언어를 좋아하세요?")
# print("{0}은 아주 좋은 언어입니다.!".format(language))

# # dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 알려주는 거
# print(dir())
# import random # random 외장함수
# print(dir())
# import pickle
# print(dir())

# print(dir(random))

# lst = [1, 2, 3]
# print(dir(lst))

# name = "ANDY"
# print(dir(name))

# list of python builtins 구글 검색


# 외장함수 내장함수와 달리 임포트해서 사용해야 한다.
# list of python modules 구글 검색

# # 외장함수 예제
# # glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우의 dir)
# import glob
# print(glob.glob("*.py"))

# os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd()) # 현재 디렉토리를 표시하라는 거

# folder = "sample_dir"

# if os.path.exists(folder): # sample_dir 폴더가 존재하면 이 구문을 타라
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder) # 폴더 생성
#     print(folder, "폴더를 생성하였습니다.")
# print(os.listdir())  # glob과 비슷하게 사용

# # time : 시간 관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
# print("오늘 날짜는 ", datetime.date.today())

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today() # 오늘 날짜 저장
td = datetime.timedelta(days=100) # 100일 저장 (100 days)
print("우리가 만난지 100일은", today + td) # 오늘부터 100일 훈
