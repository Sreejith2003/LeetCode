def findValidPair(s):
    s = list(s)

    lst = []
    for x in s:
        lst.append(int(x))
    print(lst)

    l = 0
    for r in range(1, len(lst)):
        if lst[l] + 1 == lst[r]:
            return f"{lst[l]}{lst[r]}"
        else:
            continue

s = "2523533"
print(findValidPair(s))