def fib(n):
 	if n<=2:
         return 1
 	 
 	else:
 	 return fib(n-1)+fib(n-2)

t= int( raw_input("enter the no. where fib. series can run :") )         

for i in range(1,t):
    print fib(i)


