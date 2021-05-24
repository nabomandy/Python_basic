import numpy as np
# np.arange(15) : 0 ~ 14까지의 숫자
# reshape(3,5) : 3행 5열의 배열로 설정 
a = np.arange(15)
print(a)
a = np.arange(15).reshape(3, 5)
print("(3,5) 배열의 구조 :  ", a) # (3,5) 배열의 구조
print("2차원 : ", a.ndim) # 2차원
print("a 배열 요소의 자료형 이름 : ", a.dtype.name) # a 배열 요소의 자료형 이름
print("a 배열의 요소의 크기 바이트 단위 : ", a.itemsize) # a 배열의 요소의 크기 바이트 단위
print("a 배열의 요소의 갯수 : ", a.size) # a 배열의 요소의 갯수
print(type(a))
# np.array : 배열을 생성
b = np.array([6,7,8])
print(b)
print(type(b))

print(b.dtype)


print("====================================")
#리스트를 이용하여 배열 생성
e = np.array([[1,2], [3,4]], dtype=complex)
print(e)
print(e.dtype)

f = np.zeros((3,4)) #3행 4열 2차원 배열을 생성하고 0으로 초기화
print(f)
print(f.dtype)
# 3차원 배열 생성, 요소를 1로 초기화
g = np.ones((2,3,4), dtype=np.int16)
print(g)
print(g.dtype)


print("====================================")
# arange 함수를 이용하여 10부터 29까지의 수중 5의 배수로만 이루어진 배열 생성하기
h = np.arange(10,30,5) # [start, end, step]
print(h)
print(h.dtype)
# aragne(s ,e, d) : s부터 e 앞까지 d 만큼 증가한 수들의 목록
i = np.arange(0, 2, 0.3) 
print(i)
print(i.dtype)


print("====================================")
# linspace(s, e, d) : start부터 end까지의 수를 d 등분하기
j = np.linspace(0, 2, 9) # 0 ~ 2 까지를 균등하게 9등분한 숫자들의 목록
print(j)
print(j.dtype)

print(np.pi) # 원주율
# 0 ~ 2 pu 까지의 수를 100개 가져오기

k = np.linspace(0, 2*np.pi, 100)
print(k)
print(k.dtype)
# 출력되는 양이 많아지만 ... 로 표시해준다.
print(np.arange(10000))

print(np.arange(10000).reshape(100,100))# 0 ~ 9999 까지의 수를 100행 100열 배열로 생성하여 출력하기



print("====================================")
# numpy 기본연산 , shaep(디멘전과 형식)이 같아야 연산이 가능하다!
a = np.array([20, 30, 40, 50])
b = np.arange(4) # [0,1,2,3]

print(a-b) # [20, 29, 38, 47]
print(b**2) #[0,1,4,9]
print(a < 35)


print("====================================")
c = np.array([[1,1], [0,1]])
d = np.array([[2,0], [3,4]])
print(c+d) # 행열 합
print(c-d) # 행열 곱
print(c@d) # 행열식 곱
print(c.dot(d)) # 행열식 곱 , @ 표시와 같은 기능을 한다.


print("====================================")
e = np.ones((2,3), dtype=int)
print(e)
e *= 3 #e배열의 각 요소의 값에 *3을 하여 다시 e배열에 저장
print(e)

f = np.ones(3, dtype=np.int32)
g = np.linspace(0, np.pi, 3)
print(f.dtype, g.dtype)
h = f + g
print(h)
print(h.dtype) # float 64