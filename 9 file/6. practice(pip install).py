#이미 만들어진 패키지 가져다 사용하기!
#구글에다가 pypi로 검색하기
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())