def move_zeros(l):
    zero_idx = 0
    for i in range(len(l)):
        n = l[i]
        if n != 0:
            l[zero_idx] = n
            if zero_idx != i:
                l[i] = 0
            zero_idx = zero_idx + 1
    return l


groups = ['HOT', 'Seventeen', 'Black Pink', 'NJZ']
# ratings = [1, 2, 4, 3, 100]
ratings = [1, 2, 4, 3]

l = [11, 0, 9, 0, -77]
move_zeros(l)
print(l)

# l = [11, 9, -77, 8]
# for i, v in enumerate(l):
#     print(i, v)

# l = [11, 9, -77, 8]
# for i in range(len(l)):
#     print(i, l[i])
group_rating = list(zip(groups, ratings))
print(group_rating)