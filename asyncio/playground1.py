
import asyncio

async def getData(id: str):
    print(f"Getting data for user {id}")
    await asyncio.sleep(5)
    return {"user": id, "info": f"data for user {id}"}

async def main():
    """ blocking """
    task1 = getData("1")
    task2 = getData("2")
    res1 = await task1
    res2 = await task2
    print(res1)
    print(res2)

asyncio.run(main())