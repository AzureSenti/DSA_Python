def doi_trang_thai(n):
    if n == "0":
        return "1"
    return "0"

for _ in range(int(input())):
    n = int(input())
    danh_sach = ["0" * n]
    trang_thai = "0" * n

    for _ in range(2 ** n - 1):
        for i in range(n):
            if trang_thai[i] == "0":
                trang_thai = "0" * i + "1" + trang_thai[i+1:]
                danh_sach.append(danh_sach[-1][:i] + doi_trang_thai(danh_sach[-1][i]) + danh_sach[-1][i+1:])
                break


    print(" ".join(chuoi[::-1] for chuoi in danh_sach))