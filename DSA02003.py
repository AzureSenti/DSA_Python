for _ in range(int(input())):
    N = int(input())
    me_cung = []


    duong_di = []

    def check(duong, x, y):
        if len(duong) == (N-1)*2:
            duong_di.append(duong[:])
            return

        if x < N - 1 and me_cung[x + 1][y]:
            check(duong + 'D', x+1, y)

        if y < N - 1 and me_cung[x][y + 1]:
            check(duong + "R", x, y+1)



    for _ in range(N):
        me_cung.append(list(map(int, input().split())))


    if me_cung[0][0] == 0:
        print(-1)
        continue

    check("", 0, 0)

    if len(duong_di) == 0:
        print(-1)
    else:
        for duong in duong_di:
            print(duong, end=" ")
        print()

