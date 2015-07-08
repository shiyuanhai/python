# -- functional programming --
#high order functional
print(abs(-10))
print(abs)
def add(a,b,f):
	return f(a) + f(b)
print(add(1,-1,abs))

#-- map/reduce
def f(x):
	return x * x
l = [1,2,3]
r = map(f,l)
print(list(r))
print(list(map(str,[1,2,3])))
from functools import reduce
def fn(x, y):
	return x * 10 + y
def char2num(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
print(reduce(fn,map(char2num,'12345')))
def normalize(name):
    return name.capitalize()
L1=['admam','LISA','barT']
L2=list(map(normalize,L1))
print(L2)
def str2float(s):
	sl = s.split('.')
	sint = reduce(lambda x,y : x * 10 + y, map(char2num, sl[0]))
	sfloat = reduce(lambda x,y : x / 10 + y, map(char2num,sl[1][::-1])) / 10
	return sint + sfloat
print('str2float(\'123.456\') =', str2float('123.456'))
print('123'[::-1])

#-- filter --
def is_odd(n):
	return n % 2 == 1
print(list(filter(is_odd,[1,2,3])))
# get primes
def _odd_iter():
	n = 1
	while True:
		n = n + 2
		yield n
def _not_divisible(n):
	return lambda x : x % n > 0
def primes():
	yield 2
	it = _odd_iter()
	while True:
		n = next(it)
		yield n
		it = filter(_not_divisible(n), it)
for n in primes():
	if n < 10:
		print(n)
	else:
		break
#check palindrome
def is_palindrome(n):
	return str(n) == str(n)[::-1]
print(list(filter(is_palindrome,range(10,30))))

#-- sorted --
print(sorted([1,3,2]))
print(sorted(['Ac','aB'], key=str.lower, reverse=True))
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
	return t[0]
print(sorted(L,key=by_name))
def by_score(t):
	return t[1]
print(sorted(L,key=by_score,reverse=True))
