import sys
from collections import defaultdict
from itertools import combinations

# 브루트 포스로 풀이가 가능한가?
# yes!
# 1.바둑알을 놓을 수 있는 모든 경우의 수: combination(400, 2)==> 모든 경우 == O(N^2)
# 2. 그룹나누기==> 많아야 O(N)복잡도 ==> 400번
# 3. 그룹에 인접한 빈칸이 있는가 확인하는 로직 ==> N * 4 ==> O(N)
# 따라서  O(N^2) 이므로.. brute force 풀이는 문제없는 풀이

n, m = map(int, sys.stdin.readline().strip().split())
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# 모든 경우의 수를 구하는 로직
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
temp = [(i, j) for i in range(n) for j in range(m) if board[i][j] == 0]
cases = list(combinations(temp, 2))



# 흰 바둑 돌의 그룹 나누기
white = [[0] * m for _ in range(n)]
# 흰 바둑 돌의 그룹별 좌표 ==> 그룹 나누기 결과를 저장하는 곳
white_group = defaultdict(list)


# 그룹 나누기 ==> by dfs
def dfs(x, y, group_num):
    white_group[group_num].append((x, y))
    visited[x][y] = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        # 방문을 했거나, 범위를 벗어나면 pass
        if (not (0 <= nx < n and 0 <= ny < m)) or visited[nx][ny]:
            continue
        if board[nx][ny] == 2:
            dfs(nx, ny, group_num)


visited = [[False] * m for _ in range(n)]
count = 1
for i in range(n):
    for j in range(m):
        if board[i][j] == 2 and not visited[i][j]:
            dfs(i, j, count)
            count += 1




# 흰색 바둑 알이 탈출 가능한가를 확인하는 함수
# 인접한 빈칸이 있으면 False, 아니면 True를 return
def check(group_num):
    for x, y in group_num:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 범위를 벗어나는 경우
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            # 인접한 곳에 빈칸이 있다..
            # 종료..
            if board[nx][ny] == 0:
                return False

    return True


answer = 0
for case in cases:
    # 검은 바둑알 두기
    for x, y in case:
        board[x][y] = 1
    result = 0
    # 흰색 바둑 알이 몇개 먹히는지 확인하는 로직
    for g_num in white_group:
        if check(white_group[g_num]):
            result += len(white_group[g_num])
    answer = max(result, answer)
    # 검은 바둑알 압수
    for x, y in case:
        board[x][y] = 0

print(answer)
