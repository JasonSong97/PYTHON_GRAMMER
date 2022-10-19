# 프로그램상의 사용하는 데이터를 파일형태로 저장 / 누군가에게 주면 / 피클을 이용해서 데이터 가져와서 코드에서 사용
# 피클을 사용하기 위해서는 b(바이너리)를 항상 정의를 해줘야함

#데이터를 파일로 저장하기
import pickle #모듈 import 하기
profile_file = open("profile.pickle", "wb")   #w 는 쓰기 목적 b는 바이너리라는 뜻  / 따로 인코딩 할필요 없음ㅇㅇ
profile = {"이름" : "박명수", "나이" : 30, "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) #dump함수 / profile에 있는 정보를 profile_file에 저장 / 피클을 이용해서 데이터를 파일에 작성하는 것
profile_file.close()

#데이터 가져오기  load
profile_file = open("profile.pickle", "rb")   # 읽기로할때는 r 적기 / 피클 사용할거니까 바이너리 적기
profile = pickle.load(profile_file)  #load 파일에 있는 정보를 프로필에 불러오기
print(profile)
profile_file.close()