"""
    What is an if statement?
        An if statement is a way to allow our code to branch

        Allows programs to make decisions

        Anything inside of an if statement needs to be tabbed in by one
"""
if False:
    my_int = int(input('Tell me an integer between 1 and 10: '))

    # if 1 <= my_int and my_int <= 10: equivalent expression
    if 1 <= my_int <= 10:
        print('Valid')
    else:
        print('Invalid')

    my_string = input('Tell me a string: ')
    # my_string.upper() == 'HELLO'
    if my_string.lower() == 'hello' and my_int != 5:
        print('Hello back')

    print(my_string)

    my_other_int = int(input('Tell me another int: '))

    if my_int < my_other_int or my_other_int > 100:
        print('yep it is')
    else:
        print('nope it\'s not')
    if True:
        print('True is very true')

    menu_choice = int(input('Choose 1, 2, 3, 4, 5: '))
    if menu_choice == 1:
        print('new game')
    # elif == else if
    elif menu_choice == 2:
        print('load game')
    elif menu_choice == 3:
        print('save game')
    # elif menu_choice == 3: more like a bug in the code
    #    print('something else in the game')
    elif menu_choice == 4:
        print('settings')
    elif menu_choice == 5:
        print('exit')
    else:
        print('invalid option')
        print('everything that should run should be here')
        print('there doesnt need to be another else')
    # else: sorry only one else
    #    print('i want another else')

    """
        How many if statements can you have in a single if expression?
            1
            in a single expression is the important part
            you can have two separate if statements one after another
            don't affect each other
        How many elif statements can you have?
            As many as you want
        How many elses can we have?
            1 per if statement
            
        How many elif statements execute in a single if expression?
            1 or 0
            "at most how many execute"
    """

    """
        Order of operations == operator precedence
        
        parentheses - the highest precedence operator ever in the universe
        
        arithmetic operators - takes in two numbers (ints or floats) spits out a number
            examples = +, -, *, /, //, %, **
            PEDMAS
            
            BODMAS
            
        comparison operators - return True or False
            == (equality not assignment), <, >, <=, >=, !=
            in
        logical operators
            and, or
            not
    """

    x = 5
    y = 5
    if 2 + x < 3 + y:
        print('yes')

    if (x + 1 < y + 3) or (x - 2 < x - 5):
        print('yep')

    print(2 ** (1/2))

"""
    If you evaluate an integer as a boolean 
        if    0  -> False
            != 0 -> True
        what about floats?
            same thing, all floats are true except 0
                which is false
        strings
            a string which is empty is false 
            all other strings that contain anything are True
"""
x = ""
if x:
    print(f'{x} is true')
else:
    print(f'{x} is false')
