#반복문 내에서 사용 가능

absent = [2,5] #리스트 변수 생성 
no_book = [7]  #리스트 변수 생성 
for student in range(1, 11) : # 1,2,3,4,5,6,7,8,9,10
    if student in absent :
        continue #계속해서 다음 반복 하는것
    elif student in no_book :
        print("오늘 수업 여기까지.{0}는 교무실로 따라와".format(student))
        break #반복문 종료
    print("{0}, 책을 읽어봐".format(student))