"""
    script: fraction-complex-attributes.py
    action: demonstration of the attributes of the class Fraction and built-in complex numbers
    author: Kristin Brooks
    date:   07/09/26
"""
from fractions import Fraction

# fractions
print('Fractions:')
f1 = Fraction(3, 4)
f2 = Fraction(5, 6)
print(f'f1: Fraction({f1.numerator}, {f1.denominator})')
print(f'f2: Fraction({f2.numerator}, {f2.denominator})')
print(f'f1 + f2 = Fraction({(f1 + f2).numerator}, {(f1 + f2).denominator})')
print(f'f1 - f2 = Fraction({(f1 - f2).numerator}, {(f1 - f2).denominator})')
print(f'f1 * f2 = Fraction({(f1 * f2).numerator}, {(f1 * f2).denominator})')
print(f'f1 / f2 = Fraction({(f1 / f2).numerator}, {(f1 / f2).denominator})')
print(f'f1: {f1}')
print(f'f2: {f2}')
print(f'float(f1): {float(f1)}')
print(f'float(f2): {float(f2)}')
print()

# complex numbers
print('Complex Numbers:')
c1 = complex(3, 4)
c2 = 5 + 6j
print(f'c1: {c1}')
print(f'c2: {c2}')
print(f'c1 + c2 = {c1 + c2}')
print(f'c1 - c2 = {c1 - c2}')
print(f'c1.real: {c1.real}')
print(f'c1.imag: {c1.imag}')
print(f'c2.real: {c2.real}')
print(f'c2.imag: {c2.imag}')
