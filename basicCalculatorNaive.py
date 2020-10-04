
def backtrack(n):
    if n == 1:
        return 0
    else:
        if n % 2 == 0 and n % 3 == 0:
            return 1+min(backtrack(n-1), backtrack(n//2), backtrack(n//3))
        elif n % 2 == 0:
            return 1+min(backtrack(n-1), backtrack(n//2))
        elif n % 3 == 0:
            return 1+min(backtrack(n-1), backtrack(n//3))
        else:
            return 1+backtrack(n-1)


n = int(input())
print(backtrack(n))
