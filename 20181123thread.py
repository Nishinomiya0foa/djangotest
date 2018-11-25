# 多进程

from multiprocessing import Process, Pool
import os
import time
import random

# 子进程要执行的代码
# def run_proc(name):
#     print('Run child process {} ({})...'.format(name, os.getpid()))
#
#
# if __name__=='__main__':
#     print('Parent process {}.'.format(os.getpid()))
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()  # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
#     print('Child process end.')


# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random())
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))
#
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)  # 同时跑4个进程 0 1 2 3
#     for i in range(5):
#         # p = Process(target=long_time_task, args=(i,))
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')


# def print_animals(a):
#     print('{} is running...'.format(a))
#     start = time.time()
#     time.sleep(random.random())
#     end = time.time()
#     print(start)
#     print('{} has runned {} seconds.'.format(a, (end - start)))
#
# if __name__ == '__main__':
#     p = Pool(4)
#     l = ['Ant', 'Bee', 'Cat', 'Dog']
#     for i in l:
#         p.apply_async(print_animals, args=(i,))
#     p.close()
#     p.join()

# l = ['Ant', 'Bee', 'Cat', 'Dog']
# for i in l:
#     print_animals(i)

# import subprocess
#
# print('$ nslookup https://www.python.org/')
# r = subprocess.call(['nslookup', 'https://www.python.org/'])
# print('Exit code:', r)

# Python 3: Fibonacci series up to n
# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a+b
#     print()
# fib(1000)

L = [1, 2, 3]
# it = L.__iter__()
it = iter(L)
print(it.__next__())

import threading
def loop0():
    print('loop0 start at: {}'.format(time.ctime()))
    time.sleep(3)
    print('loop0 end at: {}'.format(time.ctime()))

def loop1():
    print('loop1 start at: {}'.format(time.ctime()))
    time.sleep(3)
    print('loop1 end at: {}'.format(time.ctime()))

def main():
    threading.current_thread()
    loop0()
    loop1()

if __name__ == '__main__':
    main()