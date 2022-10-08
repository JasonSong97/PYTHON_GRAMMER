#일반 유닛 ... 메딕
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# 일반 유닛과 공격유닛의 공통점이 보인다!! >> 상속 시켜버림 >> Unit을 AttackUnit으로 상속

#공격 유닛
class AttackUnit(Unit):#상속 시켜버리기
    def __init__(self, name, hp, damage):
        # self.name = name        #상속시에는 없애기
        # self.hp = hp           
        Unit.__init__(self, name, hp)  #요거 추가
        self.damage = damage
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp >= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


#메딕


#파이어뱃
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

#공겨 2번 받음
firebat1.damaged(25)
firebat1.damaged(25)