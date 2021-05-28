# 이상치 처리
 # 이상치 : 극단적인 값 또는 존재할 수 없는 값
 # 이상치 처리
  # 1) 행 제거 또는 
  # 2) 값을 채워넣음(대표값 또는 예측값으로)
  
import pandas as pd
from pandas.core.algorithms import isin

students = pd.read_csv("/home/andybae/study_python/Python_basic/students.csv")
students

students.info()

# 1) 범주형 변수의 이상치 확인 에
 # 1반과 2반만 존재하는 학교라는 예시. 1과 2 외의 데이터는 이상치
students[ students["class"].isin(['1','2'])] # 클래스 열의 값이 1 또는 2가 아닌 행만 <--- 이상치


# 이상치를 가진 행 삭제 예
students = students[ students["class"].isin(['1','2']) ]
students


# Basic box plot
import matplotlib.pyplot as plt
%matplotlib inline

a = plt.boxplot( students['english'])
plt.show()

plt.boxplot(students['math'], sym="bo")
plt.title('Box plot of math score')
plt.xticks ([1], ['math'])
plt.show()


# 연속적 변수 이상치 구하기 예
import numpy as np
Q1 = np.percentile(students["math"], 25)
Q3 = np.percentile(students["math"], 75)
print(Q1)
print(Q3)
IQR = Q3 - Q1
outlier_step = 1.5  * IQR

outlier_step


# 연속적 변수 이상치 출력
students[(students["math"]< Q1 - outlier_step) | (students["math"] > Q3 + outlier_step)]