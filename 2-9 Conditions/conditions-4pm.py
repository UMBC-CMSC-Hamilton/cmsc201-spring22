"""
    What is an if statement?

        If statements allow our code branch
            Make decisions, doing one thing if a condition is true
            doing another thing perhaps if that condition is false



"""
if False:
    x = 7
    if x > 20:
        print('x is big')
    else:
        print('x is not big')

    if x == 5 or x == 12:
        print('x is five or twelve')

    # if x == 5 or 12:
    #     print('x is five or twelve again')

    value = "\t"
    if value:
        print(f'{value} is true')
    else:
        print(f'{value} is false')
    """
        integer type 
            0 -> False
            anything else -> True
        float type
            0 -> False
            anything else -> True
        strings
            empty -> False
            anything else -> True
    """

    if x == 5 or 12:
        print('happens all the time')

    """
        Order of Operations or Operator Precedence
        
        precedence = what happens first
        
        Arithmetic Operators (int, float) op (int, float) -> (int, float)
            +, -, *, /, //, %, **, ()
            low --->> medium --> higher
            
        Comparison Operators (int float string) op (int float string) -> boolean
            ==, <, >, <=, >=, !=
            in for strings
            
        Logical Operators
            not - higher precedence than and / or
            and / or - equal precedence lowest of all operators
        
        Secret rule is L -> R
    """

    x = int(input('Tell me an int: '))
    y = int(input('Tell me an int: '))

    my_string = input('Enter a string: ')

    if x * y < 100 and my_string != 'hello':
        print('this if works')
    else:
        print('this if doesn\'t work\"')

    if 0 <= x <= 10:
        print('x is between 0 and 10')

    if 0 <= x and x <= 10:
        print('x is between 0 and 10')

# else if ==> elif
x = int(input('Enter a number between 1 and 5: '))
if x == 1:
    print('x is definitely 1')
elif x == 2:
    print('x seems like its 2')
elif x == 3:
    print('x may or may not be 3')
if x == 4:
    print('there is a distinct possibility that x is 4')
elif x == 5:
    print('I am getting a strong feeling that x is 5')
else:
    print('You need to enter a number between 1 and 5')

"""
    When you have an if statement only one block ever EXECUTES
    
    How many elif blocks can execute in an if statement?
        0 or 1
    How many elif statements can accompany an if statement?
        as many as you like < 1000000 probably
    How many else blocks can there be?
        one
    How many if blocks can there be?
        one
    Do you need an else for any if statement?
        no it'll be fine
"""
my_string = input('How are you feeling?')

if my_string == 'happy':
    print('that sounds nice')
elif my_string == 'sad':
    print('oh no that isn\'t as nice')
# no else required
