"""
    线程的生命周期：新建-就绪-运行-阻塞-终止
    线程池-ThreadPoolExecutor：线程的新建和终止都要消耗系统资源，所以提前建好一些线程，并且对这些线程进行复用来减少系统消耗
    使用场景：适合处理突发性大量请求或需要大量线程完成任务、但实际任务处理时间较短

"""
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
# # 线程池中创建100个线程
# pool = ThreadPoolExecutor(100)
# # 给线程池添加任务
# pool.submit('任务函数名', '参数1', '参数2'....)

with concurrent.futures.ThreadPoolExecutor() as pool:
    pass


