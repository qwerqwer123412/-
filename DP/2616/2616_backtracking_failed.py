import sys

# 실패한 풀이.. 최악의 경우 25억번 연산이 이루어 지지만,
# bound되는 값이 많다면 풀리지 않을까해서  혹시나 했는데.. 역시나 안된다..


sys.setrecursionlimit(int(1e8))
n = int(sys.stdin.readline().strip())
data = list(map(int, sys.stdin.readline().strip().split()))
couch_count = int(sys.stdin.readline().strip())

# backtracking을 실행한 결과의 max값을 저장할 변수
answer = 0


def backtrack(couch_num, index, result):
    global answer, couch_count
    # 범위를 벗어나는 경우.. + 소형 기관차를 3개다 사용한 경우...
    if index >= n or couch_num >= 3:
        answer = max(answer, result)
        return

    # bound function 1
    if n - index < (3 - couch_num) * couch_count:
        return
    # bound function 2
    if result + sum(data[index:]) < answer:
        return
    for start in range(index, n):
        temp = 0
        for i in range(couch_count):
            # 범위 안에 있는 경우..
            if start + i < n:
                temp += data[start + i]
            else:
                break
        backtrack(couch_num + 1, start + couch_count, result + temp)


for i in range(n):
    backtrack(0, i, 0)
print(answer)
