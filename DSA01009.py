def check_xau_hop_le(xau, k):
    chuoi_A_can_tim = "A" * k
    danh_sach_cum_A = xau.split("B")

    return danh_sach_cum_A.count(chuoi_A_can_tim) == 1

def solve():
    N, K = map(int, input().split())

    ket_qua = []

    def sinh_xau(xau_tam):
        if len(xau_tam) == N:
            if check_xau_hop_le(xau_tam, K):
                ket_qua.append(xau_tam)
            return

        sinh_xau(xau_tam + "A")
        sinh_xau(xau_tam + "B")

    sinh_xau("")

    print(len(ket_qua))
    for xau in ket_qua:
        print(xau)


if __name__ == '__main__':
    solve()




