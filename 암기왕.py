import sys
sys.stdin = open('암기왕.txt')

T = int(input())

for t in range(T):
    N = int(input())
    N_list = list(map(int,input().split()))
    M = int(input())
    M_list = list(map(int,input().split()))

    for m in M_list:
        if m in N_list:
            print(1)
        else:
            print(0)