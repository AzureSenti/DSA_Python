for _ in range(int(input())):
    N = int(input())
    a = list(map(int, input().split()))
    A = [a]

    while len(A[-1]) > 1:
        day_moi = []
        for i in range(1, len(A[-1])):
            day_moi.append(A[-1][i] + A[-1][i - 1])

        A.append(day_moi)

    for a_nho in A:
        print(f"[{' '.join(map(str, a_nho))}]")
