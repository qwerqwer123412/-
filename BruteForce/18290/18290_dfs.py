import sys
from itertools import combinations

n, m, k = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

temp = [(i, j) for i in range(n) for j in range(m)]
cases = list(combinations(temp, k))
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
visited = [[False] * m for _ in range(n)]

answer = -sys.maxsize


def dfs(x, y, result=0, depth=0):
    global answer
    if depth == k:
        answer = max(answer, result)
        return
    for i in range(x, n):
        for j in range(y if x == i else 0, m):
            if visited[i][j]:
                continue
            flag = True
            # 인접 확인하는 ..
            for a in range(4):
                nx, ny = i + dx[a], j + dy[a]
                if (0 <= nx < n and 0 <= ny < m):
                    if visited[nx][ny]:
                        flag = False
            if flag:
                visited[i][j] = True
                dfs(i, j, result + board[i][j], depth + 1)
                visited[i][j] = False


dfs(0, 0)
print(answer)