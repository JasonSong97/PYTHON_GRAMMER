# #키와 벨류 / 중요!! / 사전 보면 단어와 의미 이런느낌? / 중복 안됨

cabinet = { 3 : "유재석", 100 : "김태호"}  # 키 : 벨류
print(cabinet[3]) #키를 입력시 대괄호
print(cabinet[100])

print(cabinet.get(3)) # == print(cabinet[3])
print(cabinet[4])     # 사전안에 해당 숫자가 없을경우 1. get을 이용하면 뒷 내용들을 송출 2. 대괄호 이용시에는 오류 후 끝
print(cabinet.get(4))   
print("Hi")

print(cabinet.get(4, "사용 가능"))  
print("hi")

print(3 in cabinet)  # 3이 캐비넷 안에 있음? 이뜻임
print(5 in cabinet)

#str사용시
cabinet = { "A-3" : "유재석", "B-100" : "김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

#새손님  변수(키) = 벨류
print(cabinet)
cabinet["A-3"] = "김종국"  #A-3에 김종국 넣는 것
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님  del 변수(키)
del cabinet["A-3"]
print(cabinet)

# 키들만 출력 / keys
print(cabinet.keys())

#values 들만 출력 / values
print(cabinet.values())

# 키 밸류 쌍으로 출력 / items
print(cabinet.items())

#목용탕 폐점 / clear
cabinet.clear()
print(cabinet)

