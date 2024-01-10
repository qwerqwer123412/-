import sys

sys.setrecursionlimit(int(1e6))

# 구해야 하는 것
# 1. root node -> 기가 노드 거리
# 2. 기가 노드 좌표
# root에서 기가로 갈때 종료 조건을 어떻게? 자식이 2개인 경우..
# but tree배열 에서는 실제 자식이 1개라도 2개이상 저장이 될 수 있다
# 어떻게 판단할 것인가? ==> visited배열 => 왔던 곳이면(visited에 있으면) 내 자식이 아니다 (사실 부모 였던 거임)
# 그래서 visited에 있는 거 싹다 쳐내고 한개만 있으면 자식이 1개이구나 판단이 가능하다

# 3. 기가노드 -> leaf 노드까지의 거리 구하기
# 만약 자식 노드가 없다면 leaf node ==> 이걸로 거리 구하면 되겠네

# tree는 그냥 재귀를 얼마나 잘 구현하는지가 중요
# 추가로 재귀 문제는 bakctracking 즉, bound function을 잘 구하는 것도 중요
# 이 경우에 visited는 자식 개수 결정하는데 쓰이기도 하지만, 왔던 곳을 또 방문 안하게 해주는 bound function 역할을 하기도 한다

n, r = map(int, sys.stdin.readline().strip().split())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, d = map(int, sys.stdin.readline().strip().split())
    tree[a].append([b, d])
    tree[b].append([a, d])

giga = 0

visited = set()


# 기가 노드를 찾기 + 기가 노드 까지 가는 cost 구해주는 함수
def find_giga_node(node, cost=0):
    # 다음으로 갈 수 있는 노드의 수를 결정 ==> 종료 조건을 위해서
    count = 0
    # 다음으로 갈 노드를 결정
    next = [0, 0]
    for a, b in tree[node]:
        # 갈 수 있는 경우
        if a not in visited:
            count = count + 1
            next = [a, b]
    # 갈 수 있는 노드가 2개 이상 이거나, 더 이상 갈 수 없는 경우-> leaf node인 경우
    # 종료 조건 ==> 이것이 기가 노드가 된다
    if count > 1 or count == 0:
        global giga
        giga = node
        return cost
    visited.add(next[0])
    return find_giga_node(next[0], cost + next[1])


visited.add(r)
answer1 = find_giga_node(r)

answer2 = 0


# 기가 노드 -> leaf 노드 까지 거리의 최대 값을 구하기
def search(node, cost=0):
    # leaf node 판단을 위한 변수
    count = 0
    for a, b in tree[node]:
        # 이동할 곳이 있는 경우..
        if a not in visited:
            # visited에 넣어줘야 bound가 잘 돼서 연산량이 줄어든다
            visited.add(a)
            count += 1
            search(a, cost + b)
    # leaf node 인 경우
    if not count:
        global answer2
        answer2 = max(answer2, cost)
        return


search(giga)

print(answer1, answer2)
