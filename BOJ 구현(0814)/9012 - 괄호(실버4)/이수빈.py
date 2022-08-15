import sys
t = int(input())
ps = []
for _ in range(t):
    ps.append(sys.stdin.readline().rstrip())

for arr in ps:
    lst = []
    for j in arr:
        if j == '(':
            lst.append(j)
        elif j == ')':
            if lst:     #  '(' 있는 경우 
                lst.pop()
            else:       # ')' 없는 경우
                print("NO")
                break

    else: # break 문으로 끊기지 않고 수행됬을경우 수행
        if not lst:
            print('YES')
        else:
            print('NO')