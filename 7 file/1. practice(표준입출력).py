print("Python", "Java", "JavaScpirt", sep=" vs ")  #sep 는 문자들 사이사이에 같은 걸 넣어주는 것
print("Python", "Java", sep=",", end="?!")  # end 다음은 마지막에 덧붙이는 것 / 연속으로 붙이기
print("무엇이 더 재밌을까요?")

import sys #sys라는 모듈을 import함
print("Python", "Java", file=sys.stdout)  #표준 출력으로 처리 / 잘 출력되는 것
print("Python", "Java", file=sys.stderr)  #표준 에러로 처리 / stderr은 따로 처리를 해야됨 ㅇㅇ


#시험성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items(): # subject, score 2개의 변수로 정의 / item 은 키와 벨류 다 나옴 / #키 : 벨류 를 튜플로 보내줌
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")#왼쪽으로 8칸 정렬 해달라는것, score

#은행 대기순번표
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))   #3크기만큼 공간을 확보를 하고 나머지는 0으로 채운다는 뜻

#표준입력 / 으로 받으면 항상 문자열로 받게됨
answer = input("아무값이나 입력하세요 : ")
print(type(answer))
print("입력하신 값은 " +answer+"입니다.")