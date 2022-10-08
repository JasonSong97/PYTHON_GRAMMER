class Unit:
    def __init__(self, name, hp, damage):  #__init__파이썬 생성자
        self.name = name   #마린이나 탱크처럼 어떤 클래스로부터 생성되는 것을 객체라고 함  /  인스턴스
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력{0}, 공격력 {1}".format(self.hp, self.damage))  #이렇게 하면 클래스 만듬 ㅇㅇ

marinel = Unit("마린", 40, 5)   #클래스로 만들어지는 것을 객체
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

marine3 = Unit("마린")  #함수에 정의된 갯수만큼 기입해야함 self 뺴고(name, hp, damage), 그 외에는 오륜 