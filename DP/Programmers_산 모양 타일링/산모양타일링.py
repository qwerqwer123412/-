from collections import defaultdict


def solution(n, tops):
    # 가능한 모양을 저장
    dic = defaultdict(list)
    # 삼각형
    dic[0] = [0, 1, 2, 3]
    # 다이아몬드(마름모)
    dic[1] = [0, 1, 2, 3]
    # 평행사변형1(오른쪽)
    dic[2] = [0, 1, 2, 3]
    # 평행사변형1(왼쪽)
    dic[3] = [0, 1, 3]

    dp = [[0] * 4 for _ in range(n)]

    for i in range(4):
        dp[-1][i] = 1

    if not tops[-1]:
        dp[-1][1] = 0

    for i in range(n - 2, -1, -1):
        # 가능한 모양
        for j in range(4):
            if not tops[i] and j == 1:
                continue
            temp = 0
            for k in dic[j]:
                temp += (dp[i + 1][k] % 10007)
            dp[i][j] = temp

    return sum(dp[0]) % 10007
