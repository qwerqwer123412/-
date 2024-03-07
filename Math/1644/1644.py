import math
import sys

n = int(sys.stdin.readline().strip())

# 에라토스테네스의 체를 사용하기 위한 배열
# 특정 구간의 소수를 구할 때는 에라토스를 사용하는게 효율적
prime_check = [True] * (n + 1)

for i in range(2, int(math.sqrt(n)) + 1):
    # 소수 아닌 놈들 쳐내기(자기 자신은 지우면 안된다..)
    for j in range(i * 2, n + 1, i):
        prime_check[j] = False

# 소수를 저장하기 위한 리스트
prime_num = []

for i in range(2, n + 1):
    if prime_check[i]:
        prime_num.append(i)

left, right = 0, 1
answer = 0

# 투 포인터
# 크면 right++
# 작으면 left++
while left < right <= len(prime_num):

    s = sum(prime_num[left:right])
    if s < n:
        right += 1
    else:
        if s == n:
            answer += 1
        left += 1
print(answer)
