#(난수)무작위로 뽑는것 / 랜덤 library 사용 하기

from random import *

print(random())  # 0.0 <= X < 1.0
print(random() * 10)  # 0.0 <= X < 10.0
print(int(random() * 10))  # 0 <= X < 10
print(int(random() * 10) + 1)  # 1 <= X <= 10

# 로또 값 뽑기
print(int(random() * 45) + 1)  # 1 <= X <= 45
print(int(random() * 45) + 1)  # 1 <= X <= 45
print(int(random() * 45) + 1)  # 1 <= X <= 45
print(int(random() * 45) + 1)  # 1 <= X <= 45
print(int(random() * 45) + 1)  # 1 <= X <= 45
print(int(random() * 45) + 1)  # 1 <= X <= 45

# 쉬운방법
print(randrange(1, 46))  # 1 <= X < 46
print(randint(1, 45))  # 1 <= X <= 45