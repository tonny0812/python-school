# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     processThreadTest
   Description :   进程，对应多核
   Author :       guodongqing
   date：          2019/9/30
-------------------------------------------------
"""


# 无法在windows上执行
def linuxForkTest():
    import os
    print(u"当前进程(%s)开始..." % os.getpid())
    pid = os.fork()
    if pid < 0:
        print(u"fork出现错误")
    elif pid == 0:
        print(u"我是子进程(%s)，我的父进程是(%s)" % (os.getpid(), os.getppid()))
    else:
        print(u"我(%s)创建了子进程(%s)" % (os.getpid(), pid))


def run_proc(name):
    print(u"子进程%s (%s) 正在执行中..." % (name, os.getpid()))


# 使用multiprocessing包，进程
def mulProcessTest():
    import os
    from multiprocessing import Process
    print(u"父进程(%s)" % os.getpid())
    for i in range(5):
        p = Process(target=run_proc, args=(str(i),))
        print(u"Process进程(%s)将会开始" % i)
        p.start()
    p.join()
    print(u"Process进程结束...")


def run_task(name):
    import os, time, random
    print(u"任务 %s (pid = %s) 正在执行..." % (name, os.getpid()))
    time.sleep(random.random() * 3)
    print(u"任务 %s 结束..." % name)


# 进程池
def mulPoolTest():
    import os
    from multiprocessing import Pool
    print(u"当前进程 %s " % os.getpid())
    pool = Pool(processes=3)
    for i in range(5):
        pool.apply_async(run_task, args=(i,))
    print(u"等待所有子进程完成...")
    pool.close()
    pool.join()
    print(u"所有子进程完成...")

# 进程通信
def proc_write(q, urls):
    import os, random, time
    print(u"进程%s正在写入..." % os.getpid())
    for url in urls:
        q.put(url)
        print(u"将%s加入到队列中..." % url)
        time.sleep(random.random())

def proc_read(q):
    import os, random, time
    print(u"进程%s正在读取..." % os.getpid())
    while True:
        url = q.get(True)
        print(u"从队列中获取到%s" % url)

def proc_send(pipe, urls):
    import random, time
    for url in urls:
        pipe.send(url)
        print(u"将%s加入到管道中..." % url)
        time.sleep(random.random())

def proc_recv(pipe):
    import random, time
    while True:
        url = pipe.recv()
        print(u"从管道中获取到%s" % url)
        time.sleep(random.random())

# Queue 队列 是多对多，Pipe是一对一
def processCommunicateWithQueue():
    from multiprocessing import Queue, Process
    q = Queue()
    proc_writer1 = Process(target=proc_write, args = (q,['url_1_1','url_1_2','url_1_3','url_1_4','url_1_5']))
    proc_writer2 = Process(target=proc_write, args = (q,['url_2_1','url_2_2','url_2_3','url_2_4']))
    proc_reader = Process(target=proc_read, args=(q,))
    proc_writer1.start()
    proc_writer2.start()
    proc_reader.start()
    proc_writer1.join()
    proc_writer2.join()
    proc_reader.terminate()

def processCommunicateWithPipe():
    from multiprocessing import Pipe, Process
    pipe = Pipe()
    proc_sender = Process(target=proc_send, args = (pipe[0],['url_'+str(i) for i in range(10)]))
    proc_recver = Process(target=proc_recv, args=(pipe[1],))
    proc_sender.start()
    proc_recver.start()
    proc_sender.join()
    proc_recver.join()


if __name__ == "__main__":
    # linuxForkTest()
    # mulProcessTest()
    # mulPoolTest()
    processCommunicateWithQueue()
    # processCommunicateWithPipe()