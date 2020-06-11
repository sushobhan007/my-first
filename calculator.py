number1=input("Enter number: ")
number2=input("Enter number: ")
number1=float(number1)
number2=float(number2)
print("What do you want to do?")
print("Addition")
print("Subtraction")
print("Multiplication")
print("Division")
choice=input("Enter your choice: ")
if choice == "Addition":
    addition()
elif choice == "Subtraction":
    subtraction()
elif choice == "Mulplication":
    mult()
elif choice == "Division":
    div()

def addition():
    sum=number1+number2
    print("The Sum of" , number1, "and", number2, "is", sum)
    return(sum)
def subtraction():
    sub=number1-number2
    print("The Subtraction of" , number1, "and", number2, "is", sub)
def mult():
    mul=number1*number2
    print("The Mulplication of" , number1, "and", number2, "is", mul)
def div():
    divi=number1/number2
    print("The Division of" , number1, "and", number2, "is", divi)
