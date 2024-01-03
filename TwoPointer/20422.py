import sys

data = sys.stdin.readline().strip()
# 여기 까지 R이 몇개 있는지 확인하는 배열
# a~b 사이의 R이 몇 개 있는지 구하고 싶으면 r_count[b]-r_count[a]를 해주면 구해줄 수 있다.
r_count = [0] * len(data)
temp = 0
for i in range(len(data)):
    if data[i] == "R":
        temp += 1

    r_count[i] = temp
# 총 k개의 개수
k = len(data) - temp
# K의 left, right
left, right = 0, len(data) - 1
temp = 0
while left < len(data):
    if data[left] == "K":
        temp += 1
    # k//2이 되면 종료
    # 왼쪽 반, 오른쪽 반 노나 가지기
    if temp == k // 2:
        break
    left += 1

temp = 0
while right >= 0:

    if data[right] == "K":
        temp += 1

    if temp == k // 2:
        break
    right -= 1


# left 변수 한칸 줄여 주는 함수
# index 벗어나는 경우를 위해 맨 처음에 left -= 1 해줬음
def left_move(left):
    left -= 1
    while left >= 0:

        if data[left] == "K":
            return left
        left -= 1
    return -1


def right_move(right):
    right += 1
    while right < len(data):

        if data[right] == "K":
            return right
        right += 1
    return -1


# 최악의 경우는 K 싹다 처내는 경우 ==> only R만 있는 경우
answer = r_count[-1]
# K개수
k_count = k // 2
while k_count:
    if r_count[right] - r_count[left] != 0:
        answer = max(answer, k_count * 2 + r_count[right] - r_count[left])
    # k 한칸 줄이고 left, right 옮기기
    k_count -= 1
    left = left_move(left)
    right = right_move(right)

    # left, right 더 이상 옮길 수 없으면 종료
    if left == -1 or right == -1:
        break

print(answer)
