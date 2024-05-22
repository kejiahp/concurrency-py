import asyncio

async def getData(id: str):
    print(f"Getting data for user {id}")
    await asyncio.sleep(5)
    if id == "2":
        raise Exception("Custom Error")
    return {"user": id, "info": f"data for user {id}"}

async def main():
    """ tasks allow running of co-routines in a non-blocking manner """
    task1 = asyncio.create_task(getData("1"))
    task2 = asyncio.create_task(getData("2"))
    res1 = await task1
    res2 = await task2
    print(res1)
    print(res2)

async def gather():
    tasks = await asyncio.gather(getData("1"), getData("2"), return_exceptions=True)
    print(tasks)

async def set_future_result(future, result: str):
    await asyncio.sleep(5)
    future.set_result(result)

async def make_shift_future():
    """
    A future is basically a promise of a future result, 
    could be an error or an actual result.

    We are waiting for a value of the execution of the coroutine
    
    you can also use: (asyncio.Future()) to create a future 
    """
    loop = asyncio.get_event_loop()
    future = loop.create_future()

    asyncio.create_task(set_future_result(future, "The future was successful"))
    result = await future
    print(f"Received future result: {result}")

asyncio.run(make_shift_future())