class Student(object):
	"""docstring for Student"""
	def __init__(self, name, score):
		self.name = name
		self.score = score

	def print_score(self):
		print("%s: %s" % (self.name, self.score))

	def get_grade(self):
		if self.score > 90:
			return 'A'
		elif self.score >= 60:
			return 'B'
		else:
			return 'C'

robert = Student('Robert',100)
robert.print_score();
print(robert)
print(robert.get_grade())
#private instance variable e.g. __name -> _Student__name
#use getter/setter 


class Animal(object):
	def run(self):
		print("Animal is running")

class Dog(Animal):
	def run(self):
		print("Dog is running")

class Cat(Animal):
	def run(self):
		print("cat is running")

dog = Dog()
dog.run();
print(isinstance(dog,Dog))
print(type(dog))

import types
print(types.FunctionType)
print(dir(dog))


#getattr(), setattr()

#class variable
class Student(object):
	name = 'Student'

s = Student()
print(s.name)
print(Student.name)