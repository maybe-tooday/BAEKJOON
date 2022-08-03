import sys
sys.stdin = open('카드놀이.txt','r')

AB = [list(map(int,input().split())) for _ in range(2)]
#print(AB)
winner = 'D'
score_a = 0
score_b = 0

for _ in range(10):
    if AB[0][_] > AB[1][_]:
        score_a += 3
        winner = 'A'
    elif AB[0][_] < AB[1][_]:
        score_b += 3
        winner = 'B'
    elif AB[0][_] == AB[1][_]:
        score_a += 1
        score_b += 1
print(score_a,score_b)
print(winner)
