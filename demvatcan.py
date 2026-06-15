lien_ke = [(-1, 0), (1, 0), (0, -1), (0, 1)]

N,M = map(int, input().split())
me_cung = []
so_vat_can = 0
for _ in range(N):
    me_cung.append(list(input()))

for i in range(N):
    for j in range(M):
        if me_cung[i][j] == '#':
            me_cung[i][j] = '.'
            so_vat_can += 1

            hang_doi = []
            hang_doi.append((i, j))

            while hang_doi:
                x, y = hang_doi.pop(0)
                for dx, dy in lien_ke:
                    x_moi = x + dx
                    y_moi = y + dy

                    if 0 <= x_moi < N and 0 <= y_moi < N and me_cung[x_moi][y_moi] == '#':
                        me_cung[x_moi][y_moi] = '.'
                        hang_doi.append((x_moi, y_moi))

print(f"{so_vat_can}")
