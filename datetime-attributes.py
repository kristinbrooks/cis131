"""
    script: datetime-attributes.py
    action: demonstration of datetime class's attributes
    author: Kristin Brooks
    date:   07/09/26
"""
from datetime import datetime

x = datetime.now()
y = datetime.now()
print(f'x: {x}')
print(f'y: {y}')
print(f'x.year: {x.year}')
print(f'x.month: {x.month}')
print(f'x.day: {x.day}')
print(f'x.hour: {x.hour}')
print(f'x.minute: {x.minute}')
print(f'x.second: {x.second}')
print(f'x.microsecond: {x.microsecond}')
print(f'y.year: {y.year}')
print(f'y.month: {y.month}')
print(f'y.day: {y.day}')
print(f'y.hour: {y.hour}')
print(f'y.minute: {y.minute}')
print(f'y.second: {y.second}')
print(f'y.microsecond: {y.microsecond}')
print(f'x < y: {x < y}')
print(f'x > y: {x > y}')
print(f'x <= y: {x <= y}')
print(f'x >= y: {x >= y}')
print(f'x == y: {x == y}')
print(f'x != y: {x != y}')
print(f'y - x: {y - x}')
