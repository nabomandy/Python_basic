# 함수

from ast import get_source_segment
from os import name


def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money):
    print("입금이 완료 되었습니다. 잔액은 {0}입니다.".format(balance + money))
    return balance + money
    
def withdraw(balance, money): #출금
    if balance >= money : #잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance
    
def withdraw_night(balance, money): #저녁에 출금
    commission = 100 # 수수료 100원
    return commission, balance - money - commission
    
        
    
balance = 0 # 잔액
balance = deposit(balance, 1000)
# print(balance)
# balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print("수수료는 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))


# #기본값
# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이: {1}\t주 사용 언어: {2}"\
#         .format(name, age, main_lang))

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업.

# def profile(name, age=17, main_lang="파이썬"): #전달받지 않았을 때 디폴트값으로 들어간다. 17과 파이썬이
#     print("이름 : {0}\t나이: {1}\t주 사용 언어: {2}"\
#         .format(name, age, main_lang))

# profile("유재석")
# profile("김태호")


# 키워드 값
def profile(name, age, main_lang):
    print(name, age, main_lang)
    
profile(name="유재석", main_lang="파이썬", age=20) #순서가 섞여있어도 잘 전달 된다.
profile(main_lang="자바", age=25, name="김태호")


# 가변인자
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이: {1}\t".format(name,age), end=" ") #end=" " 이 프린트 문이 끝날 때 줄바꿈 하지 않고 이렇게 끝낸다는 의미.
#     print(lang1, lang2, lang3, lang4, lang5)
    
def profile(name, age, *language):
    print("이름 : {0}\t나이: {1}\t".format(name,age), end=" ") #end=" " 이 프린트 문이 끝날 때 줄바꿈 하지 않고 이렇게 끝낸다는 의미.
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile("김태호", 25 ,"Kotlin", "Swift")


# 지역변수
gun = 10 

def checkpoint(soldiers): # 경게근무
    global gun # 전역 공간에 있는 gun 사용 -> 지금 전역공간에 있는 77번 줄의 gun을 이 함수 내에서 사용하겠다는 의미 -> 일반적으로 권장되는 방법은 아님.
    gun = gun - soldiers
    print("[함수  내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수  내] 남은 총 : {0}".format(gun))
    return get_source_segment

print("전체 총 : {0}".format(gun))
# checkpoint(2) # 2명이 경계 근무 나감
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))