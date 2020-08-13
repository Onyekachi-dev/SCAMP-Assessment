Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def fibonacci (n) :
	a = 0
	b = 1
	if n < 0:
		print("Incorrect input")
	elif n== 0:
		return a
	elif n==1:
		return b
	else :
		for i in range (2,n):
			c = a + b
			a = b
			b = c
		return b
	print(fibonacci(9))

	
>>> print (fibonacci (9))
21
>>> 