import sys 
# k : 이미 가지고 있는 랜선의 개수 
# n : 필요한 랜선의 개수
k, n = map(int, sys.stdin.readline().split())
array = []
for i in range(k):
    array.append(int(input()))

start = 1
end = max(array)

while (start <= end):
    mid = (start + end) // 2
    cnt = 0 

    for i in array:
        cnt += i// mid

    if cnt >= n:
        start = mid + 1 # 길이를 더 길게 
    else: 
        end = mid - 1 # 길이를 더 짧게 

print(end)