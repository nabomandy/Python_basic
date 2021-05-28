import os

from scipy.sparse import data
current_directory = os.getcwd()
print(current_directory)


import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt

df = pd.read_csv("전처리자료.csv",dtype={"x1": pd.Int64Dtype()}, parse_dates=[3])
df
df.isnull()
df.isnull().sum()

msno.matrix(df)
plt.show()

# 각 열에 결측 데이터가 얼마나 존재하는지 시각화하고 싶다면, bar함수를 사용한다.
msno.bar(df)
plt.show()

df.dropna() # row 삭제

df.dropna(axis=1) #column 삭제

# axis 인수를 1로 설정하면 결측데이터가 있는 열을 제거한다.

df.dropna(thresh=7, axis=1) # thresh 인수를 사용하면 특정 갯수 이상의 비결측 데이터가 있는 행 또는 열만 남긴다.


print("==========================")
import seaborn as sns
# data set 읽기
titanic = sns.load_dataset("titanic")
titanic.tail()

msno.bar(titanic)
plt.show()

msno.matrix(titanic)
plt.show()

# 데이터가 절반 이상이 없는 열을 삭제
titanic = titanic.dropna(thresh=int(len(titanic) * 0.5), axis=1)
msno.matrix(titanic)
plt.show



print("==========================")
# #한글 깨짐
# from matplotlib import font_manager, rc
# font_path = "C:/Windows/Fonts/NGULIM.TTF"
# font = font_manager.FontProperties(fname=font_path).get_name()
# rc('font', family=font)

sns.countplot(titanic.embark_town)
plt.title("embark_town 데이터의 분포")
plt.show()

from sklearn.impute import SimpleImputer

imputer_embark_town = SimpleImputer(strategy="most_frequent")
titanic["embark_town"] = imputer_embark_town.fit_transform(titanic[["embark_town"]])
titanic["embarked"] = imputer_embark_town.fit_transform(titanic[["embarked"]])

msno.matrix(titanic)
plt.show()


# strategy="median"로 하여 중앙값을 대체 값으로 사용한다. 다음 그림에서 걸측값이 사라진 것을 확인할 수 있다ㅏ.
imputer_age = SimpleImputer(strategy="median")
titanic["age"] = imputer_embark_town.fit_transform(titanic[["age"]])

msno.matrix(titanic)
plt.show()


print("==========================")
# Pasty 패키지
# 이번에는 pasty 패키지를 사용하여 데이터 프레임에서 원하는 데이터만 선택하거나 
# 새로운 데이터를 조합 생성하는 방법을 살펴본다. 설명을 위해 PASTY 패키지가 제공하는 demo_data() 함수로
# 다음과 같은 예제 데이터프레임을 만들자
# demo_data() 함수는 x로 시작하는 변수에 대해 임의의 실수 데이터를 생성한다.

from patsy import demo_data

df = pd.DataFrame(demo_data("x1", "x2", "x3", "x4", "x5"))
df


from patsy import dmatrix

dmatrix("x1+0", data=df)

dmatrix("x1 + x2 + x3 + 0", data=df)

# 'dmatrix()'함수는 변수를 어떤 함수에 넣어서 다른 값으로 만드는 수학변환(트랜스폼)도 가능하다.
dmatrix("x1 + np.log(np.abs(x2))", df)

def ten_times(x):
    return 10 * x
dmatrix("ten_times(x1", df)