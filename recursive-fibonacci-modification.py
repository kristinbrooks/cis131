"""
    script: recursive-fibonacci-modification.py
    action: fibonacci function modified to keep count of the number of recursions
    author: Kristin Brooks
    date:   07/14/26
"""

def fibonacci(n):
    fibonacci.count += 1
    if n in (0,1):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    for i in range(10, 31, 10):
        fibonacci.count = 0
        print(f'fibonacci({i}) is {fibonacci(i)}, function was called {fibonacci.count} times')

if __name__ == '__main__':
    main()
