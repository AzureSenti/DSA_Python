import itertools

N, K = map(int, input().split())
A = list(map(int, input().split()))

ket_qua = []

for i in range(1, N +1):
    for to_hop in itertools.combinations(A, i):
        if sum(to_hop) == K:
            ket_qua.append(to_hop)

ket_qua.sort(reverse=True)
for ket in ket_qua:
    print(" ".join(map(str, ket)))
print(len(ket_qua))