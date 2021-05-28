#결측치 처리
# 결측치 : 비어있는 값. 분석 결과 왜곡


import pandas as pd 

age      = pd.Series([ None,  42, 27,  25,  20]  ) 
score    = pd.Series([3.8, 4.2, 2.6, 1.0, 3.0] ) 
salary =  pd.Series([2700,4000,3000,2700,3200])  
stu_class = pd.Categorical([ 1, 1, 2, None, 2])   # None 결측치 
gender    = pd.Categorical([ 'F', 'M', 'M', 'M', None ])   # None 결측치


df = pd.DataFrame   ( {'age': age, 
                     'score' :  score  ,
                     'salary' : salary,
                      'class' :stu_class,
                       'gender' : gender}
)
df



df_new = df.copy() # df 복제 

# 데이터 프레임의 모든 값이 boolean 형태로 표시되도록 하며, nan 값에만 True 표시되도록
pd.isna(df_new) # 결측치 값 확인

# df_new.isnull().sum*()


# 결측치 처리 
  #1) 행 제거
df_new = df_new.dropna(how='any') #결측치를 가지고 있는 행들을 삭제
df_new

 #2) 다른 값으로 채우기

df_new = df.copy() # df 복제

df_new["age"] = df_new["age"].fillna(value=30) # age 열의 결측치를 다른 값으로 채우기(대표값 또는 예측값을 구한 후)

df_new

