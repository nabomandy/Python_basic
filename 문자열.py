
#문자열 ============
sentence = '나는 개발자입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)


#슬라이싱
jumin = "910113-1234567"

print("성별 : " +jumin[7])
print("연 : " + jumin[0:2]) # 0부터 2 직전까지 (0,1번째 값)
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6]) #처음부터 6직전까지
print("뒤 7자리 : " + jumin[7:] ) #7번째부터 끝까지
print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) #맨 뒤에서 7번째부터 끝까지


#문자열처리함수
python = "Python is Amazing"
print(python.lower()) #소문자로 출력
print(python.upper())
print(python[0].isupper()) #대문자가 맞는지
print(len(python)) #문자열의 길이 반환
print(python.replace("Python", "Java"))

index = python.index("n") #해당글자가 몇번째 위치에 있는지
print(index)
index = python.index("n", index + 1) 
print(index) 

print(python.find("Java")) #원하는 값이 포함되었지 않을때는 -1을 반환한다
# print(python.index("Java")) #원하는 값이 포함되었지 않을때는 오류를 내면서 프로그램을 종료
print("hi")

print(python.count("n")) #n이라는 글자가 몇번 나오는지


#문자열 포맷
print("a" + "b")
print("a", "b")

# 방법 1
print("나는 %d살입니다." % 20) #d는 정수값만 입력할 수 있다
print("나는 %s을 좋아해요." % "파이썬") #s는 문자열을 넣겠다는 거, 정수건 하나의 문자건 값 출력을 할 수 있다.
print("Apple 은 %c로 시작해요" % "A") #c는 문자(한글자)만 받겠다는 거
# %s 
print("나는 %s살입니다." % 20)
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# 방법 2
print("나는 {}살입니다." .format(20))
print("나는 {}색과 {}색을 좋아해요." .format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요." .format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨간"))

#방법 3
print("나는 {age}살이며, {color}색을 좋아해요." .format(age = 20, color = "빨간"))
print("나는 {age}살이며, {color}색을 좋아해요." .format(color = "빨간", age = 20))

# 방법 4 (v3.6 이상 ~)
age = 20    
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")


# 탈출문자======================
# \n : 줄바꿈
print("백문이 불여일견\n백견이 불여일타")

# \" \' : 문장 내에서 따옴표 그대로 출력
#저는 "앤디배"입니다. 라고 출력하고 싶다고 가정
print("저는 '앤디배'입니다.")
print('저는 "앤디배"입니다.')
print("저는 \"앤디배\"입니다.")
print("저는 \'앤디배\'입니다.")

# \\ : 문장 내에서 \
print("C:\\study_vscode")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") # Red Apple -> PineApple

# \b : 백스페이스(한 글자 삭제)
print("Redd\bApple") #RedAppler

# \t : 탭
print("Red\tApple") #Red     Apple

# Quiz) 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오

# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com 
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
#                           (nav)     (5)           (1)              (!)
# 예)생성된 비밀번호 : nav51!

# url = "http://naver.com"
url = "http://google.com"
my_str = url.replace("http://", "") #규칙 1
# print(my_str)
my_str = my_str[:my_str.index(".")] #규칙 2
#처음부터 처음나오는 "." 위치까지만 자른다.
#my_str[0:5] -> 0 ~ 5 직전까지. (0,1,2,3,4)
# print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1} 입니다.".format(url, password))
# print(name[7:10]+name.count[7:12])










