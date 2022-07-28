n = int(input())

#1
for i in range(1,n+1): # 1~ 입력한숫자
    print(' '*(n-i),'*'*i, sep='')
    # '' "" 구분해서 사용해보기
#rjust함수  '문자열'.rjust(전체칸수,넣을문자)

#2
for i in range(1,n+1):
    print(('*'*i).rjust(n,' '))