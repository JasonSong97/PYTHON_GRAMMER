# 반복문

#1
customer = "토르"
index = 5 #변수 생성
while index >= 1: 
    print("{0}, 커피가 준비 되었습니다. {1}번 남았어요.").format(customer, index)
    index = index - 1
    if index == 0 :
        print("커피는 폐기처분되었습니다.")

#2
customer = "아이언맨"
index = 1
while True :
    print("{0}, 커피가 준비 되었습니다.호출 {1} 회".format(customer, index))
    index += 1   #무한으로 나옴 그래서 control + c를 누르기

#3
customer = "토르"
person = "Unknown"

while person != customer:    #조건을 만족할때까지 계속 문장을 반복함 ㅇㅇ
    print("{0}, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?")