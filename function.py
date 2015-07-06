#-- invoke function --
print(abs(-10))
print(max(1,2,3,4))
print(int('12'))
print(bool(0))
robert = max
print(robert(1,2,3))

#-- define function --
def my_abs(x):
	return abs(x)
print(my_abs(-10))
# use pass as TODO
def doitlater():
	pass
#check if x is valid
#if not isinstance(x,(int,float))
import math
def move(x, y, step, angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx,ny
x,y = move(100,100,60, math.pi/6)
print(x,y)

#-- function parameter --
def power(x, n=2):
	s = 1
	while n > 0 :
		n = n - 1
		s = s * x
	return s
print(power(10,3))
print(power(10))
# default param for one function is shared.
def add_end(L=[]) :
	L.append('END')
	return L
print(add_end());
print(add_end());
def add_end(L=None) :
	if L is None:
		L = []	
	L.append('END')
	return L
print(add_end());
print(add_end());
#variable param
def calc(*numbers) :
	sum = 0
	for n in numbers :
		sum = sum + n
	return sum
print(calc(1,2,3))
nums = [1,2,3]
print(calc(*nums))
#keyword param
def person(name, age, **kw):
	print('name :',name,' age: ',age, ' other :',kw)
print(person('Robert',30,city='Princeton'))
extra = {'ssn':123456789,'DOB':'1900/1/1'}
print(person('Sally',20,**extra))
def person(name, age, *, city, job):
	print(name,age,city,job)
person('Bob', 23, city='Shanghai', job='Developer')
def f1(a, b, c=0, *args, **kw) :
	print('a=', a, 'b=', b, 'c=', c, 'args=', args, 'kw=', kw)
args = (1, 2, 3, 4)
kw = {'d':5,'e':6}
f1(*args,**kw)

#-- recursive function --
def fact(n) :
	if n==0 :
		return 0
	if n==1 :
		return 1
	return n * fact(n-1)
print(fact(5))
# opt
def fact(n):
	return fact_iter(n,1)
def fact_iter(num, product):
	if num == 1:
		return product
	return fact_iter(num-1, num * product)
print(fact(5))

# hanoi
def move(n, a, b, c):
	if n == 1:
		print('%s --> %s'%(a,c))
	else:
		move(n-1,a,c,b)
		print('%s --> %s'%(a,c))
		move(n-1,b,a,c)
move(3,'A','B','C')