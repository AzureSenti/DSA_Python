nhap = input()

nua_trai =[]
nua_phai = []

for chu in nhap:
    if chu == "<":
        if nua_trai:
            nua_phai.append(nua_trai.pop())
    elif chu == ">":
        if nua_phai:
            nua_trai.append(nua_phai.pop())
    elif chu == "-":
        if nua_trai:
            nua_trai.pop()
    else:
        nua_trai.append(chu)


print("".join(nua_trai + nua_phai[::-1]))
