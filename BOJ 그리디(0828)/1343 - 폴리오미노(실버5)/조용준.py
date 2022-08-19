board = input().split('.')
res = []

for i in board:
    len_i = len(i)
    if len_i % 2 != 0:
        print(-1)
        break
    while len_i >= 4:
        res.append('AAAA')
        len_i -= 4
    if len_i == 2:
        res.append('BB')
        len_i -= 2 
    res.append('.')
else:
    print(''.join(res)[:-1])

# replace()를 활용한 참신한 풀이
board = input()

board = board.replace("XXXX", "AAAA")
board = board.replace("XX", "BB")

if 'X' in board:
    print(-1)    
else:
    print(board)