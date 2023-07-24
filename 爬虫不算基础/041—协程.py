import asyncio


async def exeute(x):
    print('number:', x)


coroutine = exeute(1)
print('Coroutine', coroutine)
print('after')

loop = asyncio.get_event_loop()
task=loop.create_task(coroutine)
print('task',task)

loop.run_until_complete(task)
print('task',task)

print('after calling loop')
