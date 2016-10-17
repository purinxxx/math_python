from sympy import *

def list_to_frac(l):
	expr = Integer(0)
	for i in reversed(l[1:]):
		expr += i
		expr = 1/expr
	return l[0] + expr

print list_to_frac([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

