for _ in range(int(input())):
    xau = list(input())
    for i in range(len(xau)-1, -1, -1):
        if xau[i] == "1":
            xau[i] = "0"
            break
        xau[i] = "1"

    print("".join(xau))