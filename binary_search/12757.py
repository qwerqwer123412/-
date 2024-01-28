import sys

n, m, k = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
board = sorted(board, key=lambda x: x[0])
# index, key
nearest = [[sys.maxsize, sys.maxsize]]


def find_nearest(left, right, data):
    if left > right:
        return
    mid = (left + right) // 2
    global nearest
    if abs(nearest[0][1] - data) > abs(board[mid][0] - data):
        nearest = [[mid, board[mid][0]]]
        # 중복 check
        if mid + 1 < len(board) and abs(data - board[mid + 1][0]) == abs(data - board[mid][0]):
            nearest.append([mid + 1, board[mid + 1][0]])
        if mid - 1 >= 0 and abs(data - board[mid - 1][0]) == abs(data - board[mid][0]):
            nearest.append([mid - 1, board[mid - 1][0]])

    if board[mid][0] - data > 0:
        find_nearest(left, mid - 1, data)
    else:
        find_nearest(mid + 1, right, data)


for _ in range(m):
    case = list(map(int, sys.stdin.readline().strip().split()))
    nearest = [[sys.maxsize, sys.maxsize]]
    find_nearest(0, len(board) - 1, case[1])
    index, key = nearest[0][0], nearest[0][1]

    if case[0] == 1:
        board.insert(index + 1, case[1:]) if key < case[1] else board.insert(index, case[1:])

    elif case[0] == 2:
        # 가까운게 2개 있거나, 없는 경우
        if len(nearest) != 1 or abs(key - case[1]) > k:
            continue
        board[index][1] = case[2]
    else:
        # 범위안 가까운게 없는 경우
        if abs(key - case[1]) > k:
            print(-1)
        elif len(nearest) >= 2:
            print("?")
        else:
            print(board[index][1])
