# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 입력의 마지막에는 0 두 개가 들어온다.

#-> 입력 00이 들어오기 전까지 무한반복 while

# #1 
# while a > 0 and b > 0 :
#     a, b = map(int,input().split())   
#     print(a + b)
  
while True :
    a, b = map(int,input().split())
    if a > 0 and b> 0:
        print(a + b)
    else :
        break