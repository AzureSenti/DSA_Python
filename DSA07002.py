ngan_xep = []
for _ in range(int(input())):
    lenh = list(map(str, input().split()))
    if lenh[0] == "PUSH":
        ngan_xep.append(int(lenh[1]))
    elif lenh[0] == "POP":
        if len(ngan_xep) > 0:
            ngan_xep.pop()
    elif lenh[0] == "PRINT":
        if len(ngan_xep) > 0:
            print(ngan_xep[-1])
        else:
            print("NONE")