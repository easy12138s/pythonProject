"""
    线程的生命周期：新建-就绪-运行-阻塞-终止
    线程池-ThreadPoolExecutor：线程的新建和终止都要消耗系统资源，所以提前建好一些线程，并且对这些线程进行复用来减少系统消耗
    使用场景：适合处理突发性大量请求或需要大量线程完成任务、但实际任务处理时间较短


"""
import concurrent.futures

with concurrent.futures.ThreadPoolExecutor() as pool:
    pass

