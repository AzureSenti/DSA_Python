import itertools

N, K =  map(int, input().split())

tap_hop = sorted(list(set(map(int, input().split()))))

danh_sach_to_hop = list(itertools.combinations(tap_hop, K))

for to_hop in danh_sach_to_hop:
    print(*to_hop)