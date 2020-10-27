def print_map(function, iterable)
    while True
        try
            print(function(next(iterable)))
        except StopIteration
            break


def test_f1(x)
    return x  2


a = [1, 23, 4, 5]
print_map(test_f1, iter(a))