import sys

lines = sys.stdin.read().splitlines()

ngan_xep = []

for line in lines:
    if not line.strip():
        continue

    lenh = line.split()

    if lenh[0] == "push":
        ngan_xep.append(lenh[1])

    elif lenh[0] == "pop":
        if ngan_xep:
            ngan_xep.pop()

    elif lenh[0] == "show":
        if ngan_xep:
            print(" ".join(ngan_xep))
        else:
            print("empty")