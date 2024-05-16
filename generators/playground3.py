from collections import deque

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

def quiet_worker(f):
    while True:
        w = worker(f)
        try:
            yield from w # the yield from allows us to pass/return value from/to generator from a generator. Kinda like a middle man generator, btwn the caller and worker in our example 
        except Exception as exc:
            print(f"ignoring {exc.__class__.__name__}")

w = quiet_worker(str)
next(w)
w.send([(1,),(2,),(3,),(4,),(5,)])
print(next(w))
print(next(w))
print(next(w))
print(next(w))
print(next(w))
print(next(w))