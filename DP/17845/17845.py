import sys

n, k = map(int, sys.stdin.readline().strip().split())

# optimal값을 저장하는 dp배열
dp = [0] * (10001)

# 연산 횟수는  k * 10000번 연산 ==> maximum이 1000만번
for _ in range(k):
    a, b = map(int, sys.stdin.readline().strip().split())

    # result배열은 중복 선택을 피하기 위해서 별도로 만들었다.
    result = []
    for i in range(10001):
        # update해야할 값을 result에 담는다
        if i + b <= n:
            if dp[i + b] < dp[i] + a:
                result.append((i + b, dp[i] + a))
        else:
            break
    # result에 담긴 값을 dp배열에 반영
    # 이렇게해서 중복 선택을 막을 수 있다
    for x, y in result:
        dp[x] = y

print(dp[n])
