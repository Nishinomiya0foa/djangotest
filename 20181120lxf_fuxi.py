import re

# 调用函数
# hex()可以把一个10进制整数转换成十六进制的数
print(hex(99))

# 定义函数
# 定义求绝对值得函数 my_abs()
def my_abs(x):
    matchObj = re.match(r'[+-]?[0-9]+(\.[0-9]+)*$', str(x))
    if matchObj:
        if float(x) >= 0:
            return x
        elif float(x) < 0:
            return -float(x)
        else:
            return False
    else:
        return 'No number'

x = '0019.022'
abs_x = my_abs(x)
print(abs_x)

# 函数参数
# 以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积:
# def product(x, y):
#     return x * y

def product(*x):
    al = 1
    for i in x:
        al = al * i
    return al

a = product(10, 209, 3, 0.1)
print(a)

# 递归函数
# 汉诺塔的移动可以用递归函数非常简单地实现。
# 请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法，例如：

# 期待输出:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C
# move(3, 'A', 'B', 'C')

def move(n, a='A', b='B', c='C'):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1, a, c, b)
        # move(1, a, b, c)
        print(a, '-->', c)
        move(n-1, b, a, c)

n = move(3)

# 切片
# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法

def trim(s):
    start = 0
    end = len(s) - 1
    while True:
        if str(s[start]) == ' ':
            start += 1
        elif str(s[end]) == ' ':
            end -= 1
        else:
            break
    return s[start:end+1]

str1 = '    21 fdsf  fd s  ds'
print(trim(str1))

# 迭代
# 请使用迭代查找一个list中最小和最大值，并返回一个tuple
def MaxAndMin(l):
    max = l[0]
    min = l[0]
    for i in l:
        if i > max:
            max = i
        if i < min:
            min = i
    return (max, min)

l = [1,2,4,6,3,1,6,2,32,1,-1, -3]
print(MaxAndMin(l))

# 列表生成式
# 使L1 = ['Hello', 'World', 18, 'Apple', None]中字符串变为小写
L1 = ['Hello', 'World', 18, 'Apple', None]

L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)

# 生成器
# 生成杨辉三角

# def triangles():
#     L=[1]
#     while True:
#         yield L
#         L=[1]+[L[i]+L[i+1] for i in range(len(L)-1)]+[1]
#
# for d in triangles():
#     print(d)

# 高阶函数 map/reduce
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']

def Namely(args):
    return args.capitalize()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(Namely, L1 ))
print(L2)

# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
# from functools import reduce
# def prod(args):
#     m = 1
#     return m * args
# L1 = [1, 2, 3, 5]
# L2 = list(reduce(prod, L1))
# print(L2)
