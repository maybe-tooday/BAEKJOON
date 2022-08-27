H, M = map(int,input().split())

if M < 45:
    H = H - 1
    M = M + 15
    if H == -1:
        H = 23
    print(H, M)
else :
    print(H, (M-45))
