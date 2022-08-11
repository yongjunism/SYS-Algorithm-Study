import sys
input = sys.stdin.readline

n = int(input())
people = [-1] + list(map(int, input().split()))
line = []

for i in range(n, 0, -1):
    line.insert(people[i], i)
    print(line)
print(*line)