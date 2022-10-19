#input : 사용자 입력을 받는 함수

#내장함수 예제 >> 따로 함수가 내장이 되어있어서 바로 가능한것
language = input("무슨 언어를 좋아하세여?")
print("{0}은 아주 좋은 언어입니다!.".format(language))

#dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())
import random #random은 외장 함수 / random을 가지고 온다
print(dir())
import pickle
print(dir())

print(dir(random))  # 랜덤 모듈내에서 쓸수 있는 것들이 다 나옴 ㅇㅇ

lst = [1,2,3]
print(dir(lst))  #lst 내에서 사용가능한 정보가 나옴

name = "Jim"  
print(dir(name)) 

#google >> list of the python built-in functionb