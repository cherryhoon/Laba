import numpy

class PrintАverage(Exception):
    pass

class PrintVariance(Exception):
    pass

class PrintCount(Exception):
    pass

def device_control_coroutine():
    collection = []
    try:
        while True:
            try:
                x = yield
                if x is not None:
                    collection.append(x)
            except PrintАverage:
                yield numpy.average(collection)
            except PrintVariance:
                yield numpy.var(collection)
            except PrintCount:
                yield len(collection)
    finally:
        print("Stop coroutine")


coroutine = device_control_coroutine()
next(coroutine)
for i in range(25):
    coroutine.send(i)
    if i%2 == 0:
        print("Average:", coroutine.throw(PrintАverage))
        next(coroutine)
    if i%3 == 0:
        print("Variance:", coroutine.throw(PrintVariance))
        next(coroutine)
    if i%5 == 0:
        print("Count:", coroutine.throw(PrintCount))
        next(coroutine)

print()
print("Average:", coroutine.throw(PrintАverage))
next(coroutine)
print("Variance:", coroutine.throw(PrintVariance))
next(coroutine)
print("Count:", coroutine.throw(PrintCount))

coroutine.close()