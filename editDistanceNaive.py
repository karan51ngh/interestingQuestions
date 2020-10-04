def dell(w1):  # deleting from w2
    if w1 == "":
        return ""
    else:
        return w1[:-1]


def inss(w1, w2):  # inserting into w1
    if w2 == "":
        return w1
    else:
        return w1+w2[-1]


def last_ele(a):  # returns the last element
    if a == "":
        return a
    else:
        return a[-1]


def edit(w1, w2):
    if w1 == "" and w2 == "":
        return 0
    else:
        if last_ele(w1) == last_ele(w2):
            return edit(w1[:-1], w2[:-1])
        else:
            if w1 == "":        # infinite case 1
                return 1+edit(inss(w1, w2), w2)
            elif w2 == "":      # infinite case 2
                return 1+edit(dell(w1), w2)
            else:               # base case
                return 1+min(edit(dell(w1), w2), edit(inss(w1, w2), w2))


word1 = input()
word2 = input()
print(edit(word1, word2))
