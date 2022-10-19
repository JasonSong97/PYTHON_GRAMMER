#자료구조의 변경

#커피숍
menu = {"커피", "우유", "주스"}   
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

#{'커피', '우유', '주스'} <class 'set'>
#['커피', '우유', '주스'] <class 'list'>
#('커피', '우유', '주스') <class 'tuple'>
#{'주스', '우유', '커피'} <class 'set'>