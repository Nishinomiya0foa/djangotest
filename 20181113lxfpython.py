import sys
from collections import Iterable
from collections import Iterator

print('*******************')

def add(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
ad = add(1,2,3,4)

print(ad())










# # 利用filter()筛选出回数
# def _nums():
#     n = 1200
#     while n < 1244:
#         n = n + 1
#         yield n
#
# def _huiwen(n):
#     s = list(str(n))
#     x = len(s) // 2
#     for i in range(x):
#         if s[i] == s[len(s)-i-1]:
#             continue
#         else:
#             return False
#     return True
#
#
# for n in _nums():
#     print(n)
#     print(_huiwen(n))


print('*******************')



# 生成器 从3开始的奇数  无限
def _odd_iter():
    n = 1
    while True:
        n = n+2
        yield n

def _not_divisible(n):
    return lambda x:x%n>0

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    if True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列

for n in primes():
    if n < 1000:
        print(n)
    else:
        break




a = [1,2,3,4,5,6,7,8,9,0]
print(list(filter(lambda x : x%2!=0, a)))


def f(x):
    return x * x
print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

def add(x, y, f):
    return f(x)+f(y)

print(add(-3, -2, abs))


print(abs(-10))


a = ('a', 'b', 'c')
print(isinstance(a, Iterable))
print(isinstance(iter(a), Iterator))

def numbers():
    print('step 1')
    yield 1
    print('step 2')
    yield (2)
    print('step 3')
    yield (3)

num = numbers()
for i in range(0,3):
    next(num)


def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()