# 월 4회 스터디 / 3번 온라인 / 1번 오프라인
# 조건 1. 랜덤으로 날짜 정하기 2. 월별 날짜가 다르니까 걍 최소일수 28일로 결정 3. 매월 1~3일은 제외
#출력문예제
#오프라인 스터디 모임 날짜는 매월 x일로 선정되었습니다. 

from random import *
number = str(randint(4, 28))
print("오프라인 스터디 모임 날짜는 매월" + number + "일로 선정되었습니다.")

# 새로운방식
from random import *
study = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 {0}일로 선정되었습니다.".format(study))