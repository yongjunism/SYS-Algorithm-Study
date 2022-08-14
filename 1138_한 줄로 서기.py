n = int(input())
arr = list(map(int, input().split()))

ans = [0] * n 

for i in range(1, n+1):
    cnt = arr[i-1]
    r_cnt = 0 

    for j in range(n):
        if cnt == r_cnt and ans[j] == 0:
            ans[j] = i
            break 
        elif ans[j] == 0:
            r_cnt += 1 

print(*ans)