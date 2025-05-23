def intersection(l1, l2):
    l3 = list()
    for v in l1:
        if v in l2:
            l3.append(v)
    return l3


def inters(l1, l2):
    s1 = set(l1)
    s2 = set(l2)
    return list(s1 & s2)  # return list(s1.intersection(s2))


l1 = [45, 5, 22, 31, 7, 19]
l2 = [2, 1, 5, 22, 7, 38, 27, 19, 13, 41]
print(intersection(l1, l2))
print(inters(l1, l2))