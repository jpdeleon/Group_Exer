#import math library
import math

#define the factorial function as `fact` with input n.
#check: if n is equal to 1, return 0; else, return n*fact(n-1)
def fact(n):
    #define 0!=1
    if n == 0:
        return 1
    #otherwise return n! = n*(n-1)*(n-2)*...
    else:
        return n*fact(n-1) #recursion

#the loop will be infinite unless we specify the precision; e.g. 8 decimal places
#define a function `e` to compute e with input eps.
#eps specify the precision; e.g. 0.001
def e(eps):
    x = 1 
    e = 1 + x + float(1.0/fact(2))
    i = 3 
    #do recursion as long as difference x-e >= eps
    while math.fabs(x-e) >= eps:
        #initialize x
        x = e
        e += float(1.0/fact(i))
        #increment i
        i += 1
    return e 

print("The mathematical constant e")
#compute the value of e using with eps = 0.00000001
print(e(0.00000001))

#For comparison of result, print the built-in value of e
print(math.e)