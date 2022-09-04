N = int(input())
i = 0 #N값 더하기
sum_i = 1

while N > sum_i:    
    i += 1
    sum_i += 6 * i
    print(sum_i,i*6,N)

print(i+1)