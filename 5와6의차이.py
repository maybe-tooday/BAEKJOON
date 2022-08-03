A ,B = input().split()

#5,6을 모두5로 볼 경우가 최솟값 모두6으로 볼 경우가 최댓값

A_min = A.replace('6','5') #'6'이있으면 '5'로 바꿔줘
B_min = B.replace('6','5')
A_max = A.replace('5','6') #'5'있으면 '6'으로 바꿔줘
B_max = B.replace('5','6')

print(int(A_min)+int(B_min),int(A_max)+int(B_max))