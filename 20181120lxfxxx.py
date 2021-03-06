import types

class Animal(object):
    def run(self):
        print('Animal running......')

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Ant(object):
    def run(self):
        print('Ants are running')

animal = Animal()
animal.run()

dog2 = Dog()
dog2.run()

def Control(animal):
    animal.run()
    animal.run()

a = Ant()

dd = Control(a)

print(type(abs))
if type(abs) == types.BuiltinFunctionType:
    print(True)

print(isinstance(a,Animal))

print(dir(a))


# 定义Student类， 没增加一个实例，count+1
class Student(object):
    count = 0
    def __init__(self, name):
        self.name = name
        Student.count += 1

a = Student('A')
b = Student('B')
a.age = 23
print(a.name, a.count)
print(a.name, a.count)
print(a.age)

class Peole(object):
    #
    __slots__ = ('_birth', '_age')
    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self, value):
        self._birth = value
    @property
    def age(self):
        return 2018 - self._birth

a = Peole()
a._birth = 13
a._age = 234

print(a._birth, a.age)


# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
class Screen(object):
    __slots__ = ('_width', '_height')
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        self._width = value
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        self._height = value

voc = Screen()
voc._width = 1024
voc._height = 768
print(voc._width, voc._height)


class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student name is {}'.format(self.name)

s = Student('Liu')
print(s)

from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr'))

for name,member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def show(self):
        return '{}\'s gender is {}'.format(self.name, self.gender)

s = Student('Chen', 0)
print(s.show())

import logging

try:
    print('xxx')
    r = 10 / 0
    print('r:',r)
except ZeroDivisionError as e:
    print('except:', e)
# except ValueError as e:
#     print('except:', e)
# except Exception as e:
#     logging.exception(e)

finally:
    print('finally,,,')
print('END')

for i in range(10):
    print(i)
    print('')

from functools import reduce

def str2num(s):
    return int(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7')
    print('99 + 88 + 7 =', r)

main()

# try:
with open('C:\\Users\Administrator\Desktop\\1111.txt', 'r+', encoding='utf-8') as f:
    f.write('Hello,world!\n')
    for line in f.readlines():
        print(line)
# except Exception as e:
#     # logging.exception(e)
#     print(e)

from io import StringIO
f = StringIO()
f.write('key')
print(f.getvalue())

import os
print(os.name)
print(os.environ)
print(os.environ.get('PATH'))

import pickle
d= dict(name='Bob', age=25, score=78)
pickle.dumps(d) # d序列化
print(pickle.dumps(d))
with open('C:\\Users\Administrator\Desktop\dump.txt', 'wb') as f:
    # 序列化
    pickle.dump(d, f)
# 反序列化
with open('C:\\Users\Administrator\Desktop\dump.txt', 'rb') as f1:
    d1 = pickle.load(f1)
print(d1)

import json
js1 = json.dumps(d)
py1 = json.loads(js1)
print(py1)


