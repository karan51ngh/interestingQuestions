def money(n):
    mon = []
    for i in range(1000):
        mon.append(1000)
    mon[1] = 1
    mon[3] = 1
    mon[4] = 1
    for i in range(1, n+1):
        # print(f"i is {i}")
        x = i+1
        # print(f"x is {x}")
        y = i+3
        z = i+4

        if x <= n and mon[x] > mon[i]+1:
            # print("x <= n and mon[x] > mon[i]+1")
            mon[x] = mon[i]+1
        if y <= n and mon[y] > mon[i]+1:
            mon[y] = mon[i]+1
        if z <= n and mon[z] > mon[i]+1:
            mon[z] = mon[i]+1
    return mon[n]


m = int(input())
print(money(m))
