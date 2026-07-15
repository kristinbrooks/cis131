"""
    script: recursive-power-function.py
    action: a recursive version of the power function
    author: Kristin Brooks
    date:   07/13/26
"""
def power(base, exponent):
    # base case
    if exponent == 1:
        return base
    return base * power(base, exponent - 1)

def main():
    user_base = int(input('Enter the exponent base: '))
    user_exponent = int(input('Enter the exponent: '))
    print(f'{user_base}^{user_exponent} = {pow(user_base, user_exponent)}.')

if __name__ == '__main__':
    main()
