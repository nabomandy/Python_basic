"""
    3차원 그래프 그리기
"""


from mpl_toolkits.mplot3d import Axes3D# 3차원 그래프 모듈
import matplotlib.pyplot as plt
import numpy as np

n = 100
xmin, xmax, ymin, ymax, zmin, zmax = 0, 20, 0, 20, 0, 50
cmin, cmax = 0, 2
#np.random.rand(n) : 난수 100
xs = np.array([xmax - xmin] * np.random.rand(n)+xmin) # 0~20사이의 난수
ys = np.array([ymax - ymin] * np.random.rand(n)+xmin) # 0~20 사이의 난수
zs = np.array([zmax - zmin] * np.random.rand(n)+xmin) # 0 ~ 50 사이의 난수
color = np.array([(cmax - cmin) * np.random.rand(n) + cmin]) # 0 ~ 2 t사이의 난수
plt.rcParams["figure.figsize"] = (6,6) # 그래프의 크기 지정
fig = plt.figure()
ax =Axes3D(fig) # 3차원 그래프를 그리기 위한 설정
#cmap : colormap을 Greens 계역
ax.scatter(xs,ys,zs,c=color,marker='o',cmap="Greens")
plt.show()