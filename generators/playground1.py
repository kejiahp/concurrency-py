from typing import Iterator

class Range:
    """ custom iterator """
    def __init__(self, stop: int) -> None:
        self.start = 0
        self.stop = stop

    def __iter__(self) -> Iterator[int]:
        curr = self.start
        while curr < self.stop:
            yield curr
            curr += 1

# gen = Range(10)
# list = list(gen) iteable to list
# gen = (i for i in list) list to comprehnsion generator

def randoGen():
    result = yield 1 # returns the 1 but stops here. `gen.send("Daddy")` provides a value to the generator, stores that in result then continues execution
    return result

gen = randoGen()
print(next(gen))
gen.send("Daddy")

# gen.close() # special exception to clear generator state(end it)
# gen.throw(ValueError()) # throw exception within generator

def randoGen2():
    result = yield 1 # returns the 1 but stops here. `gen.send("Daddy")` provides a value to the generator, stores that in result then continues execution
    
    return result # return value stored in the StopIteration exception


gen1 = randoGen2()
gen1.send(None)
try:
    gen1.send("Stop right there")
except StopIteration as exc:
    print(exc.value)
