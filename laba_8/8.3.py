from itertools import combinations


def get_combinations(s, n):
    res = list()
    for i in range(n):
        res += map(''.join, (combinations(sorted(s), i + 1)))
    return res


print(get_combinations("cat", 2))