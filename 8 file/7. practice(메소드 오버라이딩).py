#부모 클래스 말고, 자식클래스에서 정의한 매소드를 사용하고 싶을때 .매소드를 새롭게 정의하는 것 = 오버라이딩

#일반 유닛(지상)
class Unit:  
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))

#공격 유닛
class AttackUnit(Unit):  
    def __init__(self, name, hp, speed, damage):        
        Unit.__init__(self, name, hp, speed)  
        self.damage = damage

    def attack(self, location):#공격 함수
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))
            
    def damaged(self, damage): #공격받은 함수
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp >= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

#드랍쉽

#날수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))
    
#공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable): 
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 스피드는 0
        Flyable.__init__(self, flying_speed)
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

#벌쳐
vulture = AttackUnit("벌쳐", 80, 10, 20)

#배틀크루저
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시") >> 매번 지상유닛인지 공중인지 구별 = 너무 귀찮음
#그래서 메소드 오버라이딩 쓰면 해결!
battlecruiser.move("9시")


#정리

#FlyableAttackUnit(move 재정의) >> Flyable
#                  >> AttackUniy >> Unit  (move함수)