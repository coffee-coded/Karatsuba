
def Karatsuba_multiplication(x,y):
	if x<10 and y<10:
		return x*y
	else:
		if x<10 and y>9:
			a=1
			b=x
			c=int(y/10**(int(len(str(y))/2)))
			d=int(y%10**(int(len(str(y))/2)))
		elif y<10 and x>9:
			a =1
			b =y
			c = int(x/10**(int(len(str(x))/2)))
			d = int(x%10**(int(len(str(x))/2)))
		else:
			a =int(x/10**(int(len(str(x))/2)))
			b =int(x%10**(int(len(str(x))/2)))
			c =int(y/10**(int(len(str(y))/2)))
			d =int(y%10**(int(len(str(y))/2)))
		if x >y:
			return (10**(int(len(str(x)))))*(Karatsuba_multiplication(a,c)) + (10**(int(len(str(x))/2)))*(Karatsuba_multiplication(a,d) + Karatsuba_multiplication(b,c)) + Karatsuba_multiplication(b,d)
		else:
			return (10 ** (int(len(str(y))))) * (a * c) + (10 ** (int(len(str(y)) / 2))) * (a * d + b * c) + b * d


def input_a():
	global a
	try:
		a = int(input(" First number : "))
	except:
		print("Sorry, we only accept integers. Please provide a number")
		input_a()


def input_b():
	global b
	try:
		b = int(input(" First number : "))
	except:
		print("Sorry, we only accept integers. Please provide a number")
		input_b()

if __name__ == "__main__":
	input_a()
	input_b()
	print("\nAnswer : ",Karatsuba_multiplication(a,b))
