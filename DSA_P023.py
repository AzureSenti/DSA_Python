import itertools

maxnum = 200000
nguyen_to = [1 for _ in range(maxnum)]

for i in range(2, maxnum):
    if nguyen_to[i]:
        for j in range(2*i, maxnum, i):
            nguyen_to[j] = 0

N, K = map(int, input().split())
to_hop = list(itertools.combinations(range(1, N + 1), K))

for i in range(2, len(to_hop)):
    if nguyen_to[i]:
        print(f"{i}: {' '.join(map(str, to_hop[i-1]))}")