f=1
a1=int(input("Enter a number to check its factorial: "))
if a1<0:
	print("Fibonacci is not possible for negetive numbers.")
elif a1==0:
	print("Factorial of 0 is 1.")
else:
	for a2 in range(f,a1+1):
		f=f*a2
	print("The factorial of",a1,"is:",f,end="")