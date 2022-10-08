python = "Python is Amazing"   #변수 기입
# # 변수.함수 >> 이런식으로

print(python.lower())  # 소문자로 바꾸는 거임
print(python.upper())  # 대문자로 바꾸는 거임
print(python[0].isupper())  # 해당 함수의 0번째가 대문자인지 묻는 것 >> 불 형태로 나옴
print(len(python))  #길이를 의미함 
print(python.replace("Python", "Java"))  # 대체하는 것 replace

# index 어떤 문자가 어떤 위치에 있는지 알려주는 함수
index = python.index("n")   #n이 몇번쨰에 위치하는지 알려주는 함수를 index라는 변수에 넣기
print(index)
index = python.index("n", index + 1)     # 파이썬변수에서 인덱스 함수를 써서 n이 5번째에 있으니, 5+1인 6번쨰부터 n을 찾기
print(index)

print(python.find("Java"))     #내가 원하는 값이 없으면 -1로 알려줌
print(python.index("Java"))       #오류남 / 그래서 뒤에 다른 문장이 실행 x

print(python.count("n"))       # 해당 함수에 n이 몇번 들어있는지 counting
