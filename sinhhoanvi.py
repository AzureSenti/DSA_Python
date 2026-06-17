import itertools


def sinhhoanvi(n):
    return list(itertools.permutations(range(1,n+1)))

for _ in range(int(input())):
    n = int(input())
    hoan_vi = sinhhoanvi(n)
    kequa = ""
    for i in hoan_vi:
        kequa += "".join(map(str, i)) + " "

    print(kequa.strip())