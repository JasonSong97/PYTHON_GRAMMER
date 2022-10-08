# 파이썬에서는 함수 정의나 클래스 즉 파이썬 문장들을 담고 있는 것을 모듈이라고 함
# 모듈은 py로 끝남(확장자.py)
# 모듈은 쓸려고 하는 같은 경로에 있어야함 / 아니면 같은 라이브러리가 모여있는 폴더에 있어야함

#1
import theater_module
theater_module.price(3) # 3명이서 영화 보러 갔을 떄 가격
theater_module.price_morning(4) # 4명이서 조조할인 가격
theater_module.price_soldier(5) # 5명의 군인 할인

#2
import theater_module as mv  # 의미는 theater_module 를 mv로만 호출하는 것  /  별명 느낌임 ㅇㅇ
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

#3
from theater_module import *#전부
price(3)
price_morning(4)
price_soldier(5)

#4
from theater_module import price, price_morning  # 사용하고 싶은 모듈만 기입
price(5)
price_morning(6)

# 만약 군인만 알고 싶은 경우는 (별명 붙이기)
from theater_module import price_soldier as price # theater_module 에서 price_soldier 함수를 가져다 쓰는데 별명을 price로 함
price(5)
