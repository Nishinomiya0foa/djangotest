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


