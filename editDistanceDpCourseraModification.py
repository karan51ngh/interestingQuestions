def edit(w1, w2):
    mtx = list()  # initializing matrix
    for i in range(len(w1)+1):
        a = []
        for j in range(len(w2)+1):
            if i == 0:
                a.append(j)
            elif j == 0:
                a.append(i)
            else:
                a.append(0)
        mtx.append(a)
    if w1 == "":
        return len(w2)
    elif w2 == "":
        return len(w1)
    else:
        w3 = " "+w1
        w4 = " "+w2
        for i in range(1, len(w1)+1):
            for j in range(1, len(w2)+1):
                inser = mtx[i][j-1]+1
                dele = mtx[i-1][j]+1
                match = mtx[i-1][j-1]
                mismatch = mtx[i-1][j-1]+1
                if w3[i] == w4[j]:
                    mtx[i][j] = min(inser, dele, match)
                else:
                    mtx[i][j] = mtx[i][j] = min(inser, dele, mismatch)

    return mtx[i][j]


word1 = input()
word2 = input()
print(edit(word1, word2))
