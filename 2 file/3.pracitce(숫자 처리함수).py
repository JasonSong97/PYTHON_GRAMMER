# 파인썬에서 제공하는 숫자 함수들 ㅇㅇ
# abs pow max min round ...

print(abs(-5))          #abs 절댓값 의미
print(pow(4, 2))       # 4*4 = 16   4의 2승 이라는 의미
print(max(5, 12))      # 2개중에서 가장 큰 수를 뽑아줌
print(min(4, 10))        # 2개중에서 가장 작은 수를 뽑아줌
print(round(3.14))    # 반올림
print(round(4.99))

# math libaray 이용 방법

from math import * #math libaray에있는 모든 것을 이용한 다는 의미
print(floor(4.99))   # 내림
print(ceil(3.14))   #올림
print(sqrt(16)) # = 4      # 제곱근(루트) 구하는 방법    16은 4의 제곱근