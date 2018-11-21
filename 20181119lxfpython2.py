import time
import functools


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now():
    print(time.localtime())
f = now()


max10 = functools.partial(max, 10)
maxNum = max10(3,4,1,5,6,7)
print(maxNum)

class Student(object):
    def __init__(self, name, age, grade):
        self.__name = name
        self.__age = age
        self.__grade = grade

    def get_name(self):
        return self.__name

    def print_age(self):
        print('{}的年龄为：{}'.format(self.__name, self.__age))

    def get_grade(self):
        if self.__grade >= 80:
            return 'A'
        else:
            return 'Noob'

li = Student('Li', 12, 33)
# 这种方法的 name 属性 与 方法内部的 __name 属性不是同一东西了
li.__name = 'Li wen'
print(li.__name)
# 这才是内部的__name
print(li.get_name())
li.print_age()
print(li.get_grade())
