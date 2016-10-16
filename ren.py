# -*- coding: utf-8 -*-
from sympy import *

def list_to_frac(l):
	expr = Integer(0)
	for i in reversed(l[1:]):
		expr += i
		expr = 1/expr
	return l[0] + expr

x = 354224848179261915075
y = 218922995834555169026

result=[]

while x>0 and y>0:
	if y!=0:
		result.append(int(x/y))
		print '%d を %d で割った商は %d で余剰は %d' % (x, y, x/y, x%y)
		x = x%y
	if x!=0:
		result.append(int(y/x))
		print '%d を %d で割った商は %d で余剰は %d' % (y, x, y/x, y%x)
		y = y%x

print result
print list_to_frac(result)

