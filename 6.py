N = int(input())
listahan = input().split()
diks = {"pos": 0, "neg": 0, "zer": 0}
for i in listahan:
    if int(i) > 0:
        diks["pos"] += 1
    elif int(i) < 0:
        diks["neg"] += 1
    else:
        diks["zer"] += 1     
print(format(diks["pos"]/N, '.3f'))
print(format(diks["neg"]/N, '.3f'))
print(format(diks["zer"]/N, '.3f'))