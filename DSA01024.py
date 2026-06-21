import itertools

N, K = map(int, input().split())
ten = list(set(map(str, input().split())))
ten.sort()


danh_sach_to_hop = list(itertools.combinations(ten, K))

for to_hop in danh_sach_to_hop:
    print(*to_hop)

