import sys

n = int(sys.stdin.readline().strip())

datas = [list(sys.stdin.readline().strip().split())[1:] for _ in range(n)]
datas.sort()

visited = set()
for data in datas:
    temp = []
    for i in range(len(data)):
        temp.append(data[i])
        if tuple(temp) in visited:
            continue
        else:
            result = "--" * (i) + data[i]
            print(result)
            visited.add(tuple(temp))
