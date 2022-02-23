"""
    if statements
        handle branching
        make decisions in the program

"""

a = 4
b = 17

if a == 5:
    print('a is five')
elif b == 17:
    print('b is 17')

# if you want both of them to execute then maybe change elif to if

x = 9
if x == 3 or x == 9:
    print('x is 3 or 9')
elif x > 0:
    print('x is positive')

"""
    Remember that order of operations == operator precedence
    arithmetic PEMDAS
    comparisons ==, <=, >=, !=, <, >, in keyword
        all comparisons have the same precedence L-> R
    logic
        not - slightly higher than lowest
        and / or - equal precedence (lowest)
"""
x = 3
if x == 4 or 10:
    print('x is 4 or 10')

"""
    There are two or three divisions in python (depending on how you count)
    
    / , //, %
    
    What is the difference between / and //?
        / gives floats
        // gives integer division with positive remainder
        
    % - modulus division (mod)
        tells you the remainder (in python the remainder is positive)
"""

x = int(input('Enter x: '))
y = int(input('Enter y: '))
print(x / y)
print(x // y, x % y)

day_of_month = int(input('Enter the current day of the month: '))

my_int = int(input('something'))
my_float = float(input('something else'))
