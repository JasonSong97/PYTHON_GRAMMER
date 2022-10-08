def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") # end = " " 는 해당 print 구문을 사용하고 밑에있는 구문도 계속해서 이어 붙인다는 의미 ㅇㅇ
    print(lang1, lang2, lang3, lang4, lang5)       # >> 두 문장이 하나로 출력
profile("유재석", 20, "Python", "Java", "C", "C+", "C#")
profile("김태호", 25, "Kotlin", "Swift", "", "","")

#유재석이 언어를 더 배우거나 하면? 이럴 때 쓰는게 가변인자
#서로다른 갯수의 값을 넣을 떄는 가변인자를 사용
def profile(name, age, *language):  #가변인자 조건  *language
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") # end = " " 는 해당 print 구문을 사용하고 밑에있는 구문도 계속해서 이어 붙인다는 의미 ㅇㅇ
    for lang in language:
        print(lang, end=" ")
    print()
profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift")