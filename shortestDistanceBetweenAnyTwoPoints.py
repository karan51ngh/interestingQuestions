def func(a):                # returns x cood
    return(a[0])


def dist(a, b):             # returns distance between points
    X2 = (a[0]-b[0])**2
    Y2 = (a[1]-b[1])**2
    return (X2+Y2)**0.5


def ldist(a, x):
    return ((a[0]-x)**2)**0.5


def mind2(a1, a2, n1, n2):             # semi naive function for the strip case
    md = dist(a1[0], a2[0])
    for i in range(n1):
        for j in range(n2):
            d = dist(a1[i], a2[j])
            if d < md:
                md = d
    return md


def mind(a, n):  # minimum dist
    if n == 2:
        return(dist(a[0], a[1]))
    if n == 3:
        return(min(dist(a[0], a[1]), dist(a[0], a[2]), dist(a[1], a[2])))
    else:
        x = (a[n//2 - 1][0]+a[n//2][0])/2  # divider line
        a1 = a[0:n//2]                     # set of points left of x
        a2 = a[n//2:n]                     # set of points right of x
        d1 = mind(a1, n//2)  # smallest dist in a1
        d2 = mind(a2, (n-n//2))  # smallest dist in a2
        d = min(d1, d2)                    # min dist
        a3 = list()  # 3rd set
        a4 = list()  # 4th set
        i = 0
        while(ldist(a2[i], x) < d):
            a3.append(a2[i])
            i += 1
            if i == (n-n//2):
                break
        if a3 != []:
            i = n//2-1
            while(ldist(a1[i], x) < d):
                a4.append(a1[i])
                i -= 1
                if i == 0:
                    break
            a3.sort(key=func)
            a4.sort(key=func)
            d3 = mind2(a3, a4, len(a3), len(a4))
            if d3 > d:
                return d
            else:
                return d3
        else:
            return d


arr = list()
n = int(input())
for i in range(n):
    i, j = list(map(int, input().split()))
    arr.append([i, j])
arr.sort(key=func)          # sorted the list of lists(points)
ans = mind(arr, n)
print(ans)
