H,M = map(int,input().split())

#H가 0일 경우
if H == 0:
    H = H + 24
    
#H가 24일 경우
#M이 45보다 클 경우
if H == 24 and M >=45 :
    H = 0
    M = M - 45
    print(f"{H} {M}")
    #M이 45보다 작을 경우
elif M < 45 :
    H = H - 1
    M = M + 15
    print(f"{H} {M}")
else : #M이 45보다 클 경우
    M = M - 45
    print(f"{H} {M}")
        
    