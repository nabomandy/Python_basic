import matplotlib.pylab as plt # graphic을 위한 모듈
from matplotlib import rc
rc('font', family="Malgun Gothic") # 한글 가능한 폰트 설정

labels = ['개구리', '돼지', '개', '통나무'] # 이름
sizes = [15, 30, 45, 10] # 데이터
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
explode = (0, 0.1, 0, 0) # 중심에서 간격 수치로 지정
plt.title("Pie Chart")
# wedgeprops : 부채꼴 설정
# width : 반지름 대비 비율
# linewidth : 구분선 굵기
wedgeprops = {'width':0.7, 'edgecolor': 'w', 'linewidth':2}
#그래프 작성
# autopct : 부채꼴 내부에 표시되는 내용의 형식.
# startangle : 시작되는 위치 각도 지정. 배치순서 반시계 방향.
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90,wedgeprops=wedgeprops)

plt.show()