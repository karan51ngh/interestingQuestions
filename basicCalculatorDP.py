# to print all instances
def cal(n):
    mon = []
    for i in range(n+1):
        mon.append(1000)
    mon[1] = 0
    for i in range(1, n+1):
        # print(f"i is {i}")
        x = i+1
        # print(f"x is {x}")
        y = i*2
        z = i*3

        if x <= n and mon[x] > mon[i]+1:
            # print("x <= n and mon[x] > mon[i]+1")
            mon[x] = mon[i]+1
        if y <= n and mon[y] > mon[i]+1:
            mon[y] = mon[i]+1
        if z <= n and mon[z] > mon[i]+1:
            mon[z] = mon[i]+1
    print(mon[n])
    ans = []
    t = n
    while t >= 1:
        ans.append(t)
        if t == 1:
            break
        if mon[t-1] == mon[t]-1:
            t = t-1
        elif t % 2 == 0 and mon[t//2] == mon[t]-1:
            t = t//2
        elif t % 3 == 0 and mon[t//3] == mon[t]-1:
            t = t//3
    # print(ans)
    ans.reverse()
    for i in range(0, len(ans)):
        print(ans[i], end=" ")


n = int(input())
cal(n)
