"""
    script: recursive-fibonacci-modification2.py
    action: fibonacci function modified to keep count of the number of recursions
    author: Kristin Brooks
    date:   07/15/26
"""

def fibonacci(n):
    # base case
    if n in (0,1):
        return n, 1
    else:
        # get the fibonacci numbers and counts from n-1 and n-2
        (fib_num1, fib_count1) = fibonacci(n-1)
        (fib_num2, fib_count2) = fibonacci(n-2)

        #sum the fibonacci numbers and counts and add 1 to count for the current call
        fib_num = fib_num1 + fib_num2
        fib_count = fib_count1 + fib_count2 + 1

        return fib_num, fib_count

def main():
    for i in range(10, 31, 10):
        number, count = fibonacci(i)
        print(f'fibonacci({i}) is {number}, function was called {count} times')

if __name__ == '__main__':
    main()
