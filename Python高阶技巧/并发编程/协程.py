"""
    同步  不同程序单元为了完成某个任务,在执行过程中需靠某种通信方式以协调一致，我们称这些程序单元是同步执行的  比如：购物系统中更新商品库存,用行锁作为通信信号
    异步  不同程序单元之间过程中无需通信协调，也能完成任务的方式，不相关的程序单元之间可以是异步的	比如：爬虫

    1.含义
    协程(Coroutine)是一种用户态的轻量级线程，在单线程内实现并发

    2.特点
    拥有自己的寄存器上下文
    协程本质上是单线程
    3.协程与线程比较
    1.由于GIL锁的存在,多线程的运行需要频繁的加锁解锁,切换线程,这极大地降低了并发性能,

    2.协程本质上是单线程,无需线程上下文切换开销,无需原子操作,

    3.协程调度切换时,将寄存器上下文和栈保存到其他地方,在切回来的时候,恢复先前的寄存器上下文和栈,极大的提高了并发性能
"""
import asyncio
import aiohttp  # requests不支持asyncio异步，只能用这个aiohttp


async def async_craw(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            result = await resp.text()
            print(url, len(result))

# 获取事件循环
loop = asyncio.get_event_loop()

tasks = [
    loop.create_task(async_craw(url))
    for url in ['url信息']
]

loop.run_until_complete(asyncio.wait(tasks))

"""
    信号量：是一个同步对象，用于保持在0至指定最大值之间的一个计数值,可以用来控制并发度
"""
sem = asyncio.Semaphore(10)

async with sem:
    pass

