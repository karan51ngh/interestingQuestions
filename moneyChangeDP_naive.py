def money(n):
    if n == 0:
        return 0
    else:
        if n >= 4:
            return 1+min(money(n-1), money(n-3), money(n-4))
        elif n >= 3:
            return 1+min(money(n-1), money(n-3))
        else:
            return 1+money(n-1)


m = int(input())
print(money(m))
