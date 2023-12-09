def find_occurrences(ms, ss):
    indi = []
    si = 0

    while True:
        ind = ms.find(ss, si)
        if ind == -1:
            break
        indi.append(ind)
        si = ind + 1

    return indi if indi else -1


m=input(print("enter the main string"))
n= input("enter the substring")
result = find_occurrences(m, n)
print(result)
