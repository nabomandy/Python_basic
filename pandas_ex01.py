from numpy import product
import pandas as pd

goods = pd.Series(["사과", "딸기", "수박"])
price = pd.Series([1800, 15000, 3000])
qty = pd.Series([24,38,13])

products = pd.DataFrame( {"제품" : goods , "가격" : price, "판매량" : qty})
products

from io import StringIO

csv_data = StringIO("""
x1,x2,x3,x4,x5
1,0.1,"1",2019-01-01,A
2,,,2019-01-02,B
3,,"3",2019-01-03,C
,0.4,"4",2019-01-04,A
5,0.5,"5",2019-01-05,B
,,,2019-01-06,C
7,0.7,"7",,A
8,0.8,"8",2019-01-08,B
9,0.9,,2019-01-09,C
""")

df = pd.read_csv(csv_data, dtype={"x1": pd.Int64Dtype()}, parse_dates=[3])
df


df["class"] = pd.Series([1, 1, 2, 2, 2, 3, 3, 4, 4, 4])
# class열이 존재하면 갱신, 없으면 추가
df.head()

aa = df.drop(columns=["class"])
# class 컬럼이 삭제된 새로운 데이터 프레임을 생성ㅎ서 반환. df 자체는 변하지 않음
print(aa)

# 데이터 프레임 행 삭제
bb = df.drop(labels=[0,1], axis = 0)
#행 인덱스 0,1인 행을 삭제하여 새로운 데이터프레임을 생성해서 반환.
# df 자체는 변하지 않음.
print(df)
print(bb)

#아래 에러났으니 다시 확인해볼것 영상보고
# df.drop(labels=[0,1], axis=(), inplace=True)
# # inplace = True df 자체는 변함. df의 행 인덱스 0.1인 행을 삭제
# df



print("=================")
#범주형 열 데이터

age      = pd.Series([ 26, 42, 27, 25, 20,  20, 21, 22, 23, 25]  ) 
score    = pd.Series([3.8,4.2, 2.6,1.0,3.0,4.0, 4.2,2.2,4.1,3.8] ) 
salary =  pd.Series([2700,4000,3000,2700,3200,1000,3000,7000,3200,3500]) 

# 범주형 변수 생성 
stu_class = pd.Categorical ([ 1, 1, 2, 2, 2, 3, 3, 4, 4, 4])  
gender    = pd.Categorical([ 'F', 'M', 'M', 'M', 'M', 'F', 'F','F', 'M', 'M'])
df = pd.DataFrame ( {'age': age, 
                     'score' :  score  ,
                     'salary' : salary,
                      'class' :stu_class,
                       'gender' : gender}
)
print( df ) 
df.describe()


# 복수열 추출
print(type(df.loc [:, ('class', 'score')]))
df.loc [:, ('class', 'score')]


# 조건으로 추출
df[df.score>3.0] # score 가 3.0보다 큰 행만 # 또는 df[df["score"]>3.0]

# 1 반만 추출
df[df["class"]==1 ] 

# 1반 또는 2반 추출
df[ (df["class"] == 1) | (df["class"] == 2)]

df[df["class"].isin ([1,2])] # 1반 또는 2반 추출

df[ (df.score >= 2.0) & (df.score <= 3.0)]

df.loc[ (df.score >= 2.0) & (df.score <= 3.0), ("class", "score")]