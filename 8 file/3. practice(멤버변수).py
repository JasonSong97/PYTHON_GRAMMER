#멤버변수 : 어떤 클래스 내에서 정의된 변수 그 변수를 가지고 초기화 또는 사용 가능

class Unit:
    def __init__(self, name, hp, damage): 
        self.name = name   # 요놈들이 멤버변수임 ㅇㅇ / 즉 어떤 클래스 내에서 정의된 변수 그 변수를 가지고 초기화 또는 사용 가능
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력{0}, 공격력 {1}".format(self.hp, self.damage)) 

marinel = Unit("마린", 40, 5) 
marine2 = Unit("마린", 40, 5)  #__init__함수는 self를 제외한 갯수만큼 변수로 만들어야 함 
tank = Unit("탱크", 150, 35)

#레이스 만들거임 ㅇㅇ

wraith1 = Unit("레이스", 80, 5)
print("유닛이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))    # 멤버변수 wraith1.name와 wraith1.damage

#마인드 컨트롤 함

wraith2 = Unit("빼았은 레이스", 80, 5)
wraith2.clocking = True  # 클로킹 변수는 위 클래스에 없음 / 하지만 외부에서 변수를 생성

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))