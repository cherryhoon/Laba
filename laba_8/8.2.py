from itertools import permutations


def get_permutations(a, b):
    return map(''.join, permutations(sorted(a), b))


print(*get_permutations("cat", 2))
