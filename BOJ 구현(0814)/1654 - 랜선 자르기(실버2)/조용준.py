import sys
input = sys.stdin.readline

def binary_search(cables, n):
    low, high = 1, max(cables)
    while low <= high:
        mid = (low + high) // 2
        cnt = 0
        for cable in cables:
            cnt += cable // mid
        if cnt >= n:
            low = mid + 1
        else:
            high = mid - 1
    return high

k, n = map(int, input().split())
cables = [int(input()) for _ in range(k)]
print(binary_search(cables, n))