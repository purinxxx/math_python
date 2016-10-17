# -*- coding: utf-8 -*-
from sympy import *

def list_to_frac(l):
	expr = Integer(0)
	for i in reversed(l[1:]):
		expr += i
		expr = 1/expr
	return l[0] + expr

def list_to_expr(l):
	expr = ''
	tex = ''
	for i in l[:-1]:
		expr += str(i) + '+1/('
		tex += str(i) + r'+\frac{1}{'
	expr = expr[:-1] + str(l[-1]) + ')' * (len(l)-2)
	tex = tex + str(l[-1]) + '}' * (len(l)-1)
	yield expr
	yield tex

x = 354224848179261915075
y = 218922995834555169026
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]

x = 5275871481466581051
y = 3681369418442407670
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

x = 1618034
y = 1000000
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 14, 2, 2]

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

for i in list_to_expr(result):
	print i

for i in xrange(len(result)):
	print list_to_frac(result[:i+1])

