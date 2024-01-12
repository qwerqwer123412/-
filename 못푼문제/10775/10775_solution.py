import sys

G = int(sys.stdin.readline().strip())

P = int(sys.stdin.readline().strip())
parent = [i for i in range(G + 1)]
answer = 0
data = [int(sys.stdin.readline().strip()) for _ in range(P)]


def find_parent(x):
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]


def union(a, b):
    a, b = find_parent(a), find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


answer = 0

for i, plane in enumerate(data):
    x = find_parent(plane)
    if x <= 0:
        answer = i
        break
    union(x - 1, x)

print(answer)
