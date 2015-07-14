# __slots__ accepts a tuple and not applied to child class.
class Student(object):
	__slots__ = ('name', 'age', 'set_age')
	pass

s = Student()
s.age = 25
print(s.age)

def set_age(self, age):
	self.age = age

from types import MethodType
s.set_age = MethodType(set_age,s)
s.set_age(20)
print(s.age)

Student.set_age = MethodType(set_age, Student)


class Person(object):

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, value):
		self._name = value

p = Person()
p.name = 'Robert'
print(p.name)

# multiple inheritance

class Animal(object):
	pass

class Mammal(Animal):
	pass

class Bird(Animal):
	pass

class Dog(Mammal):
	pass

class Bat(Mammal):
	pass

class Parrot(Bird):
	pass

class Ostrich(Bird):
	pass

class Runnable(object):
	def run(self):
		print('Running...')

class Flyable(object):
	def fly(self):
		print('flying...')

class Cat(Mammal, Runnable):
	pass

c = Cat()
c.run()

# Mixin is not is-a. similar to 'interface' but is implemented.
class EatableMixIn():
	pass