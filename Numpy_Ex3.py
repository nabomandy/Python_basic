"""
    numpy 에서 사용되는 함수
"""

import numpy as np
from numpy.core.fromnumeric import size

a = np.arange(12).reshape(3,4)
print(a)

print(a.sum(axis=0)) # 합계, axis=0 컬럼기준 수직기준
print(a.sum(axis=1)) # 합계, axis=1, 행기준 수평기준
print(a.max(axis=0)) # 최댓값 axis=0, 컬럼기준
print(a.max(axis=1)) # 최댓값 axis=1, 행기준
print(a.min(axis=1)) # 최솟값 axis=1, 행기준
print(a.cumsum(axis=1)) # 누적합 행기준


print("===========================")

b= np.arange(3)
print(b)
print(np.exp(b)) # 자연로그 in x= b
print(np.sqrt(b)) # 제곱근


print("===========================")
c = np.array([2, -1, 4])
print(type(c))
print(b+c)
print(np.add(b,c))


print("===========================")
# 평균 10, 표준편차 1인 정규분포를 따르는 3행 3열 난수 배열 생성?
d = np.random.normal(10, 1, (3, 3))
print(d)
print(np.mean(d)) # 평균


print("===========================")
# 0 ~ 10 구간의 임의의 정수를 가진 3행 3열 배열 생성
e = np.random.randint(0,10,(3,3))
print(e)


print("===========================")
import numpy as np
x= np.arange(10) # 0 ~ 9
print("0부터 4 인덱스까지 부분 배열: ", x[:5]) 
print(x[5:]) # 5부터 끝까지 부분 배열
print(x[4:7]) # 4부터 6 인덱스까지 부분 배열
print(x[::2]) # 0 부터 끝 인덱스까지 2씩 증가한 부분 배열 [start:end:step]
print(x[1::2]) # 1부터 끝 인덱스까지 2씩 증가한 부분 배열
print(x[1:8:3]) # 1부터 7 인덱스까지 3씩 증가한 부분 배열
print(x[::-1]) # 끝부터 0 인덱까지 역순인 배열


print("===========================")
print("0부터 9까지의 난수를 4행 5열 배열로 생성")
# x = np.random.randint(10,size=(4,5))
x = np.random.randint(10, size=(4,5))
print(x)


print("===========================")
# 2개의 행과 3개의 열을 가진 부분 배열
print(x[2:3])


print("===========================")
# 모든 행을 한개씩 걸러서 열 조회하기
print(x[:,::2])


print("===========================")
# 행과 열 모두 역으로 조회하기.
print(x[::-1,::-1])
# 모든 행의 열만 역으로 조회하기
print(x[:,::-1])


print("===========================")
# 0 ~ 9 까지의 임의의 수 10개 가진 배열 생성
x = np.random.randint(10, size = 10)
print(x)
x_sub = x[:2] # 0,1 인덱스를 가진 부분 배열
print(x_sub)


print("===========================")
x_sub[0] = 20 # 부분 배열을 변경 시 원본 배열도 변경 된
print(x)
print(x_sub)


print("===========================")
# 배열 복사
x_cop = x.copy() # x 배열 복사
x_cop[0] = 100
print(x)
print(x_cop)


print("===========================")
# 배열의 재편성 : 재편성되는 배열 요소의 수가 원본의 배열의 수와 같아야 한다.
x2 = x.reshape(5,2) # 1차원 배열 => 2차원 배열로 재편성함.
print(x2)


print("===========================")
# 0부터 99까지의 임의의 수를 9개 가진 배열 a 생성.
# a 배열을 3행 3열로 재편성한 배열 b 생성하기
# 재편성시 요소의 갯수가 맞아야 한다.
a = np.random.randint(100, size=9)
b= a.reshape(3,3)
print(a)
print(b)


print("===========================")
"""
    numpy 배열의 연결 및 분할
"""
import numpy as np
x = np.array([[1,2,3],[4,5,6]])
y = np.array([[3,2,1],[6,5,4]])
print(x)
print(y)
# 배열의 연결
print(np.concatenate([x,y], axis=0)) # 수직연결. 행으로 연결
print(np.concatenate([x,y], axis=1)) # 수평연결, 열으로 연결


print("===========================")
# 형태가 다른 배열의 연결
x = np.array([[1,2,3], [4,5,6]])
y = np.array([[3,2,1],[6,5,4],[3,2,1]])
z = np.array([[7], [10]])
print(x)
print(y)
print(z)
# vsatck : 수직연결, 행기준 연결
# hstack : 수평연결, 열기준 연결.
print(np.vstack([x,y])) # 열의 갯수가 동일해야 함.
print(np.hstack([x,z])) # 행의 갯수가 동일해야 함.
# print(np.hstack([x,y])) # 행의 갯수가 다름. 오류 발생
# print(np.vstack([x,z])) # 열의 갯수가 다름. 오류 발생


print("===========================")
# 배열의 분리
# 0 ~ 15 까지의 값을 4행 4열 배열로 생성
x = np.arange(16).reshape((4,4))
print(x)
upper, lower = np.vsplit(x,[2]) # 2ㅎㅇ 분리
print(upper)
print(lower)

# 2열 분리
left, right = np.hsplit(x,[2])
print(left)
print(right)