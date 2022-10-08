#에러가 생길때 사용

#계산기

print("나누기 전용 계산기입니다.")
num1 = int(input("첫 번쨰 숫자를 입력하세요 : "))
num2 = int(input("두 번쨰 숫자를 입력하세요 : "))
print("{0} / {1} = {2}".format(num1, num2, int(num1/num2))) #한글로 작성 하면 오류남

#그래서

try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    # nums.append(int(nums[0]/nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))  #int 로 감싸는 이유는 실수가 나올 가능성이 있기 떄문에
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:  # 6 과 0으로 하면 0으로 못 나눈다고 함
    print(err)
# except:  # ValueError와ZeroDivisionError를 제외하고 모든 것을 다 포용
#     print("알 수 없는 에러가 발생하였습니다.")
except Exception as err:  # 어떤 에러인지 알고 싶으면 print(err)하면 됨
    print(("알 수 없는 에러가 발생하였습니다."))
    print(err)