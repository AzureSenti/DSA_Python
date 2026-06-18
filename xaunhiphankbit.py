import itertools

def sinh_to_hop(n, k):
    arr = range(1, n + 1)
    return list(itertools.combinations(arr, k))

for _ in range(int(input())):
    N, K = map(int, input().split())
    to_hop = sinh_to_hop(N, K)
    for to in to_hop[::-1]:
        bit = [0] * N
        for i in to:
            bit[i - 1] = 1
        print("".join(map(str, bit)))

