

def fibonacci(n):
    """
fibonacci
n < 0 ---> "will return the fibonacci(abs(n))"
n = 0 ---> "0"
n = 1 ---> "1"
n > 1 ---> "fibonacci(n-1) + fibonacci(n-2)"
"""
    if n == 0:
        return n
    elif n == 1:
        return 1
    elif n < 0:
        return fibonacci(abs(n)-1) + fibonacci(abs(n)-2)
    else:
        return fibonacci(n-1) + fibonacci(n-2)


    
def lucas(n):
    """
lucas
n is string ---> "will return the lucas(int(n)-1) + lucas(int(n)-2)"
n = 0 ---> "2"
n = 1 ---> "1"
n > 1 ---> "lucas(n-1) + lucas(n-2)"
"""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(int(n)-1) + lucas(int(n)-2)
    
 
def sum_series(n,x=0,y=1):
    """
If x and y are not provided, the function will return the n-th element in the Fibonacci series
If x = 2 and y = 1, the function will return the n-th element in the Lucas series 
If n was not a number greater than 1 it will work as an absolute of N .

""" 
    num = abs(n)
    if n == 0:
        return x
    elif n == 1:
        return y
    else:
        return sum_series(num-1, x, y) + sum_series(num-2, x, y)