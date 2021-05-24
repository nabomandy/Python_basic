
import matplotlib.pyplot as plt # pip install ggplot

# 아래는 한글 깨질 때 문제
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

plt.style.use("ggplot") # ggplot으로 그리겠다는 의미
subjects = ["자바","JSP","SPRING","HADOOP","PYTHON"] # 막대그래프의 x좌표의 값
print(range(len(subjects)))
subjects_index = range(len(subjects)) # subjects_index : 0 ~ 4값을 저장
print(type(subjects_index))
scores = [65, 90, 85, 60, 95] # 막대그래프로 표현할 값.
#그래프 출력
fig = plt.figure() # 그래프로 그릴 수 있는 공간. 도화지
# 도화지 영역 분리. 하나의 도화지에 여러개의 그림 가능.
# 1행 1열 분리 => 한개 그림. 분리 안함.
# 1 : 1번째 그림.
# ax1 : 그래프가 그려지는 영역
ax1 = fig.add_subplot(1,1,1) #  1x1(행x열)의 subplot을 생성한다는 의미이고 세 번째 인자 1은 생성된 subplot 중 첫 번째 subplot을 의미합니다.
# ax1.bar : 막대 그래프
# subjects_index : x좌표 내용 인덱스
# scores : 막대그래프로 표현할 데이터 값
ax1.bar(subjects_index, scores, align="center", color="darkblue")
# xaxis : x축 위치
# yaxis : y축 위치
ax1.xaxis.set_ticks_position("bottom")
ax1.yaxis.set_ticks_position("left")

# xticks : x축
# rotation : x축에 표시되는 내용의 방향
plt.xticks(subjects_index, subjects, rotation=(), fontsize="small")
# x축 제목
plt.xlabel("과목")
plt.ylabel("점수") # y축 제목
plt.title("과정 점수")
# 메모리 저장된 이미지 파일로 생성
plt.savefig("bar_plot.png", dpi=400, bbox_inches="tight")
plt.show() # 메모리에 있는 그래프 이미지를 화면 보여줌
