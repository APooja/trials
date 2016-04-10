s = raw_input("enter the operation :")
a= int(raw_input("enter the operand 1 :"))
b=int(raw_input("enter the operand2 :"))
def add(a,b):
	print a+b
def sub(a,b):
	print a-b
def div(a,b):
	print a/b
def multi(a,b):
	print a*b

if (s=="+"):
	add(a,b)
elif s=="-":
	sub(a,b)
elif s=="/":
	div(a,b)
elif s=="*":
    multi(a,b)
else :
	print "you have entered a wrong operation"	
    