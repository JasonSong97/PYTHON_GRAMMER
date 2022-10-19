def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name="유재석", main_lang="파이썬", age=20)  # 튜플형식
profile(main_lang="자바", age=25, name="김태호")

# 함수에서 전달 받는 키워드를 이용해서 
# 호출을 하면 해당 키워드의 값이 섞여있어도 알아서 처리됨