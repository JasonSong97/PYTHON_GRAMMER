import pickle #모듈 불러오기

# with open(profil.pickle열고 읽기목적) as profile_file에다가 저장
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))
#close 필요 없음 >> with는 자동으로 close가 됨 

#
with open ("study.txt", "w", encoding="utf8") as study_file:  #encoding = "utf8"의미는 한글로 작성한다는 것
    study_file.write("파이썬을 열심히 공부하고 있어요")

#
with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())