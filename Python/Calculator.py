import math
from math import floor

First =int(input('Enter first number: '))
Second = int(input('Enter second number: '))
Operator = input('Enter operator: ')

if Operator == '+':
    print(f'{First} + {Second} =', First + Second)
elif Operator == '-':
    print(f'{First} - {Second} =', First - Second)
elif Operator == '*':
    print(f'{First} * {Second} =', First * Second)
else:
    print(f'{First} / {Second} =', (First/Second))


