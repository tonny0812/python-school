# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     distributeTest
   Description :   分布式队列, https://github.com/qiyeboy/SpiderBook/blob/master/ch01/1.4.4.py
   Author :       guodongqing
   date：          2019/10/05
-------------------------------------------------

"""
import threading
import time
from multiprocessing import Queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support


class QueueManager(BaseManager):
    pass


def taskManager_linux():
    # 第一步，建立task_queue和result_queue，用来存放任务和结果
    task_queue = Queue.Queue()
    result_queue = Queue.Queue()
    # 第二步，把创建的两个队列注册在网络上，利用register方法，callable参数关联了Queue对象，
    # 将Queue对象在网络中暴露

    QueueManager.register('get_task_queue', callable=lambda: task_queue)
    QueueManager.register('get_result_queue', callable=lambda: result_queue)

    # 第三步，绑定端口8001，设置验证口令‘test’, 相当于对象的初始化
    manager = QueueManager(address=('', 8001), authkey=b'test')

    # 第四步，启动管理，监听信息通道
    manager.start()

    # 第五步，通过管理实例的方法获得通过网络访问的Queue对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    # 第六步，添加任务
    for url in ["ImageUrl_" + i for i in range(10)]:
        print('put task %s ...' % url)
        task.put(url)

    # 返回结果

    print('try get result...')
    for i in range(10):
        print('result is %s' % result.get(timeout=10))

    # 关闭管理
    manager.shutdown()

# 任务个数
task_number = 10
# 第一步，建立task_queue和result_queue，用来存放任务和结果
task_queue = Queue(task_number)
result_queue = Queue(task_number)

# 第二步，把创建的两个队列注册在网络上，利用register方法，callable参数关联了Queue对象，
# 将Queue对象在网络中暴露

def get_task():
    return task_queue

def get_result():
    return result_queue

# win不支持lambda
def taskManager_win():


    QueueManager.register('get_task_queue', callable=get_task)
    QueueManager.register('get_result_queue', callable=get_result)

    # 第三步，绑定端口8001，设置验证口令‘test’, 相当于对象的初始化
    manager = QueueManager(address=('127.0.0.1', 8001), authkey=b'test')

    # 第四步，启动管理，监听信息通道
    manager.start()
    try:
        # 第五步，通过管理实例的方法获得通过网络访问的Queue对象
        task = manager.get_task_queue()
        result = manager.get_result_queue()

        # 第六步，添加任务
        for url in ["ImageUrl_" + str(i) for i in range(10)]:
            print('put task %s ...' % url)
            task.put(url)

        # 返回结果
        print('try get result...')
        for i in range(10):
            print('result is %s' % result.get(timeout=15))

    except Exception as e:
        print('Manager error...', e)
    finally:
        # 关闭管理
        manager.shutdown()


def taskWorker():
    # 第一步，使用QueueManager注册用于获取Queue的方法名称
    QueueManager.register('get_task_queue')
    QueueManager.register('get_result_queue')
    # 第二步，连接到服务器
    server_addr = '127.0.0.1'
    print('Connect to server %s ...' % server_addr)
    # 端口和验证口令
    m = QueueManager(address=(server_addr, 8001), authkey=b'test')
    # 从网络连接:
    m.connect()
    # 第三步，获取Queue的对象
    task = m.get_task_queue()
    result = m.get_result_queue()
    # 第四步，从task队列获取任务，并把结果写入result队列
    while (not task.empty()):
        image_url = task.get(True, timeout=15)
        print('Run task download %s ...' % image_url)
        time.sleep(1)
        result.put('%s--->success...' % image_url)
    print('Worker exit...')


if __name__ == "__main__":
    freeze_support()
    server = threading.Thread(target=taskManager_win, name="taskManager_win")
    worker = threading.Thread(target=taskWorker, name="taskWorker")
    server.start()
    time.sleep(5)
    worker.start()
