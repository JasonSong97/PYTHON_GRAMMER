# 댓글 작성자중 1명은 치킨 3명은 커피
#조건 1. 20명 작성/ 아이디는 1~20 2. 무작위로 결정+중복 불가 3. random, shuffle과 sample 사용할것

#출력예제
# --당첨자 발표--
# 치킨 당첨자 : 1
# 커피 당첨자 : [2,3,4]
# --축하합니다--

# 활용예제
# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst,1))   # lst인자(리스트)에서 1개만큼 뽑는다는 뜻

from random import *
users = range (1, 21)   # 1부터 20까지 숫자를 생성
# print(type(users))
users = list(users)
# print(type(users))

shuffle(users)
print(users)

winners = sample(users, 4)   # 4명중에서 1명은 치킨 3명은 커피
print( "--당첨자 발표--")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("--축하합니다--")


#스스로 푼 방법
from random import *
lst = range (1, 21)
lst = list(lst)
shuffle(lst)

당첨자 = sample(lst, 4)
print("치킨 당첨자{0}".format(당첨자[0]))
print("커피당첨자는{0} 입니다.".format(당첨자[1:]))