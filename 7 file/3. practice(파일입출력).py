#
score_file = open("score.txt","w", encoding="utf8") #파일 열기 / 쓰기용 / 한글
print("수학 : 0", file=score_file)
print("영어 : 50",file=score_file)
score_file.close()  #파일 닫기 / 항상 해줘야함

#
score_file = open("score.txt","a", encoding="utf8")  # a 는 내용이 있는 것에 계속 쓰겠다는 뜻
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")    #1에서는 줄바꿈이 필요 없음 하지만 score_file에서는 줄바꿈을 해줘야함
score_file.close()

# 파일 읽어 오기
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())  #해당 파일의 모든 내용을 다 가져오는 것
score_file.close()

#한줄씩 읽어 오기(줄바꿈 있음)
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline())  # 줄별로 읽기, 한 줄읽고 커서는 다음 줄로 이동
print(score_file.readline())  
print(score_file.readline())
print(score_file.readline())  
score_file.close()

#한줄씩 읽어 오되 줄바꿈 안하고 싶을 때
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="")# 줄바꿈 안하고 싶으면 end=""해주면 됨 print(score_file.readline(),end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")  
score_file.close()

#다른 사람이 가져온 파일에 관해서는 몇줄인지 모르니까 모르는 거 처리 방법
score_file = open("score.txt", "r", encoding="utf8")
while True:   #반복문
    line = score_file.readline()   #한줄씩 읽기 변수 생성
    if not line :   #라인이 없으면 
        break  #끝!!!반복문 탈출쓰
    print(line, end="")     #라인 내용이 있으면 출력  /줄바꿈 안하고 싶으면 end=""해주면 끝
score_file.close()    # 닫아주기

#리스트로 처리
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()  #모든 라인을 가지고 와서 리스트 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()