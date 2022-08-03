import sys
sys.stdin = open('상금헌터.txt')

T = int(input()) #테스트 케이스
ab = [list(map(int,input().split())) for _ in range(T)]
#print(ab) #ab[T][0]: a등수 / ab[T][1]: b등수

for t in range(T):
    reward_a = 0 #2017년 1회 코드 페스티벌 상금
    if ab[t][0] == 1:
        reward_a = 5000000
    elif ab[t][0] == 0: #진출하지 못했을 경우
        reward_a = 0
    elif ab[t][0] <= 3:
        reward_a = 3000000
    elif ab[t][0] <= 6:
        reward_a = 2000000
    elif ab[t][0] <= 10:
        reward_a = 500000
    elif ab[t][0] <= 15:
        reward_a = 300000    
    elif ab[t][0] <= 21:
        reward_a = 100000
    
    reward_b = 0 #2018년 2회 코드 페스티벌 상금
    if ab[t][1] == 1:
        reward_b = 5120000
    elif ab[t][1] == 0:
        reward_b = 0
    elif ab[t][1] <= 3:
        reward_b = 2560000
    elif ab[t][1] <= 7:
        reward_b = 1280000
    elif ab[t][1] <= 15:
        reward_b = 640000
    elif ab[t][1] <= 31:
        reward_b = 320000 

    print(reward_a + reward_b) 
        