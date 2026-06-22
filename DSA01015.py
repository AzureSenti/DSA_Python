from collections import deque

kiem_tra = ["9"]

for i in range(1, 500):
    hang_doi = deque()
    hang_doi.append("9")

    while hang_doi:
        hien_tai = hang_doi.popleft()
        if int(hien_tai) % i == 0:
            kiem_tra.append(hien_tai)
            break
        hang_doi.append(hien_tai + "0")
        hang_doi.append(hien_tai + "9")

for _ in range(int(input())):
    N = int(input())
    print(kiem_tra[N])

