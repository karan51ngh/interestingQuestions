# bag contains the weights.
# Pro cotains Profits.

def maxi(w, n):
    P = []
    M = []

    for i in range(w+1):
        M.append(0)

    for i in range(n+1):
        P.append(M.copy())

    bag.insert(0, 0)     # weights
    Pro = bag.copy()        # profits

    for i in range(n+1):
        for j in range(w+1):

            if i == 0 or j == 0:
                P[i][j] = 0
                continue

            elif bag[i] > j:
                P[i][j] = P[i-1][j]
                continue

            else:
                P[i][j] = max(P[i-1][j-bag[i]] + Pro[i], P[i-1][j])
                continue

    return P[n][w]


w, n = list(map(int, input().split()))
bag = list(map(int, input().split()))
bag.sort()
print(maxi(w, n))
