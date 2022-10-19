#입금
def open_account():   
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money): #괄호 안에는 전달값을 기입 / # 입금함수
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance+money))
    return balance+money #반환값  / # 리턴에 하나의 값만 보냄
balance = 0 # 잔액
balance = deposit(balance, 1000)#deposit함수
print(balance)

#출금
def withdraw(balance, money):
    if balance >= money: #잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance-money))
        return balance-money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance  # 리턴에 하나의 값만 보냄
balance = 0 # 잔액
balance = deposit(balance, 1000)#withdraw함수
# balance = withdraw(balance, 2000)
balance = withdraw(balance, 500)

#밤 출금 수수료
def withdraw_night(balance, money):
    commission = 100    #수수료 변수
    return commission, balance - money - commission   #튜플형식(2가지 값)으로 보냄
balance = 0 #잔액 
balance = deposit(balance, 1000)  
commission, balance = withdraw_night(balance, 500)
print("수수료{0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))

# balance = 0 #잔액
# balance = deposit(balance, 1000)  
# print(balance)