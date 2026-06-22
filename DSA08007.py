for _ in range(int(input())):
    n = list(input())
    for i in range(len(n)):
        if int(n[i]) > 1:
            n[i:] = "1"*(len(n) - i)

    print(int("".join(n), 2))
