# 표준체중 구하기 : 

#남자 : 키m x 키m x 22
#여자 : 키m x 키m x 21

#조건1 표준 체중은 별도의 함수 내에서 계산
    #함수명 : std_weight
    #전달값 : 키(height), 성별(gender)
#조건2 표준 체중은 소수점 둘쨰자리까지 표시

# 키 175cm 남자의 표준 체중은 67.38kg 입니다.


# 스스로 푼것
def std_weight(gender, height):
    if gender == "남자" :
        print("키 {0} 남자의 표준 체중은 {1} 입니다.".format(height,round((height/100)**2*22, 2)))
        return round((height/100)**2*22, 2)
    else :
        print("키 {0} 여자의 표준 체중은 {1} 입니다.".format(height,round((height/100)**2*21, 2)))

std_weight("남자", 181)


# 강의해설
def std_weight(height, gender): #std_weight함수
    if gender == "남자":
        return height**2*22
    else:
        return height**2*21

height = 175 #변수
gender = "남자" #변수
weight = round(std_weight(height/100, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))
