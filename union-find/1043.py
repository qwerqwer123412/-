import copy
import sys

n, m = map(int, sys.stdin.readline().strip().split())
true_member = sys.stdin.readline().strip()

# -1 : 거짓을 들은 상태
# 0 : 이야기를 안 들은 상태
# 1 : 진실을 들은 상태
truth = [0] * (n + 1)
if true_member[0] != "0":
    true_member = list(map(int, true_member.split()))
    for i in true_member[1:]:
        truth[i] = 1

answer = 0

parties = [list(map(int, sys.stdin.readline().strip().split()))[1:] for _ in range(m)]


def dfs(index, truth, count):
    """
    이 함수는 dfs 탐색을 통해 거짓이야기를 들을 수 있는 max값을 찾으려고 하는 함수이다

    :param int index: 파티의 index
    :param list[int] truth: 위의 이야기를 들은 상태
    :param int count: 거짓 이야기를 들은 파티의 개수
    """

    # 종료 조건
    if index >= m:
        global answer
        answer = max(answer, count)
        return

    # 거짓 먼저 이야기 한 뒤, 참 이야기 하기
    for i in [-1, 1]:
        party = parties[index]
        flag = True
        for j in party:
            # 거짓 -> 참 or 참 -> 거짓
            if truth[j] == -i:
                flag = False
                break
        temp = []
        if flag:
            temp = copy.deepcopy(truth)
            for j in party:
                truth[j] = i
            if i == -1:
                dfs(index + 1, truth, count + 1)
            else:
                dfs(index + 1, truth, count)
            truth = temp


dfs(0, truth, 0)
print(answer)
