#끝나면 사라지는 것 지역변수
# 모든 공간에서 부를 수있는것이 전역 변수


# 지역변수
gun = 10 # 총10개 있음
def checkpoint(soldiers):
    gun = gun - soldiers  #요기서의 gun은 checkpoint함수 내에서의 gun/외부 gun 이아님 
    print("[함수 내] 나은 총 : {0}".format(gun))
print("전체 총 : {0}".format(gun))
checkpoint(2)  # 경계근무 2명 나감
print("남은 총 : {0}".format(gun))

#따라서
def checkpoint(soldiers):
    gun = 20
    gun = gun - soldiers
    print("[함수 내] 나은 총 : {0}".format(gun))
print("전체 총 : {0}".format(gun)) # 외부의 gun 10개 나옴
checkpoint(2)  # 경계근무 2명 나감
print("남은 총 : {0}".format(gun)) #내부 총 나옴
 
#전역변수 / 권장은 안함
gun = 10
def checkpoint(soldiers): #경계근무 수=전달값
    global gun  #전역공간에 있는 gun 사용# 지역변수(gun = 10) 임(이거 없으면 오류가 남)
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
print("전체 총 : {0}".format(gun))
checkpoint(2)
print("남은 총 : {0}".format(gun))

gun = 10
def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun #바뀌어진 gun을 외부로 던질 수 있음
print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))