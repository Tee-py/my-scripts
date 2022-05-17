import asyncio
import time



async def f1():
    res = 0
    for i in range(200):
        res += i
    return res

async def main():
    res = await f1()
    print(res)


print("Started")

print('Ended')
