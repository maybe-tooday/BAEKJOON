# 출력: Aa0aPAf985Bz1EhCz2W3D1gkD6x
import sys
sys.stdin = open('세로읽기.txt','r')

from collections import deque

que = [deque(list(input()))for _ in range(5)]

print(que,)

# for _ in range(15) #각줄의 최대길이 15