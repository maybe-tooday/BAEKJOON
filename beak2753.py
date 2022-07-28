# 연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.

year = int(input())
a = 0

if year%4 == 0 :
    if year % 100 != 0 :
        a = 1
    elif year % 400 == 0 :
        a = 1

print(a)