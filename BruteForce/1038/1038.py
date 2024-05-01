import sys
from collections import deque

N = int(sys.stdin.readline().strip())
count = 9
if N < 10:
    print(N)
    sys.exit()
q = deque()
for i in range(10):
    q.append(i)

while q:
    x = list(str(q.popleft()))
    for i in range(min(list(map(int, x)))):
        q.append(int("".join(x + [str(i)])))
        count += 1
        if count == N:
            print(q.pop())
            sys.exit()
print(-1)