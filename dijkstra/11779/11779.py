import sys
from collections import defaultdict
import heapq

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
graph = defaultdict(list)

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    graph[a].append((b, c))

start, end = map(int, sys.stdin.readline().strip().split())


def dijkstra(start, end):
    """
    :param start:시작점
    :param end: 목적지
    :return:
    """

    pq = []
    # 거리, 직전 node
    distance = [[sys.maxsize, 0] for _ in range(n + 1)]
    distance[start] = [0, start]
    heapq.heappush(pq, (0, start))

    while pq:
        dist, node = heapq.heappop(pq)
        if distance[node][0] < dist:
            continue
        for next_node, next_cost in graph[node]:
            if distance[next_node][0] > dist + next_cost:
                distance[next_node] = [dist + next_cost, node]
                heapq.heappush(pq, (distance[next_node][0], next_node))
    result = find_route(distance, end, start)
    print(distance[end][0])
    print(len(result))
    print(*result)


def find_route(distance, end, start):
    """

    :param distance: dijkstra에서 사용한 distance
    :param end:
    :param start:
    :return:
    """
    result = [end]
    cur = end
    while cur != start:
        result.append(distance[cur][1])
        cur = distance[cur][1]
    result = result[::-1]
    return result


dijkstra(start, end)
