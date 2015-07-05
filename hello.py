print('hello world')
# -*- coding: utf-8 -*-

print('Have','a','nice','day')
print('100 + 200 =',100+200)

# name = input('input your name: ')

# print absolute value for variable
a = -100
if a >= 0 :
	print(a)
else :
	print(-a)

#data type and variables
print("I\'m \"OK\"")
print(r'Hello, "Bart"')
print(r'\\t\\')
print(True and False)

a = 'abc'
b = a
a = 'xyz'
print(b)

#-- string and encoding --
#print('中')
print(ord('A'))
print(chr(66))
#b'ABC' -> bytes type. each char is one byte
print('ABC'.encode('ascii'))
print(b'ABC'.decode('ascii'))
#len str->char count, bytes-> byte count
print(len('abc'))
#format, %d %f %s %x
print('hello, %s' % 'bob')
# %s convert any type to strig, %% - > %
print('True or False: %s' % True)
print('72/85: %.2f' % (72/85))

#-- list and tuple --
#list (ArrayList)
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))
print(classmates[-1])
classmates.append('Adam')
print(classmates)
#insert at index. 
classmates.insert(1,'Jack')
print(classmates)
#delete last from list. pop(index)
classmates.pop()
print(classmates)
#tuple (Array)
#... t = (1,)
roommates = ('Michael', 'Bob', 'Tracy')
print(roommates)

#-- if else --
age = 20
if age >= 18 :
	print('your age is', age)
	print('adult')
elif age > 6:
	print('teenager')
else :
	print('kid')
# 0, empty str, empty list are False
# input(), convert str to int

#-- loop --
names = ['1','2','3']
for name in names:
	print(name)
#sum(100)
sum = 0
for x in range(101):
	sum = sum + x
print(sum)
#while
sum = 0
n = 100
while n > 0 :
	sum = sum + n
	n = n - 1
print(sum)

#-- dict and set --
# key in dict is immutable, list can't be a key
d = {'Michael':95, 'Bob':75, 'Tracy':85}
print('Bob\'s score is',d['Bob'])
d['adam'] = 99
print(d['adam'])
if('Bob' in d):
	print('Bob is in d')
print(d.get('Peter',-1))
d.pop('Bob')
print(d.get('Bob',-1))
# set(list). use & and | for math
s = set([1,2,3])
print(s)
s.add(4)
print(s)
s.add(4)
print(s)
s.remove(4)
print(s)
# tuple can be key in dict or value in set. (1, [2, 3]) can't
d[(1, 2, 3)] = 10
print(d)
s.add((1, 2, 3),)
print(s)
