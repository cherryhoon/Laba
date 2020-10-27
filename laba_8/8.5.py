from itertools import groupby


def compress_string(s):
    return map(lambda a,: (len(list(a[1])), a[0]), groupby(s))


print(*compress_string("1222311"))