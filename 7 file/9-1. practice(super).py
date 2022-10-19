class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        super().__init__()
        Unit.__init__(self)
        FlyableUnit.__init__(self)
# 2개이상의 부모클래스를 다중상속받으면 순서상 맨처음에 상속받음 ㅇㅇ
#그래서 따로 초기화 시켜줘야함
# 드랍쉽
dropship = FlyableUnit()