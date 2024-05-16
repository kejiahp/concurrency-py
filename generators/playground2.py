from collections import deque

def randoGen():
    yield 1

# generators a bi-directional they can take `gen.send()` they can give `yield`
# gen = randoGen()
# v = next(gen)
# print(v)


def worker(f):
    tasks = deque()
    value = None
    while True:
        batch = yield value
        value = None
        if batch is not None:
            tasks.extend(batch)
        else:
            if tasks:
                args = tasks.popleft()
                value = f(*args)

w = worker(str)
next(w)
w.send([(1,),(2,),(3,),(4,),(5,)])
print(next(w))
print(next(w))
print(next(w))
print(next(w))
print(next(w))
print(next(w))
