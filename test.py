from sympy import *

def list_to_frac(l):
	expr = Integer(0)
	for i in reversed(l[1:]):
		expr += i
		expr = 1/expr
	return l[0] + expr

def list_to_frac_expr(l):
	expr = ''
	for i in l:
		expr += str(i) + '+1/('
	expr = expr[:-4] + ')' * (len(l)-1)
	return expr

print list_to_frac([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
print list_to_frac_expr([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

