"""
    pandas 데이터를 이용하여 그래프 그리기
"""

from os import name
from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.use("ggplot")
# 1행2열 영역 분리
fig, axes = plt.subplots(nrows=1, ncols=2)
ax1, ax2 = axes.ravel() # 그래프 2개 ax1, ax2
#np, random, rand(5,3) : 5행 3열 만큼 난수 저장 0<= x < 1.0
data_frame = pd.DataFrame(np.random.rand(5,3), index=\
["Customer 1", "Customer 2", "Customer 3", "Customer 4", "Customer 5"], 
columns=pd.Index(["Matric 1", "Matric 2", "Matric 3"], 
                 name="Metrics"))
print(data_frame) 

#아래는 첫번 째 그래프 세팅
data_frame.plot(kind="bar", ax=ax1, alpha=0.75, title="Bar plt")
# x축, y축 설정
plt.setp(ax1.get_xticklabels(), rotation=45, fontsize=10)
plt.setp(ax1.get_xticklabels(), rotation=0, fontsize=10)

ax1.set_xlabel("Customer")
ax1.set_ylabel("Value")
ax1.xaxis.set_ticks_position("bottom")
ax1.yaxis.set_ticks_position("left")
# dict : dictionary 데이터 설정
colors = dict(boxes="Darkblue", whiskers="Gray", medians="Red", caps="Black")
print(colors)

# 아래는 두번째 그래프 설정
# ax2 영역에 box형 그래프 설정
data_frame.plot(kind="box", color = colors, sym="r.", ax = ax2, title = "Box Plot")
plt.setp(ax2.get_xticklabels(), rotation=45, fontsize=10)
plt.setp(ax2.get_xticklabels(), rotation=0, fontsize=10)
ax2.set_xlabel("Metric")
ax2.set_ylabel("Value")
ax2.xaxis.set_ticks_position("bottom")
ax2.yaxis.set_ticks_position("left")
