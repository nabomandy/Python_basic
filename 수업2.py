"""
    210524 월요일
    csvex2.py : 파일을 읽기 위한 모듈 codecs 사용
"""

import codecs
filename = "jeju1.csv"
csv = codecs.open(filename, "r", "UTF-8").read()
data = [] # 한줄을 ,분리한 내용을 저장.
rows = csv.split("\r\n") # line별로 나눠서 리스트로 생성
for row in rows:
    if row == "" : continue
    cells = row.split(",")
    data.append(cells)
outfp = open("jeju1.txt", "w", encoding='UTF-8')    
for c in data:
    print(c[0], c[1], c[2])
    outfp.write(" ".join(map(str,c)) + "\n")
outfp.flush()
outfp.close()