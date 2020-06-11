x=int(input("Enter 1st Number: "))
y=int(input("Enter 2nd Number: "))
if x>y:
	smaller=x
else:
	smaller=y
for i in range(1,smaller+1):
	if ((x%i==0) and (y%i==0)):
		gcd=i
print("The GCD is: ",gcd)