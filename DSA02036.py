import itertools

for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    result = []
    for i in range(1, N+1):
        for to_hop in itertools.combinations(A, i):
            if sum(to_hop) % 2 == 1:
                result.append(to_hop)

    result.sort()
    for r in result:
        print(" ".join(map(str, r)))