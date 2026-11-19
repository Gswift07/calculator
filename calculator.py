#SCCM910 lab project- a four- operation calculator
def add(a,b):
        return a+b
def subtract (a,b):
	return a-b
def multiply (a,b):
	return  a+b
def divide (a,b):
	return a/b
def CiricleArea(r):
	if r>=0:
		return 3.14 * r * r
	else:
		return "Error"


def main():
	while True:
		a=float(input("Enter first number:"))
		op = input("Operator (+,-,*,/):")
		b=float(input("Second number:"))
		if op =="+":
			print("Results", add(a,b))
		elif op =="-":
                        print("Results", subtract(a,b))
		elif op =="*":
			print("Results",multiply(a,b))
		elif op =="/":
			print("Results", divide(a,b))


if __name__=="__main__":
	main()
