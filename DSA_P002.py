import itertools

N = int(input())

hoan_vi = list(itertools.permutations(range(1, N + 1)))

for i in range(len(hoan_vi)):
    print(f"{i+1}: " + " ".join(map(str, hoan_vi[i])))