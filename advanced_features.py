#-- consequence --
L = ['Michael','Sarah','Tracy','Bob','Jack']
print(L[0:3])
print(L[::2])
#slimlar to substring
print('abcde'[:3])

#-- iteration --
#dict: default is keys. others, d.values(), d.items()
d = {'A':1, 'B':2, 'C':3}
for k, v in d.items():
	print(k,v)
from collections import Iterable
print(isinstance('ABC',Iterable))
#convert list to be index based
for i,value in enumerate(['A', 'B', 'C']):
	print(i,value)

#-- List comprehensions --
print(list(range(1,11)))
print(range(1,11))
#list(range()) is equal to range() when use in for-in
print([x * x for x in list(range(1,11))])
print([x * x for x in range(1,11) if x %2 == 0])
print('A'+'B')
print([m + n for m in 'ABC' for n in 'XYZ'])
#list all files and dir
import os
print([d for d in os.listdir('.')])
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]
print(L2)

#-- generator --
L = [x*x for x in range(10)]
print(L)
# next()
g = (x*x for x in range(10))
for n in g:
	print(n,end='')
def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a + b
		n = n + 1
	return 'done'
for x in fib(6):
	print(x)
#yanghui trangle
def trangles():
	L = [1]
	yield L
	while True:
		if len(L) > 1:
			L = [L[i]+L[i-1] for i in range(1,len(L))]
			L.insert(0,1)
		L.append(1)
		yield L
def getYH(x):
	t = 0
	for l in trangles():
		print(l)
		t = t + 1
		if(t == x):
			break
getYH(5)

#-- Ietrator --
from collections import Iterator
from collections import Iterable
print(isinstance([], Iterable))
print(isinstance([], Iterator))
# list , dict, string is not Ietrator
print(isinstance(iter([]),Iterator))