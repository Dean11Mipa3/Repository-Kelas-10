"""
4!	= 4 x 3!
	= 4 x (3 x 2!)
	= 4 x (3 x (2 x 1!))
	= 4 x (3 x (2 x 1))
"""

def factorial(number):
	if number < 0:
		return
	if number == 0 or number == 1:
		return 1
	return number * factorial(number-1)

num = 0
print(factorial(num))