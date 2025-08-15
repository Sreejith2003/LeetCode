def uppercase(s):
    lst = list(s)
    print(lst)
    for i in range(0, len(lst)):
        if lst[0] is lst[0].lower:
            lst[0] = lst[0].upper()
    return "".join(lst)
s =  "gEEKs"
res = uppercase(s)
print(res)