def add(a,b):
	return a+b
	
def subtract(a,b):
	return a-b
	
def multiply(a,b):
	return a*b 

def divide(a,b):
	return a/b

def square(a):
	return a*a

def cube(a):
	return a*a*a

def square_n_times(a,n):
	final_product = a
	for i in range(0,n):
		final_product = square(final_product)
	return	final_product 

print("I'm going use the calculator functions to multiply 5 and 6")
x = multiply(5,6)

print(x)

y = square_n_times(2,2)

print(y)
