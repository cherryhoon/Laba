from itertools import combinations_with_replacement


def get_combinations_with_r(s, n):
    return map(''.join, combinations_with_replacement(sorted(s), n))


print(*get_combinations_with_r("cat", 2))