from travel import *
trip_to = vietnam.VietnamPackage() #요렇게 오류가 나옴!
trip_to = thailand.ThailandPackage()
trip_to.detail()

# 이유는 * 은 travel에 있는 모든 것을 가져오겠다는 의미
# 원래는 원하는 것을 공개하고 원하지 않은것은 비공개로 설정 해야함 >> 범위 설정 필요
# __init__.py 가서 __all__ = ["vietnam", "thailand"] 적기