# 마린 : 공격 유닛, 군인. 총을 쏠 수 있음
name = "마린" #유닛의 이름 
hp = 40 # 유닛의 체력
damage = 5  # 유닛의 공격력

print("{0} 유닛이 생성되었습니다.".format(name))
print("체력{0}, 공격력 {1}\n".format(hp, damage))

# 탱크 : 공격 유닛, 탱크, 포를 쏠수 있다. 일반모드/ 시즈모드
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank_name))
print("체력{0}, 공격력 {1}\n".format(tank_hp, tank_damage))

tank2_name = "탱크"
tank2_hp = 150
tank2_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank2_name))
print("체력{0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))

def attack(name, location, damage): # 이름 공격방향 데미지 함수 생성
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format( \
        name, location, damage))

attack(name, "1시", damage)  # 함수 호출
attack(tank_name, "1시", tank_damage)
attack(tank2_name, "1시", tank2_damage)

# 클래스로 해봄 / 위의 tank2 이런식으로는 비효율적
# 클래스는 붕어빵으로 비유 / 서로 연관이 있는 함수와 변수의 집합
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력{0}, 공격력 {1}".format(self.hp, self.damage))  #이렇게 하면 클래스 만듬 ㅇㅇ

marinel = Unit("마린", 40, 5) #self를 제외한 나머지 3부분을 기입
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)