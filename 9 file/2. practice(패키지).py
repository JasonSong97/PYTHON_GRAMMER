# 모듈들을 묶어놓은 집합

import travel.thailand   # import 뒤에는 함수or 클래스는 불가 / 반드시 패키지나 모듈만 가능
trip_to = travel.thailand.ThailandPackage()  #객체생성
trip_to.detail()

from travel.thailand import ThailandPackage # travel 패키지에서 thailand 모듈 안에있는 thailandpackage를 불러온것
trip_to = ThailandPackage()
trip_to.detail

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()