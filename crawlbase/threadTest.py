# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     threadTest
   Description :   线程，使用单核，适合多io场景
   Author :       guodongqing
   date：          2019/9/30
-------------------------------------------------
"""


def thread_run(urls):
    import threading, time, random
    print(u"当前线程%s正在运行..." % threading.current_thread().name)
    for url in urls:
        print("%s---->>>%s" % (threading.current_thread().name, url))
        time.sleep(random.random())
    print(u"%s完成..." % threading.current_thread().name)


# 直接使用Thread
def threadTest():
    import threading
    print(u"%s线程开始运行..." % threading.current_thread().name)
    t1 = threading.Thread(target=thread_run, name="Thread1",
                          args=(['url_1_1', 'url_1_2', 'url_1_3', 'url_1_4', 'url_1_5'],))
    t2 = threading.Thread(target=thread_run, name="Thread2", args=(['url_2_1', 'url_2_2', 'url_2_3', 'url_2_4'],))
    t1.start()
    t2.start()
    print(u"%s线程结束..." % threading.current_thread().name)


# 继承Thread，重写run方法
def threadTest2():
    import threading, time, random
    class myThread(threading.Thread):
        def __init__(self, name, urls):
            threading.Thread.__init__(self, name=name)
            self.urls = urls

        def run(self):
            print(u"当前线程%s正在运行..." % threading.current_thread().name)
            for url in self.urls:
                print("%s---->>>%s" % (threading.current_thread().name, url))
                time.sleep(random.random())
            print(u"%s完成..." % threading.current_thread().name)

    print(u"%s线程开始运行..." % threading.current_thread().name)
    t1 = myThread(name='Thread_1', urls=['url_1_1', 'url_1_2', 'url_1_3', 'url_1_4', 'url_1_5'])
    t2 = myThread(name='Thread_2', urls=['url_2_1', 'url_2_2', 'url_2_3', 'url_2_4', 'url_2_5'])
    t1.start()
    t2.start()
    print(u"%s线程结束..." % threading.current_thread().name)

# 线程同步，共有变量，需要加锁
num = 0
def threadLockTest():
    import threading, time, random
    class myThread(threading.Thread):
        def __init__(self, name):
            threading.Thread.__init__(self, name=name)

        def run(self):
            print(u"当前线程%s正在运行..." % threading.current_thread().name)
            global num
            while True:
                mylock.acquire()
                print("%s上锁，共享资源数值：%d\n" % (threading.current_thread().name, num))
                if num >=4:
                    mylock.release()
                    print("%s释放锁，共享资源数值：%d\n" % (threading.current_thread().name, num))
                    break
                num += 1
                time.sleep(random.random())
                mylock.release()
                print("%s释放锁，共享资源数值：%d\n" % (threading.current_thread().name, num))

    mylock = threading.RLock()

    thread1 = myThread("Thread_1")
    thread2 = myThread("Thread_2")
    thread1.start()
    thread2.start()


if __name__ == "__main__":
    # threadTest()
    # threadTest2()
    threadLockTest()
