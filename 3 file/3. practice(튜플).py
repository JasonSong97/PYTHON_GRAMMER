#내용 변경이나 추가 불가능 / 속도가 리스트보다 빠름 / 변경되지 않은 목록을 할때 사용

menu = ("돈까스", "치즈까스") # 튜플 사용시 ()사용 >> 추가 X
print(menu[0])
print(menu[1])

# menu.add("생선까스")  #튜플은 더하거나 뺴지 못함 ㅇㅇ

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

#튜플 이용하는 경우 >> 서로 다른 값에 변수를 입력하는 것
(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)