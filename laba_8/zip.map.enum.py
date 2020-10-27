def my_map(function, iterable):
    while True:
        try:
            yield function(next(iterable))
        except StopIteration:
            break


def my_zip(*args):
    iters = list(my_map(iter, iter(args)))
    m = min(my_map(len, iter(args)))
    for i in range(m):
        yield tuple(my_map(next, iter(iters)))


def my_enumerate(iterable, start=0):
    while True:
        try:
            yield start, next(iterable)
            start += 1
        except StopIteration:
            break


print(*my_zip([1, 2, 3], ['a', 'b', 'c']))
print(*my_enumerate(iter([1, 2, 3, 4, 5]), 5))