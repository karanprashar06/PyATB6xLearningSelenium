#write a program for fibbochi series
import math
n = int(input("enter number"))
# a=0
# b=1
# for i in range(1,n):
#     print(a, end=" ")
#     a,b = b,a+b
#
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)


for i in range(n):
    print(fibonacci(i), end=" ")