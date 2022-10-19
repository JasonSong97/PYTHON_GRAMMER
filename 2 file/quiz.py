# http://naver.com
# 1. http:// 를 제거 2. 처음 만나는 점(.) 이후 부분은 제거 3. 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성


url = "http://google.com"  #변수 생성
my_str = url.replace("http://", "")  #replace 함수 사용
my_str = my_str[:my_str.index(".")]  #my_str변수에 있는 문자열 중에서 처음부터 . 까지 자른다는 것

password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
                            #문자               문자
print("{0} 의 비밀번호는 {1} 입니다.".format(url, password))

# 내가 푼 풀이
x = "http://naver.com"
x = x[-9:-4]
print(x+str(len(x))+str(x.count("e"))+"!")