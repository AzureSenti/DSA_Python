def phat_loc(day, n):
    if len(day) == n:
        if day[-1] == '6':
            print(day)
        return

    if not day.endswith("666"):
        phat_loc(day + "6", n)

    if day[-1] != "8":
        phat_loc(day + "8", n)

N = int(input())
day = "8"

phat_loc(day, N)
