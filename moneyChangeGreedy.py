def get_change(m):
    count = 0
    # write your code here
    while m > 0:
        if m >= 10:
            m = m - 10
            count = count + 1
            continue
        if m >= 5:
            m = m - 5
            count = count + 1
            continue
        if m >= 1:
            m = m - 1
            count = count + 1

    return count


if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
