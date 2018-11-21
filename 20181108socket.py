from socket import *
import random

import math
import re


# 递归
def ManyNums(n):
    if n > 10:
        return 0
    return n+ManyNums(n + 1)

nums = ManyNums(1)
print(nums
      )

# 函数打印斐波那契数列
def Fib(n):
    l = [1,1]
    for i in range(n):
        if i > 1:
            c = l[i-1] + l[i-2]
            l.append(c)
    return l
fibn = Fib(1)
print(fibn)






# 请使用迭代查找一个list中最小和最大值，并返回一个tuple
l = []
for i in range(10):
    l.append(random.randint(0,20))
# print(l)
def FindMinAndMax(l):
    mi = l[0]
    ma = l[0]
    for i in l:
        if i < mi:
            mi = i
        if i > ma:
            ma = i
    # mi = min(l)
    # ma = max(l)
    return (mi,ma)
a = FindMinAndMax(l)
print(l)
print(a)





dict = {'a':1, 'b':2, 'c':3}
l = 'aaaaadfwef'
for key,i in enumerate(l):
    print(key, i)
print(dict.keys(), dict.items(), dict.values())

l = list(range(100))
print(l[11::2])

# 递归函数 - 调用本身
# 阶乘n
def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)
print(fact(4))


# 函数 接受1或多个数，计算他们的乘积
# def ddd(*a):
#     sum = 1
#     for n in a:
#         if re.match(r'[0-9]+', n):
#             print(re.match(r'[0-9]+', n).group())
#             sum = n * sum
#     print(sum)
# x = ddd(3,4,1,0,'x')


def quadratic(a ,b ,c):
    x1 = (-b+math.sqrt(b*b-4*a*c))/(2*a)
    x2 = (-b-math.sqrt(b*b-4*a*c))/(2*a)

    return x1, x2

s = quadratic(2, 3, 1)
print(s)
tcpSock = socket(AF_INET, SOCK_STREAM)

# name = input('Input your name:')
# print('Your name is', name)

a = 12 // 3
a = r'''
    Hello,wo_fdsr/
'''
a = '中文str'
a = ord('A')
a = chr(25991)
l = [1,543,6436,1,2321,32]
a = l[len(l)-1] - l[0]
t = (1,)

b = 3
c = 2
t = (a, b ,c)

t = 0
for i in range(0,101):
    t = t + i

t = 0
x = 1
while x < 100:
    t = x + t
    x = x + 2




d = {'Ada': '3x', 'Bob':27, 'Clod': 37, 'Diana': 14}
t = d['Ada']
d.get('fds', 32)

print(d)


def circle(PI, r):
    s = PI*r*r
    c = 2*PI*r
    return s


PI = 3.1415927
r = 3
c3 = circle(PI, r)

print(type(c3))

def f(a,b,c=2,d=2):
    return a,b,c,d

fn = f(1,2,d=4,c=3)
print(fn)


def f2(a,b,**c):
    return a,b,c


tt = f2(32,421,lo=32,fji=321)
print(tt)



