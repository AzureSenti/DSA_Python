import itertools

def combinations(n, k):
    arr = range(1, n + 1)
    return list(itertools.combinations(arr, k))

for _ in range(int(input())):
    N, K = map(int, input().split())
    danh_sach_to_hop = combinations(N, K)
    for to_hop in danh_sach_to_hop:
        print("".join(map(str, to_hop)) , end=" ")
    print()