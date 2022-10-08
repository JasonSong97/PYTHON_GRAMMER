# set = 집합
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}  # 튜플과의 차이점은 키와 벨류가 없음
print(my_set)

java = {"유재석","김태호","양세형"}  #두개 다 같은 표현
python = set(["유재석","박명수"]) # 리스트로 만들고 set으로 감싸기

#교집합(java 와 python을 모두 할수 있는사람)
print(java & python)
print(java.intersection(python))

#합집합(java도 가능하고python도 가능한 사람)
print(java | python)
print(java.union(python))

#차집합(java만 할수있는 사람, python 뺴고)
print(java-python)
print(java.difference(python))

# 파이썬 할줄 아는 사람 늘어남
python.add("김태호")
print(python)

# java를 까먹음
java.remove("김태호")
print(java)