import inspect

async def rando():
    print("YES")

print(inspect.isawaitable(rando()))