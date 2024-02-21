import math
import sys
from collections import defaultdict

n = int(sys.stdin.readline().strip())
graph = defaultdict(list)
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)

d, g = 0, 0

def solveG(current):
    global g
    g += math.comb(len(graph[current]), 3)

def solveD(a, b):
    length_a = len(graph[a]) - 1
    length_b = len(graph[b]) - 1
    global d
    d = d + length_a * length_b if length_b > 0 and length_a > 0 else d


for i in range(1, n + 1):
    solveG(i)
    for j in graph[i]:
        if i <= j:
            continue
        solveD(i, j)
if g * 3 > d:
    print("G")
elif g * 3 < d:
    print("D")
else:
    print("DUDUDUNGA")