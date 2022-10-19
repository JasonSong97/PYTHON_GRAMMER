#애완동물을 소개해 주세요~

#변수는 값을 저장하는 공간

name = "연탄이"  # 문자열이여서 감쌈
animal = "강아지"  # 문자열이여서 감쌈
age = 4  #정수형자료(숫자형)
hobby = "산책"
is_adult = age >= 3 #불리안 형태

# 변수 = 변수값

print("우리집" + animal + "의 이름은" + name + "에요")  
hobby = "공놀이"
print(name, "는", age, "살이며,", hobby, "을 아주 좋아해요")
print(name + " 는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")  #정수형을 출력하기 위해서는 str로 감싸주기!
print(name, "는 어른일까요? " , is_adult)
print(name + "는 어른일까요? " + str(is_adult)) #불리안도 str 로 감싸주어야함

# +대신 , 로 대체가능하다
