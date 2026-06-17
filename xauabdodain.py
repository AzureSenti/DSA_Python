def sinhab(xau,n):
    if len(xau) == n:
        print(xau, end=" ")
    else:
        sinhab(xau[:] + "A", n)
        sinhab(xau[:] + "B", n)

for _ in range(int(input())):
    N = int(input())
    sinhab("", N)
    print()
