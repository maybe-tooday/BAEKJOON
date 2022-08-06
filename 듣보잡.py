import sys
sys.stdin = open("듣보잡.txt")

N, M = map(int,input().split()) #N:듣지못한사람, M:보지못한사람
N_set = set(input() for _ in range(N))
M_set = set(input() for _ in range(N))
NM_list = []

for N_one in N_set:
    if N_one in M_set:
        NM_list.append(N_one)

NM_list.sort()
print(len(NM_list))
for a in NM_list:
    print(a)