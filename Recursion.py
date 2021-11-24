'''Recursion in data structure using python 
1. divide a big problem into a small one 
2.find a base condition with simple ans
3.return ans to base condition for solving all sub problems
find the sum of numbers from 1 to 5
here e.g 5+10=15
         4+6=10
         3+3=6
         2+1=3
         1==1 @@@ the base condition is find the sum between 1 to 1

recursion in python '''
def find_sum(n):
    if (n==1):
        return 1
    return n + find_sum(n-1)
    print(find_sum(n))
result=print(find_sum(5))
 
'''output=15 so we can reduce the no of itretions by using recursion'''


'''fibonaci series using recursion'''
def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1)+fib(n-2)
result=print(fib(10))
        