import sys
from itertools import combinations

n, m, k = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

temp = [(i, j) for i in range(n) for j in range(m)]
cases = list(combinations(temp, k))
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def check(case):
    for i in range(len(case)):
        x, y = case[i][0], case[i][1]

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if (nx, ny) in case:
                return False
    return True


answer = -sys.maxsize
for case in cases:
    if check(case):
        result = [board[x][y] for x, y in case]
        answer = max(answer, sum(result))
print(answer)
