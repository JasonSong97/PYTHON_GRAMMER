#1
def profile(name, age, main_lang):  # 튜플 함수
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" \
        .format(name, age, main_lang))
profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업. 요때 기본값을 씀 ㅇㅇ 패시브 같은거임

#2
def profile(name, age=17, main_lang="파이썬"):   #기본값 기입하는 것 / 17과 파이썬은 기본값으로
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" \
        .format(name, age, main_lang))

profile("유재석")
profile("김태호")