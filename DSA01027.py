import itertools

N = int(input())
A = list(map(int, input().split()))


hoan_vi = list(itertools.permutations(sorted(A)))
for h in hoan_vi:
    print(*h)